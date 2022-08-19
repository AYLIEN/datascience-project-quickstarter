FROM python:3.8-bullseye

WORKDIR /srv

RUN pip install --upgrade pip

ADD aylien_zs_classifier ./aylien_zs_classifier
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD Makefile ./

RUN pip install -e .
RUN pip install -r requirements.txt

CMD make run
