PROJ_DIR := "new-project"
PKG_NAME := "new_pkg"
PORT := 8000

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
	python -Wignore -m unittest discover ; \
	flake8 zs_classification bin --exclude schema_pb2.py ; \
	black zs_classification bin --check --line-length=79 --exclude schema_pb2.py --experimental-string-processing

.PHONY: proto
proto:
	protoc --python_out=zs_classification schema.proto

.PHONY: run
run:
	python -m aylien_model_serving \
		--handler zs_classification.serving \
		--port $(PORT)
