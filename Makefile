PROJ_DIR ?= new-project
PKG_NAME ?= new_pkg
PORT ?= 8000
CONTAINER := zs-classifier
VERSION ?= `cat VERSION`
DEMO_NAME ?= new-demo

# initialize a new project
.PHONY: new-project
new-project:
	python bin/create_project.py \
		--project-dir $(PROJ_DIR) \
		--pkg-name $(PKG_NAME)


# initialize a new demo within current project
.PHONY: new-demo
new-demo:
	python bin/create_demo.py --dirname $(DEMO_NAME)


.PHONY: dev
dev:
	pip install -e .


.PHONY: test
test:
	python -Wignore -m unittest discover ; \
	flake8 zs_classification bin --exclude schema_pb2.py ; \
	#black zs_classification bin --check --line-length=79 --exclude schema_pb2.py --experimental-string-processing


.PHONY: proto
proto:
	protoc --python_out=zs_classification schema.proto


# run service locally
.PHONY: run
run:
	python -m aylien_model_serving \
		--handler zs_classification.serving \
		--port $(PORT)


# build docker container
.PHONY: build
build:
	docker build --no-cache -t $(CONTAINER):$(VERSION) -f Dockerfile .
