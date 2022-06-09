
# Data Science Project Quickstarter

This is a tool for bootstrapping real-world datascience projects that are maintainable, deployable, and easy to understand, from an opinionated template.
The quickstarter  lets you set up a new project with the following components:
* 📚 Python library
* 📨 Service
* ⚓ Docker container
* ✨ Streamlit demos

We also provide a few [examples](examples) of datascience projects that we bootstrapped with the quickstarter:
* A [zero-shot text classifier](examples/zs_classifier) which runs out-of-the-box, with accompanying research notebooks and a streamlit demo.
* (something else)

## Quickstart

### Clone & install quickstarter
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

### Completing a project
Here is a checklist to turn the new project into a fully functional tool:
- [ ] implement your project's core functionality in the Python package
- [ ] maintain dependencies in `requirements.txt`
- [ ] implement a demo
- [ ] implement service
- [ ] write unit tests


## Project Structure
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
├── setup.py
├── VERSION
```

An overview of each component of this template follows. We use our zero-shot classification project in [examples/aylien-zs-classifier](examples/zs-classifier) as an example.

#### The [`research/`](examples/aylien-zs-classifier/research) directory

In this directory, anything goes. The `research/` directory is the home of Jupyter notebooks and other exploratory analysis tools. This directory gives us the freedom to iterate quickly and break things, while still using git to keep track of the code and to facilitate easy sharing. Any code that is not ready for production, but that you still want to keep track of, can go into this directory.

#### The Python package directory (for example: [`aylien_zs_classifier/`](examples/aylien-sz-classifier/aylien_zs_classifier))

This is where the main source code of a project lives. We generally structure one project around one Python package. In early stages of a project we tend to prototype new features in notebooks or scripts in the `research/` directory. Once a new feature is ready to be used within the project, we add it to an existing or new module of the Python package from where it can be imported easily. For each module (.py file) in the package, we write unit tests in a file with a consistent naming convention: e.g. test_classifier.py for the module classifier.py.

The Python package also requires the `requirements.txt`, `setup.py` and `VERSION` files. Make sure to keep the dependencies in`requirements.txt` updated and depending on your deployment scenario, maintain the package version in the `VERSION` file.

#### The [`demos/`](examples/aylien-zs-classifier/demos) directory
This is the newest addition to our template. Over the last few years, amazing libraries like streamlit have drastically reduced the effort required to make interactive demos of data science projects. Streamlit in particular is fast-becoming an essential library for anyone building python-based prototypes. In  the `demos/` directory we put self-contained demos that are expected to have their own `requirements.txt` and `make run` commands. Interactive demos are one of the main ways for data scientists to communicate their work to the rest of an organization.

Check out our example for zero-shot-classification: [demos/zs-classifier-demo](demos/zs-classifier-demo)

#### The [`bin/`](examples/aylien-zs-classifier/bin) directory
This directory contains executable scripts, usually written in Python or bash. These are usually on-off data processing scripts that we keep separated from the python package modules for better clarity.


## Example Project: Zero-shot Event Classification

In addition to the templates included in this repo, we've also included an example data science project that works out of the box.

#### New environment
To use or work on this project, we first want to create a project-specific Python environment, let's call it `zsc`. <br>

Option 1 with Anaconda:
```bash
# Create new environment
conda create -n zsc python=3.8
# Activate new environment
conda activate zsc
```

Option 2 with Venv:
```bash
# Create new environment
python3.8 -m venv zsc
# Activate new environment
source zsc/bin/activate
```

#### Install
Run `make dev`

This will install the dependencies in `requirements.txt` and the `zs_classification` library in development mode.

Currently we also need install `model-serving`:

```
git clone git@github.com:AYLIEN/model-serving.git
pip install ./model-serving
```

#### Using the example library

Using the `aylien_zs_classifier` library to create a zero-shot text classifier:
```python
from aylien_zs_classifier.classifier import ZeroShotClassifier
from aylien_zs_classifier.vector_store import NaiveVectorStore
from sentence_transformers import SentenceTransformer
from pprint import pprint


model = SentenceTransformer("paraphrase-mpnet-base-v2", device="cpu")
classifier = ZeroShotClassifier(model=model, vector_store=NaiveVectorStore())

labels = ["fire", "water", "wind"]
descriptions = ["fire", "water", "wind"]
classifier.add_labels(labels, descriptions)

snippets = ["flame", "ocean", "hurricane"]
predictions = classifier.predict(snippets, output_scores=True)
pprint(predictions)
```

#### Using the example service

We also include an example service to demonstrate exposing your library via a REST API.
Use `make run` to get the service running locally. You can now create and interact with a classifier via post requests:

| Endpoint | Request Format | Explanation |
|---|---|---|
| `/add` | `{"label": "<label>", "description": "<description>"}` | Adding a new label |
| `/classify` | At minimum: `{"text": "<text>"}`<br>Optional settings: `{"text": "<text>", "threshold": 0.1, "topk": 10}` | Classify a text snippet |
| `/remove` | `{"label": "<label>"}` | Remove a label |
| `/reset` | (no data) | Delete all labels |

The requests have to follow a Protobuf schema defined in [schema.proto](schema.proto).

We provide request examples in [research/library_usage.py](research/service_usage.py).

## Docker image

Deployment will be easy once you have a working Docker image!
We can containerize our service by creating a Docker image:

```bash
# create Docker image
make build

# run container locally
docker run -p 8000:8000 -e --rm -it zs-classifier:0.1
```


## TODO

- [ ] install `model-serving` and the quickstarter via PyPI
- [ ] separate dev/prod dependencies
- [ ] add demo-specific requirements.txt files
- [ ] (optional) `bin/evaluate.py` and `make evaluate` for zero-shot classifier?
- [ ] rename `zs_classification` to e.g. `aylien_zs_classification` or so to show current best practices
- [ ] make command for docker run (currently only mentioned in readme)
