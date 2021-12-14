CONTAINER     ?= PKG_NAME-demo
VERSION       ?= `cat VERSION`
PORT		  ?= 8000


.PHONY: run
run:
	streamlit --log_level debug run \
			  --server.port $(PORT) \
			  --server.baseUrlPath PKG_NAME \
		  	  demo.py


.PHONY: build
build:
	cd ../..; docker build --no-cache -t $(CONTAINER):$(VERSION) -f demos/DEMO_DIRNAME/Dockerfile .
