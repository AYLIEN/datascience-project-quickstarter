FROM python:3.7.9-stretch

WORKDIR /srv

RUN ls .

RUN pip install --upgrade pip

ADD {{PKG_NAME}} ./{{PKG_NAME}}
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD demos/{{DEMO_NAME}}/demo.py ./
ADD demos/{{DEMO_NAME}}/Makefile ./

RUN ls .

RUN pip install -e .

CMD make run
