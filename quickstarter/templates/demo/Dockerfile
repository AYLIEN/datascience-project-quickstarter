FROM python:3.8-bullseye

WORKDIR /srv

RUN ls .

RUN pip install --upgrade pip

ADD {{PKG_NAME}} ./{{PKG_NAME}}
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD demos/{{DEMO_NAME}}/demo.py ./
ADD demos/{{DEMO_NAME}}/requirements_demo.txt ./
ADD demos/{{DEMO_NAME}}/Makefile ./

RUN ls .

RUN make dev
RUN pip install -r requirements_demo.txt

CMD make run
