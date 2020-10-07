format:
	black .
	isort .
	docformatter -i -r . --wrap-summaries 88 --wrap-descriptions 88 

lint:
	env PYTHONPATH=. pytest --pylint --mypy --flake8 --ignore tests

test:
	env PYTHONPATH=. pytest tests --cov=senaug --cov-report term-missing --cov-report html

dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

install:
	pip install -r requirements.txt
