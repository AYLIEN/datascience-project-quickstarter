FROM python:3.7.9-stretch

WORKDIR /srv

RUN pip install --upgrade pip

ADD aylien_zs_classifier ./aylien_zs_classifier
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD Makefile ./

RUN pip install -e .

CMD make run
