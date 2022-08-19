CONTAINER     ?= zs-classifier-demo
VERSION       ?= `cat VERSION`
PORT          ?= 8000


.PHONY: run
run:
	streamlit --log_level debug run \
			  --server.port $(PORT) \
			  --server.baseUrlPath zs-classifier \
		  	  demo.py


.PHONY: build
build:
	cd ../..; docker build --no-cache -t $(CONTAINER):$(VERSION) -f demos/zs-classifier-demo/Dockerfile .
	@echo "To run the container, use:"
	@echo "docker run -p 8000:8000 -e --rm -it $(CONTAINER):$(VERSION)"
