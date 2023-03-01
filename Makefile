SHELL=/bin/bash

.DEFAULT_GOAL := help

.PHONY: help
help: ## Shows this help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: clean install checkov test ## Clean environment and reinstall all dependencies

.PHONY: clean
clean: ## Removes project virtual env
	rm -rf .venv cdk.out build dist **/*.egg-info .pytest_cache node_modules .coverage

.PHONY: install
install: ## Install the project dependencies and pre-commit using Poetry.
	poetry install --with lint,test,checkov
	poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push

.PHONY: test
test: ## Run tests
	poetry run python -m pytest

.PHONY: lint
lint: ## Apply linters to all files
	poetry run pre-commit run --all-files

.PHONY: synth
synth: ## Synthetize all Cdk stacks
	poetry run cdk synth

.PHONY: checkov
checkov: synth ## Run Checkov against IAC code
	poetry run checkov --config-file .checkov --baseline .checkov.baseline

.PHONY: checkov-baseline
checkov-baseline: synth ## Run checkov and create a new baseline for future checks
	poetry run checkov --config-file .checkov --create-baseline --soft-fail
	mv cdk.out/.checkov.baseline .checkov.baseline
