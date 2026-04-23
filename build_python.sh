#!/usr/bin/env bash
set -e
BASEDIR=$(dirname "$0")
cd "$BASEDIR"

if [ "$1" == "--dev" ]; then
    uv tool run maturin develop --features wgpu_rendering
else
    uv tool run maturin build --release --features wgpu_rendering
fi
