PORT ?= 8000
CONTAINER := aylien_zs_classifier
VERSION ?= `cat VERSION`
NUM_WORKERS ?= 1
LOG_LEVEL ?= DEBUG
DEMO_NAME ?= new-demo


.PHONY: dev
dev:
	pip install -e .
	pip install -r requirements.txt


.PHONY: demo
demo:
	@python -m quickstarter.create_demo --name $(DEMO_NAME)
	make run --directory demos/$(DEMO_NAME)


.PHONY: test
test:
	pytest aylien_zs_classifier
	pycodestyle aylien_zs_classifier --exclude *_pb2.py


# optional; if protobuf schema is used
.PHONY: proto
proto:
	protoc --python_out=aylien_zs_classifier schema.proto


# run service locally
.PHONY: run
run:
	gunicorn -b:$(PORT) 'aylien_zs_classifier.serving:run_app()' --log-level=$(LOG_LEVEL)


# build docker container
.PHONY: build
build:
	docker build --no-cache -t $(CONTAINER):$(VERSION) -f Dockerfile .
