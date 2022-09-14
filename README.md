# Data Science Project Quickstarter

This is a tool for bootstrapping real-world datascience projects that are easy to understand,
easy to deploy, easy to customise, and easy to maintain.

The quickstarter  lets you set up a new project with the following components:
* 📚 Python library
* 📨 Service
* ⚓ Docker container
* ✨ Streamlit demo(s)

This repo also contains a few [examples](examples) of datascience projects that we bootstrapped with the quickstarter:
* A [zero-shot text classifier](examples/aylien-zs-classifier) which runs out-of-the-box, with accompanying research notebooks and a streamlit demo.


## Quickstart

### Installation
```
pip install datascience-quickstarter
```

After installation finishes, the the following new commands will be available:
* `quickstart-project`
* `quickstart-demo`

### Creating a new project

To start a new project, simply run `quickstart-project` and you will be guided through the process.

You can also provide all required arguments directly, e.g.:
```
quickstart-project --path cool-project --libname cool_library
```
This will create a project in `cool-project` , including a Python package/library named `cool_library`.

Next, create and activate a new project-specific environment (we like [miniconda](https://docs.conda.io/en/latest/miniconda.html)):
```
# skip the next two lines if you prefer to create python environments in a different way
conda create -n cool-project python=3.8
conda activate cool-project
```
Go to the new project and install it:
```
cd cool-project && make dev
```

### Running the project's service
New projects are already setup with a mock service that receives POST requests.  Back in your project directory, start the service by simply running:
```
make run
```

The default service includes two routes as toy examples: `/reverse` which takes a `text` argument and `/count` with no arguments. Once the service is running, you try out sending requests, e.g. using
```
make example-request-count
make example-request-reverse
```
or by using the [python script](quickstarter/templates/project/example_requests.py) which shows how to send requests and receive responses as a client:
```
python examples/example_requests.py
```

#### Containerize the service with Docker
Deploying your service will be easy once you have a working Docker image!
Run this to containerize the service implemented in the project:
```bash
# create Docker image
make build

# run container locally
docker run -p 8000:8000 -e --rm -it <image name>:0.1
```

You can interact with the containerized service in the same way as earlier, e.g. by running `python examples/example_requests.py`.


### Creating new demos using Streamlit
We begin many projects by creating a proof-of-concept in a Streamlit demo.
Demos live inside a project. Simply run:
```
quickstart-streamlit
```
this will create new demo, e.g. called `cool-demo` in the `demos/` subdirectory of your new data science project. Move into the new demo directory and run the demo in the browser:
```
cd demos/cool-demo && make run
```

Within the demo directory `demos/cool-demo` you can develop the demo which is implemented in the script `demos/cool-demo/demo.py`.

#### Containerize demo with Docker
You can also containerize the whole demo using Docker! Within the demo folder, simply run:
```
make build
```
The Docker image will make sharing or deploying the demo easier.


### Completing a project
Here is a checklist to turn the new project into a fully functional tool:
- [ ] implement your project's core functionality in the Python package
- [ ] maintain dependencies in `requirements.txt`
- [ ] implement a demo
- [ ] implement service
- [ ] build Docker image & make sure containerized service works afterwards (this often takes a few debugging cycles)
- [ ] write tests for each new module in the Python package


## Data Science Project Structure

Let's have a closer look at how projects created by our quickstarter are built.
The top-level structure of our projects usually looks like this:
```
<project directory>/
├── <python package name>/
├── bin/
├── Makefile
├── README.md
├── requirements.txt
├── demos/
├── research/
├── resources/
├── setup.py
├── VERSION
```

An overview of each component of this template follows. Let's use the zero-shot classification project in [examples/aylien-zs-classifier](examples/aylien-zs-classifier) as an example.

Data science projects are different than other software projects, because they often result in both a body of exploratory research _and_ a codebase that is used in production.
Some engineering teams prefer to take prototypes from research and data-science teams and re-implement them from scratch, which is totally ok. However, we believe that
it is good practice for researchers and data science teams to strive to produce code libraries that can be used in production, meaning that code is well-tested, and follows good API design principles.

Below we explain how we structure our projects to support both exploratory research and production-ready code in the same repo. We have used this simple pattern effectively in
many real-world projects, ranging from research papers with accompanying codebases, to production services wrapping ML-models which handle millions of requests per day.


#### The [`research/`](examples/aylien-zs-classifier/research) directory

In this directory, anything goes. The `research/` directory is the home of Jupyter notebooks and other exploratory analysis tools. This directory gives us the freedom to iterate quickly and break things, while still using git to keep track of the code and to facilitate easy sharing and collaboration. Any code that is not ready for production, but that you still want to keep track of, can go into this directory.
If multiple members of the team are working on different ideas in parallel, just create multiple subdirectories in `research/` such as
`research/GAN-graph-based-meta-reinforcement-learning/...` and `research/bayesian-flow-multi-horizon-hypercubes/...`.

We don't like to use branches for non-production code because ideas tend to get lost in unmerged branches. So we commit research code directly to the `main` branch, but we put it in the `research/` directory.
We only create branches for production features (see below).

#### The Python package directory (for example: [`aylien_zs_classifier/`](examples/aylien-sz-classifier/aylien_zs_classifier))

This is where the main source code of a project lives. We generally structure each project around one Python package. In the early stages of a project, we tend to prototype new features in notebooks or scripts in the `research/` directory. Once we're confident that we have something working and useful, we add it to an existing or new module of the Python package from where it can be imported easily. For each module (`.py` file) in the package, we write unit tests in a file with a consistent naming convention: e.g. `test_classifier.py` for the module `classifier.py`.
Code that is added to the main Python package should be submitted in a branch, and ideally reviewed by at least one other person. In our projects, multiple review cycles are common, and we somethimes even end up moving an idea
to the `research/` directory if it's cool, but somehow not well-suited or relevant to the primary usecase of the project.

Once the project is mature, the code in the main Python package should be ready for production, meaning that it can be integrated into a larger system, shared on PyPI, or shipped in a docker container that exposes a service.

The main Python package also requires the `requirements.txt`, `setup.py` and `VERSION` files. Make sure to keep the dependencies in`requirements.txt` updated and depending on your deployment scenario, maintain the package version in the `VERSION` file.

#### The [`demos/`](examples/aylien-zs-classifier/demos) directory
This is the newest addition to our template. Over the last few years, amazing libraries like [streamlit](https://streamlit.io/) have drastically reduced the effort required to make interactive demos of data science projects. Streamlit in particular is fast-becoming an essential library for anyone building Python-based prototypes. In  the `demos/` directory we put self-contained demos that are expected to have their own `requirements.txt` and `make run` commands. Interactive demos are one of the main ways for data scientists to communicate their work to the rest of an organization.

Check out our example for zero-shot-classification: [demos/zs-classifier-demo](demos/zs-classifier-demo)

#### The `bin` directory
This directory contains executable scripts, usually written in Python or bash. These are usually one-off data processing or shell scripts that we keep separated from the python package modules for better clarity.

#### The `resources/` directory
We usually store any large files required in a project such as model binaries or database-like files in `resources`. We usually add a `Makefile` command to obtain these resources locally from an external storage source, e.g. Google Cloud Storage, and do not track them with `git`.

### Testing

Checkout [Testing.md](Testing.md) for instructions to test the datascience project quickstarter, e.g. for making changes.

### About

The datascience project quickstarter was conceived of and implemented by Demian Gholipour Ghalandari and Chris Hokamp.
Aishwarya Radhakrishnan provided feedback and code review, and created the current version of the model-serving library.
Many of the ideas in this template are based on John Glover's excellent approach to ml-ops and productionization of research work, in particular the use of Makefiles to expose the main entrypoints to projects.

![Aylien Labs Logo](vis/aylien-labs-logo-small.png)
