PROJ_DIR := "new-project"
PKG_NAME := "new_pkg"

.PHONY: init
init:
	python bin/create_project.py \
		--project-dir $(PROJ_DIR) \
		--pkg-name $(PKG_NAME)

.PHONY: dev
dev:
	pip install -e .

.PHONY: test
test:
	python -Wignore -m unittest discover
	flake8 PKG_NAME_
