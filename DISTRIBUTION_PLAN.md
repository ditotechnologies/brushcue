# Plan: Distribute brushcue via PyPI + GitHub Mirror

## Context
`brushcue` is a Maturin-based PyO3 package (Python bindings to the `rust/matisse/py` crate). The Rust source is deeply embedded in the monorepo. The goal is to:
1. Publish installable wheels to PyPI so users can `pip install brushcue`
2. Maintain a public-facing GitHub mirror of just the Python package files (no Rust source)
3. Keep the mirror in sync automatically via GitHub Actions

---

## Part 1: PyPI Publishing

### 1a. Enhance pyproject.toml for PyPI
**File:** `py/brushcue/pyproject.toml`

Add PyPI metadata:
```toml
[project]
name = "brushcue"
version = "0.1.0"
description = "Python bindings for the Matisse graph computation system"
requires-python = ">=3.11"
dependencies = []
license = { text = "Proprietary" }
authors = [{ name = "Dito Technologies LLC" }]

[project.urls]
Homepage = "https://github.com/<org>/brushcue"   # mirror repo URL
```

### 1b. Create publish workflow
**New file:** `.github/workflows/brushcue-publish.yml`

Trigger: push of a tag matching `brushcue-v*` (e.g. `brushcue-v0.1.0`)

Steps per platform matrix:
- **Linux x86_64**: `maturin-action` with `manylinux` container
- **Linux aarch64**: `maturin-action` with QEMU cross-compilation
- **macOS arm64**: native macOS-latest runner
- **macOS x86_64**: macOS-latest runner (cross-target `x86_64-apple-darwin`)

Each step produces `.whl` files which are uploaded to a shared artifact. A final `publish` job uploads all wheels to PyPI using **trusted publishing** (OIDC — no long-lived secrets).

Use `PyO3/maturin-action@v1` which handles the `manifest-path` flag to point at the Rust workspace.

Key maturin flags:
```
--manifest-path rust/matisse/py/Cargo.toml
--out dist
--release
--features ...   # if any
```

PyPI trusted publishing requires one-time setup on pypi.org: create the project, go to Publishing → add a trusted publisher pointing to this repo + workflow name.

---

## Part 2: GitHub Mirror (Python-only)

### 2a. Create the mirror repo
Manually create `github.com/<org>/brushcue` (public). Initialize with no files.

The mirror will contain:
```
brushcue/           ← the Python package files (from py/brushcue/brushcue/)
pyproject.toml      ← from py/brushcue/pyproject.toml (note: not buildable without Rust source)
README.md           ← from py/brushcue/README.md
```

The pyproject.toml can stay as-is (documents how it's built) but users should know to `pip install brushcue` rather than build from source.

### 2b. Create mirror sync workflow
**New file:** `.github/workflows/brushcue-mirror.yml`

Trigger: push to `main` when `py/brushcue/**` changes

Steps:
1. Checkout monorepo with full history
2. Use `cpina/github-action-push-to-another-repository` (or raw git commands) to:
   - Clone the mirror repo using a deploy key or PAT stored in monorepo secrets
   - Copy `py/brushcue/` contents to the mirror
   - Commit and push

Secret needed: `BRUSHCUE_MIRROR_DEPLOY_KEY` — an SSH deploy key with write access to the mirror repo, stored in the monorepo's GitHub Secrets.

---

## Part 3: One-time Setup Steps (manual, outside code)

1. **Create the mirror repo** on GitHub
2. **Generate SSH deploy key**: `ssh-keygen -t ed25519 -C "brushcue-mirror"`
   - Add public key to mirror repo → Settings → Deploy keys (with write access)
   - Add private key to monorepo → Settings → Secrets → `BRUSHCUE_MIRROR_DEPLOY_KEY`
3. **Set up PyPI trusted publishing**:
   - Create `brushcue` project on pypi.org (or test.pypi.org first)
   - Add trusted publisher: repo=`<monorepo>`, workflow=`brushcue-publish.yml`, environment=`pypi`
4. **Create a GitHub environment** named `pypi` in the monorepo (required for OIDC)

---

## Critical Files

| File | Action |
|------|--------|
| `py/brushcue/pyproject.toml` | Add PyPI metadata (author, license, URLs) |
| `.github/workflows/brushcue-publish.yml` | New — builds + publishes wheels to PyPI on version tag |
| `.github/workflows/brushcue-mirror.yml` | New — syncs Python files to mirror repo on push to main |

---

## Verification

1. **Test publish**: Push tag `brushcue-v0.1.0-test` pointing at the workflow; check if wheels appear as artifacts. Use test.pypi.org first.
2. **Test install**: `pip install --index-url https://test.pypi.org/simple/ brushcue` in a fresh venv on macOS/Linux.
3. **Test mirror**: Push a trivial change to `py/brushcue/README.md` on main; verify the mirror repo's commit appears within minutes.
