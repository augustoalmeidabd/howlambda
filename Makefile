clean:
	rm -rf .venv day-summary *.checkpoint .pystest_cache .coverage

init: clean
	pip install poetry
	poetry install