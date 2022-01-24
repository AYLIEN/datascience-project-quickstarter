PROJECT_NAME ?= test-project
PROJECT_DIR ?= $(PROJECT_NAME)
PKG_NAME ?= `echo $(PROJECT_NAME) | tr "-" "_"`
PORT ?= 8000
CONTAINER := $(PKG_NAME)
VERSION ?= `cat VERSION`
DEMO_NAME ?= $(PROJECT_NAME)-demo


# initialize a new project
.PHONY: new-project
new-project:
	python templates/create_project.py \
		--project-dir $(PROJECT_DIR) \
		--pkg-name $(PKG_NAME)
	cd $(PROJECT_DIR) && \
	pip install -r requirements.txt && \
	pip install -e .
	echo "Finished creating project in directory: $(PROJECT_DIR)"

# initialize a new demo
.PHONY: new-demo
new-demo:
	python templates/create_demo.py --dirname $(DEMO_NAME)
	echo "Finished creating new demo: $(DEMO_NAME)"
	echo "To run, do: cd demos/$(DEMO_NAME) && make run"

# install locally
.PHONY: dev
dev:
	pip install -e .


# run tests
.PHONY: test
test:
	python -Wignore -m unittest discover ; \
	flake8 zs_classification bin --exclude schema_pb2.py ; \
	#black zs_classification bin --check --line-length=79 --exclude schema_pb2.py --experimental-string-processing

# compile protobuf schema
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

# git tag
.PHONY: tag
tag:
	git tag -a $(VERSION) -m "version $(VERSION)"
	git push origin $(VERSION)


