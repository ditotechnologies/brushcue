#!/usr/bin/env bash
set -e
BASEDIR=$(dirname "$0")
cd "$BASEDIR"

if [ "$1" == "--dev" ]; then
    uv tool run maturin develop
else
    uv tool run maturin build --release
fi
