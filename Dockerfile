FROM python:3.7.9-stretch

WORKDIR /srv

RUN pip install --upgrade pip

ADD zs_classification ./zs_classification
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD Makefile ./
ADD model-serving ./model-serving

RUN ls

RUN pip install ./model-serving
RUN pip install -e .

CMD make run
