PROJECT_NAME ?= test-project
PROJ_DIR ?= $(PROJECT_NAME)
PKG_NAME ?= `echo $(PROJECT_NAME) | tr "-" "_"`
PORT ?= 8000
CONTAINER := zs-classifier
VERSION ?= `cat VERSION`
DEMO_NAME ?= new-demo


# initialize a new project
.PHONY: new-project
new-project:
	python templates/create_project.py \
		--project-dir $(PROJ_DIR) \
		--pkg-name $(PKG_NAME)
	cd $(PROJ_DIR)
	pip install -r requirements.txt
	pip install -e .
	echo "Finished creating project in directory: $(PROJ_DIR)"

# initialize a new demo within current project
.PHONY: new-demo
new-demo:
	python templates/create_demo.py --dirname $(DEMO_NAME)

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


