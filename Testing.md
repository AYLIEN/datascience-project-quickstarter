
## Testing the Quickstarter
The following steps explore the full range of provided actions/features of this tool. Run all of these to check if the tool works when making changes. We're planning to automate this in the future.

#### New project

1) Install quickstarter from pip (or locally if you made changes) <br>
`pip install datascience-quickstarter`

2) Create new project (e.g. name `qs-test`) <br>
`quickstart-project` + follow instructions

3) Create new environment <br>
`conda create -n qs-test python=3.8` (or non-conda alternative) <br>
`conda activate qs-test`

4) Install package of new project <br>
`cd qs-test && make dev`

  **Note**: if you made changes to the quickstarter, run `pip uninstall datascience-quickstarter` and install your local version using in development mode `pip install -e ...` at this step.

5) Run tests <br>
`make test`

  For the next steps, open a second terminal so that one terminal and use one to keep a service running and the other to send requests to the service.

6) Run service <br>
`make run`

7) Send requests <br>
`make example-request-count` <br>
`make example-request-reverse` <br>
`python examples/example_requests.py` <br>
(stop service)

8) Build Docker image for service <br>
`make build`

9) Run service within Docker container; run-command will also be printed after building. <br>
`docker run -p 8000:8000 -e --rm -it <package-name>:0.1`

10) Repeat 7), i.e. test sending requests <br>
(stop container)

#### New demo

8) Create new demo <br>
`quickstart-streamlit` (call it `cool-demo`)

9) Build Docker image for demo <br>
`cd demos/cool-demo` <br>
`make build`

10) Run demo with docker container; run-command will also be printed after building. <br>
`docker run -p 8000:8000 -e --rm -it cool-demo:0.1` <br>
(stop container)


#### Zero-shot classifier example

1) Create environment <br>
`conda create -n zsc python=3.8`

2) Install project package <br>
`cd examples/aylien-zs-classifier` <br>
`make dev`

3) Run tests <br>
`make test`

4) Run service <br>
`make run`

5) Send requests <br>
`example-request-add` <br>
`example-request-classify` <br>
`python examples/example_requests.py` <br>
 (stop service)

6) Build Docker image for service <br>
`make build`

7) Run service within Docker container; run-command will also be printed after building. <br>
`docker run -p 8000:8000 -e --rm -it aylien-zs-classifier:0.1`

8) Repeat 5), i.e. test sending requests <br>
(stop container)

9) Try out existing demo <br>
`cd zs-classifier-demo` <br>
`make run` (stop streamlit)

10) Build Docker image for demo <br>
`make build`

11) Run demo with docker container; run-command will also be printed after building. <br>
`docker run -p 8000:8000 -e --rm -it zs-classifier-demo:0.1`
