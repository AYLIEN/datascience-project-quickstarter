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
	flake8 bin aylien_zs_classifier --exclude *_pb2.py


# optional; if protobuf schema is used
.PHONY: proto
proto:
	protoc --python_out=aylien_zs_classifier schema.proto


# run service locally
.PHONY: run
run:
	gunicorn -b:$(PORT) 'aylien_zs_classifier.serving:run_app()' --log-level=$(LOG_LEVEL)


# service must be running, i.e. start "make run" first
.PHONY: example-request-add
example-request-add:
	curl -i -H "Content-Type: application/json" -X POST --data "@./examples/example_request_add.json" "http://localhost:8000/add"


.PHONY: example-request-classify
example-request-classify:
	curl -i -H "Content-Type: application/json" -X POST --data "@./examples/example_request_classify.json" "http://localhost:8000/classify"


# build docker container
.PHONY: build
build:
	docker build --no-cache -t $(CONTAINER):$(VERSION) -f Dockerfile .
	@echo "To run the container, use:"
	@echo "docker run -p 8000:8000 -e --rm -it $(CONTAINER):$(VERSION)"
