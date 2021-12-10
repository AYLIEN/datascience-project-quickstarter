# Data Science Project Quick-Starter

This is an opinionated template for bootstrapping real-world datascience projects that are maintainable, deployable, and easy to understand.

This template lets you set up a new project with a running streamlit demo and a production-ready `Dockerfile` in minutes.

## Project Structure

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

An overview of each component of this template follows. 

#### The [`research/`](research) directory

In this directory, anything goes. The `research/` directory is the home of Jupyter notebooks and other exploratory analysis tools. This directory gives us the freedom to iterate quickly and break things, while still using git to keep track of the code and to facilitate easy sharing. Any code that is not ready for production, but that you still want to keep track of, can go into this directory.

#### The Python package directory (our example: [`zs_classification/`](zs_classification))

This is where the main source code of a project lives. We generally structure one project around one Python package. In early stages of a project we tend to prototype new features in notebooks or scripts in the `research/` directory. Once a new feature is ready to be used within the project, we add it to an existing or new module of the Python package from where it can be imported easily. For each module (.py file) in the package, we write unit tests in a file with a consistent naming convention: e.g. test_classifier.py for the module classifier.py.

The Python package also requires the `requirements.txt`, `setup.py` and `VERSION` files. Make sure to keep the dependencies in`requirements.txt` updated and depending on your deployment scenario, maintain the package version in the `VERSION` file.

#### The [`demos/`](demos) directory
This is the newest addition to our template. Over the last few years, amazing libraries like streamlit have drastically reduced the effort required to make interactive demos of data science projects. Streamlit in particular is fast-becoming an essential library for anyone building python-based prototypes. In  the `demos/` directory we put self-contained demos that are expected to have their own `requirements.txt` and `make run` commands. Interactive demos are one of the main ways for data scientists to communicate their work to the rest of an organization.

Check out our example for zero-shot-classification: [demos/zs-classifier-demo](demos/zs-classifier-demo)

#### The [`bin/`](bin) directory
This directory contains executable scripts, usually written in Python or bash. These are usually on-off data processing scripts that we keep separated from the python package modules for better clarity.


## Example Project: Zero-shot Event Classification

#### New environment
To use or work on this project, we first want to create a project-specific Python environment, let's call it `zsc`. <br>

Run `conda create -n zsc python=3.8` if you're using Anaconda, alternatively `python3.8 -m venv zsc`

Activate the environment: <br>
Run `conda activate zsc` or `source zsc/bin/activate`

#### Install library
Run `make dev`

This will install the dependencies in `requirements.txt` and the `zs_classification` library in development mode.

## Create New Project
To create a project, pick a project directory and a name for the project's Python package, and run:

`PROJ_DIR=my_project PKG_NAME=my_lib make init`

This will create an empty new project from scratch, including all of the default components described above.
