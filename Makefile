.PHONY: ci install lint test

# Travis cannot use 'pushd' or 'popd' without SHELL defined
SHELL := /bin/bash

ci: lint coverage

coverage:
	coverage run *.test.py

install:
	pip install -r requirements.txt

lint:
	pycodestyle --format=pylint *.py

test:
	@echo "TODO"
