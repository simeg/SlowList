.PHONY: ci coverage docs install lint

# Travis cannot use 'pushd' or 'popd' without SHELL defined
SHELL := /bin/bash

ci: lint coverage

# Run tests and generate coverage data
coverage:
	coverage run *.test.py

docs:
	pdoc --html --output-dir docs SlowList
	mv docs/SlowList.html docs/index.html

install:
	pip install -r requirements.txt

lint:
	pycodestyle --format=pylint *.py
