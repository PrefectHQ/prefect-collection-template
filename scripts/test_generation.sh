#!/bin/bash

cookiecutter --no-input --overwrite-if-exists .

cd prefect-collection

conda create -n "prefect-collection" python=3.9 -y

eval "$(conda shell.bash hook)"

conda activate prefect-collection

pip install -e ".[dev]"