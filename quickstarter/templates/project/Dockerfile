FROM python:3.8-bullseye

WORKDIR /srv

RUN pip install --upgrade pip

ADD {{PKG_NAME}} ./{{PKG_NAME}}
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD Makefile ./

RUN make dev

CMD make run
