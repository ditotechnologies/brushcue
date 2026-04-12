#!/usr/bin/env bash
set -e
BASEDIR=$(dirname "$0")
cd "$BASEDIR"

uv tool run pdoc brushcue --output-dir ../../js/monet/public/docs/py
