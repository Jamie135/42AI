#!/bin/bash

# Upgrade pip
pip install --upgrade pip

# Build distribution packages
python setup.py sdist bdist_wheel
