CONTAINER     := zs-classifier-demo
VERSION       ?= `cat VERSION`


.PHONY: run
run:
	streamlit --log_level debug run \
			  --server.port 8000 \
			  --server.baseUrlPath zs-classifier \
		  	  demo.py


.PHONY: build
build:
	cd ../..; docker build --no-cache -t $(CONTAINER):$(VERSION) -f demos/zs-classifier-demo/Dockerfile .
