.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 main.py test_main.py __init__.py

run:
	python main.py

test:
	PYTHONPATH=. py.test --verbose -s

docker_build:
	docker build -t hello-world-printer-k7-2026 .