# {{PROJECT_NAME}}

#### New environment

Run `conda create -n <env-name> python=3.8` if you're using Anaconda, alternatively `python3.8 -m venv <env-path>`

Activate: <br>
Run `conda activate <env-name>` or `source <env-path>/bin/activate`

#### Install library
Run `make dev`

### New Demo

Within in a project, you can initialize a new demo as follows: <br>
`quickstart-streamlit --project . --name super-cool-demo`

or just run `quickstart-streamlit` and follow the instructions.

A demo directory with the given name and running streamlit skeleton will be created in [/demos](demos).

You can checkout the README generated in the new demo directory for further guidance.

### Create Another Project

Run `quickstart-project --path <new project path> --libname <new library name>`    

### Completing a project
Here is a checklist to turn the new project into a fully functional tool:
- [ ] implement your project's core functionality in the Python package
- [ ] maintain dependencies in `requirements.txt`
- [ ] implement a demo
- [ ] implement service
- [ ] write tests
