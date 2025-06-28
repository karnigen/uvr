#!/usr/bin/env bash

# uvr pytest
#uvr pytest --cov-report term-missing --cov-report html --cov-report xml --cov=uvr

cd ..

uv run pytest --cov=uvr --cov-report html:coverage --cov-report xml --cov-report term
