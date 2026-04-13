#!/usr/bin/env bash
set -e
BASEDIR=$(dirname "$0")
cd "$BASEDIR"

uv tool run pdoc brushcue --output-dir ../../js/monet/public/docs/py

EXAMPLES_DIR="$(pwd)/examples"
OUTPUT_DIR="$(pwd)/../../js/monet/public/docs/py/examples"
DOCS_HTML="$(pwd)/../../js/monet/public/docs/py/brushcue.html"
mkdir -p "$OUTPUT_DIR"
uv tool run jupyter nbconvert --to html --output-dir "$OUTPUT_DIR" "$EXAMPLES_DIR"/*.ipynb

uv tool run python3 - "$OUTPUT_DIR" "$DOCS_HTML" << 'PYEOF'
import pathlib, sys

output_dir = pathlib.Path(sys.argv[1])
docs_html = pathlib.Path(sys.argv[2])

# Rename underscore files to hyphens for clean URLs
for f in list(output_dir.glob('*.html')):
    hyphenated = f.with_name(f.name.replace('_', '-'))
    if hyphenated != f:
        f.rename(hyphenated)

# Build examples list HTML for injection
files = sorted(output_dir.glob('*.html'))
nav_items = ''.join(
    f'<li><a href="/docs/py/examples/{f.stem}">{f.stem.replace("-", " ").title()}</a></li>'
    for f in files
)
body_items = ''.join(
    f'<li><a href="/docs/py/examples/{f.stem}">{f.stem.replace("-", " ").title()}</a></li>'
    for f in files
)

nav_section = f'<h2>Examples</h2><ul>{nav_items}</ul>'
body_section = (
    '<section id="examples">'
    '<h2 id="examples-heading">Examples</h2>'
    f'<ul>{body_items}</ul>'
    '</section>'
)

html = docs_html.read_text()
html = html.replace('<h2>API Documentation</h2>', nav_section + '<h2>API Documentation</h2>', 1)
html = html.replace('<input id="mod-brushcue-view-s', body_section + '<input id="mod-brushcue-view-s', 1)
docs_html.write_text(html)
print(f'injected {len(files)} examples into {docs_html}')
PYEOF
