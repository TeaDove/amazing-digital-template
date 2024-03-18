PYTHON ?= .venv/bin/python

backend-install:
	cd backend && python3.11 -m venv .venv
	cd backend && $(PYTHON) -m pip install poetry
	cd backend && $(PYTHON) -m poetry update

backend-run:
	cd backend && $(PYTHON) web_entrypoint.py

infra-run:
	docker-compose -f docker-compose-infra.yaml up -d

lint:
	pre-commit run -a
