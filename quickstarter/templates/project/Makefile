PORT ?= 8000
CONTAINER := {{PKG_NAME}}
VERSION ?= `cat VERSION`
NUM_WORKERS ?= 1
DEMO_NAME ?= new-demo


.PHONY: dev
dev:
	pip install -e .
	pip install -r requirements.txt

.PHONY: test
test:
	pytest {{PKG_NAME}}
	pycodestyle {{PKG_NAME}} --exclude *_pb2.py


# optional; if protobuf schema is used
.PHONY: proto
proto:
	protoc --python_out={{PKG_NAME}} schema.proto


# run service locally
.PHONY: run
run:
	gunicorn -b:$(PORT) '{{PKG_NAME}}.serving:run_app()' --log-level=$(LOG_LEVEL)


# build docker container
.PHONY: build
build:
	docker build --no-cache -t $(CONTAINER):$(VERSION) -f Dockerfile .
