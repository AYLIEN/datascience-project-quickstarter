# Data Science Project Quickstarter

This is a tool for bootstrapping real-world datascience projects that are easy to understand, 
easy to deploy, easy to customise, and easy to maintain.

The quickstarter  lets you set up a new project with the following components:
* 📚 Python library
* 📨 Service
* ⚓ Docker container
* ✨ Streamlit demo(s)

This repo also contains a few [examples](examples) of datascience projects that we bootstrapped with the quickstarter:
* A [zero-shot text classifier](examples/zs_classifier) which runs out-of-the-box, with accompanying research notebooks and a streamlit demo.
* (something else)

## Quickstart

### Installation
(todo: replace this with `pip`)
```
git clone https://github.com/AYLIEN/datascience-project-quickstarter
cd datascience-project-quickstarter
pip install .
```

### Creating a new project

As an example, let's call our new project `cool-project`, and name the Python library associated with this  project `cool_library`. Let's say the project will live in `~/projects/cool-project`. Let's save these as variables:
```
export PROJECT_NAME=cool-project
export PROJECT_DIR=~/projects/cool-project
export LIBNAME=cool_library
```

To create this project, use the installed `quickstart-project` command as follows:
```
quickstart-project --path $PROJECT_DIR --libname $LIBNAME
```

Create and activate a new project-specific environment (we like [miniconda](https://docs.conda.io/en/latest/miniconda.html)):
```
# skip the next two lines if you prefer to create python environments in a different way
conda create -n $PROJECT_NAME python=3.8
conda activate $PROJECT_NAME
```
Go to the new project and install it:
```
cd $PROJECT_DIR && make dev
```
### Create a new demo
We begin many projects by creating a proof-of-concept in a Streamlit demo.
Simply run this to create a new demo:
```
quickstart-demo --project $PROJECT_DIR --name super-cool-demo
```
It will appear in the `demos/` subdirectory of your data-science project.

### Running the project's service
A new project is already setup with a mock service that receives POST requests.  Start the service by simply running:
```
make run
```

### Building & running a Docker container
Deploying your service will be easy once you have a working Docker image!
Run this to containerize the service implemented in the project:
```bash
# create Docker image
make build

# run container locally
docker run -p 8000:8000 -e --rm -it <image name>:0.1
```


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

Below we explain how we structure our projects to support both exploratory research and production-ready code in the same repo. We have used this pattern effectively in 
many real-world projects. 


#### The [`research/`](examples/aylien-zs-classifier/research) directory

In this directory, anything goes. The `research/` directory is the home of Jupyter notebooks and other exploratory analysis tools. This directory gives us the freedom to iterate quickly and break things, while still using git to keep track of the code and to facilitate easy sharing. Any code that is not ready for production, but that you still want to keep track of, can go into this directory.

We don't like to use branches for non-production code because ideas tend to get lost in unmerged branches. So we commit research code directly to the `main` branch, but we put it in the `research/` directory. 
We only create branches for production features. 

#### The Python package directory (for example: [`aylien_zs_classifier/`](examples/aylien-sz-classifier/aylien_zs_classifier))

This is where the main source code of a project lives. We generally structure one project around one Python package. In early stages of a project we tend to prototype new features in notebooks or scripts in the `research/` directory. Once a new feature is ready to be used within the project, we add it to an existing or new module of the Python package from where it can be imported easily. For each module (`.py` file) in the package, we write unit tests in a file with a consistent naming convention: e.g. `test_classifier.py` for the module `classifier.py`.
Once the project is mature, the code in this library should be ready for production, meaning that it can be integrated into a larger system, shared on PyPI, or shipped in a docker container. 

The Python package also requires the `requirements.txt`, `setup.py` and `VERSION` files. Make sure to keep the dependencies in`requirements.txt` updated and depending on your deployment scenario, maintain the package version in the `VERSION` file.

#### The [`demos/`](examples/aylien-zs-classifier/demos) directory
This is the newest addition to our template. Over the last few years, amazing libraries like [streamlit](https://streamlit.io/) have drastically reduced the effort required to make interactive demos of data science projects. Streamlit in particular is fast-becoming an essential library for anyone building python-based prototypes. In  the `demos/` directory we put self-contained demos that are expected to have their own `requirements.txt` and `make run` commands. Interactive demos are one of the main ways for data scientists to communicate their work to the rest of an organization.

Check out our example for zero-shot-classification: [demos/zs-classifier-demo](demos/zs-classifier-demo)

#### The `bin` directory
This directory contains executable scripts, usually written in Python or bash. These are usually one-off data processing or shell scripts that we keep separated from the python package modules for better clarity.

#### The `resources/` directory
We usually store any large files required in a project such as model binaries or database-like files in `resources`. We usually add a `Makefile` command to obtain these resources locally from an external storage source, e.g. Google Cloud Storage, and do not track them with `git`.

## TODO

- [ ] install `model-serving` and the quickstarter via PyPI
- [ ] separate dev/prod dependencies
- [ ] add demo-specific requirements.txt files
- [ ] (optional) `bin/evaluate.py` and `make evaluate` for zero-shot classifier?
- [ ] make command for docker run (currently only mentioned in readme)
