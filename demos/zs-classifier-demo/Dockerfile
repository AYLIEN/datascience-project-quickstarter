FROM python:3.7.9-stretch

WORKDIR /srv

RUN ls .

RUN pip install --upgrade pip

ADD zs_classification ./zs_classification
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD demos/zs-classifier-demo/demo.py ./
ADD demos/zs-classifier-demo/Makefile ./

RUN ls .

RUN pip install -e .

CMD make run
