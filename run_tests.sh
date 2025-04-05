#!/usr/bin/env bash

# uvr pytest
#uvr pytest --cov-report term-missing --cov-report html --cov-report xml --cov=uvr

uvr pytest --cov=uvr --cov-report html:coverage --cov-report xml
