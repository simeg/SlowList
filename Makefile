.PHONY: ci coverage docs install lint

ci: install lint coverage

# Run tests and generate coverage data
coverage:
	coverage json -o .coverage.json *.test.py

docs:
	pdoc --html --output-dir docs SlowList
	mv docs/SlowList.html docs/index.html

install:
	pip install -r requirements.txt

lint:
	pylama *.py
