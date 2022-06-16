DEMO_NAME     ?= `basename \`pwd\``
CONTAINER     ?= `echo $(DEMO_NAME) | tr "_" "-"`-demo
VERSION       ?= `cat VERSION`
PORT		  ?= 8000


.PHONY: dev
dev:	
	pip install -r requirements.txt


.PHONY: run
run:
	streamlit \
		run demo.py \
		--logger.level debug \
		--server.port $(PORT) \
		--server.baseUrlPath $(DEMO_NAME)


.PHONY: build
build:
	cd ../..; docker build --no-cache -t $(CONTAINER):$(VERSION) -f demos/DEMO_DIRNAME/Dockerfile .
