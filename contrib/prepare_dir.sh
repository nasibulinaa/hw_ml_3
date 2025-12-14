#!/bin/bash

set -e

cd $(dirname $0)/..
if [[ -f .venv/bin/activate ]]; then
    source .venv/bin/activate
else
    exit 1
fi

python3 contrib/gen_models.py