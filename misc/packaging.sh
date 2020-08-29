#!/bin/sh

# Update wheel and setuptools
# pipenv update setuptools wheel twine > /dev/null 2>&1

# Clear previous archive
./misc/delete_package_files.sh

# Generate archive
pipenv run python setup.py sdist bdist_wheel

# Upload to pypi
# pipenv run python -m twine upload --repository testpypi dist/*
# pipenv run python -m twine upload dist/*

# Token:
# pypi-AgENdGVzdC5weXBpLm9yZwIkNzJlNTlkOGUtNWQ2MC00ODJmLThkZTQtNDc1M2MzYTE4NGIwAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiA-v-oeVfyICYm_jY_6eAMiAT9ydFykqUuyRvSQ91tMqg