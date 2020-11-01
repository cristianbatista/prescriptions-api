-include .env
export $(shell sed 's/=.*//' .env)

export APP_NAME = prescriptions
export PYTHONPATH=$(CURDIR)

format:
	@black prescriptions
	@isort --recursive prescriptionso

lint:
	@flake8 prescriptions
	@black --check prescriptions --diff
	@isort --recursive --check-only prescriptions

####################################
# Dependencies Commands
####################################
packages:
	@printf "Instalando bibliotecas... "
	@venv/bin/pip install -q --no-cache-dir -r requirements.txt
	@echo "OK"

env-create: env-destroy
	@printf "Criando ambiente virtual... "
	@virtualenv -q venv -p python3.8
	@echo "OK"

env-destroy:
	@printf "Destruindo ambiente virtual... "
	@rm -rfd venv
	@echo "OK"

install: env-create packages

infra-up:
	@docker-compose up -d


####################################
# App (Run, Debug and Test) Commands
####################################
test:
	@py.test -vv -rxs

coverage:
	@py.test -xs --cov kilimanjaro --cov-report xml --cov-report term-missing --cov-config .coveragerc

# Query (API)
debug-api:
	@uvicorn prescriptions.api.main:app --workers 3 --reload

run-api:
	@gunicorn kprescriptions.api.main:app -w 3 -k uvicorn.workers.UvicornWorker

docker-up:
	@docker-compose --log-level ERROR up -d

docker-down:
	@docker-compose down

docker-stop:
	@docker-compose stop
