help:
	@echo "clean:        remove all build, test, coverage and Python artifacts"
	@echo "clean-build:  remove build artifacts"
	@echo "clean-pyc:    remove Python file artifacts"
	@echo "clean-test:   remove test and coverage artifacts"
	@echo "lint:         check style with flake8"
	@echo "test:         run tests quickly with the default Python"
	@echo "test-all:     run tests on every Python version with tox"
	@echo "coverage:     check code coverage quickly with the default Python"
	@echo "release:      package and upload a release"
	@echo "dist:         package"
	@echo "install:      install the package to the active Python's site-packages"
	@echo "build:        Build (usually, requires to build when changes happen to the Dockerfile or docker-compose.yml)"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint_tests:
	flake8 leviathan_serving tests

test:
	docker-compose run --rm app pytest

test-all:
	tox

coverage:
	coverage run --source leviathan_serving setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

release: clean
	python setup.py sdist
	twine upload dist/*

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py install

lint:
	pre-commit run --all-files

bash:
	docker-compose run --rm app bash

migrations:
	docker-compose run --rm app python manage.py makemigrations

migrate:
	docker-compose run --rm app python manage.py migrate

rm:
	docker-compose down && docker-compose rm -f

up:
	docker-compose up -d

build:
	docker-compose build