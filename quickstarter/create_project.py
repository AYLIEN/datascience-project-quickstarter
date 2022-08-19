import argparse
import os
import shutil
import json
from quickstarter import utils
from pathlib import Path


HERE = Path(os.path.abspath(__file__)).parent


def main():
    args = parse_args()

    if args.path is None:
        project_dir = Path(input(
            "Hi, let's set up a new project! \n"
            "Please name the project directory (cannot already exist): "
        ))
        if project_dir.exists():
            utils.override_old_project(project_dir)
    else:
        project_dir = Path(args.path)

    if args.libname is None:
        package_name = input(
            "Please name your python package "
            "(e.g. 'aylien_zs_classification'): "
        )
        print("Python package name:", package_name)
    else:
        package_name = args.libname

    pkg_dir = project_dir / package_name
    template_dir = HERE / "templates" / "project"

    if project_dir.exists():
        utils.override_old_project(project_dir)

    project_dir.mkdir(parents=True)
    (project_dir / "demos").mkdir()
    (project_dir / "bin").mkdir()
    (project_dir / "resources").mkdir()
    (project_dir / "research").mkdir()
    (project_dir / "examples").mkdir()
    pkg_dir.mkdir()

    # Readme
    utils.read_replace_write(
        inpath=template_dir / "README.md",
        replacements={"{{PROJECT_NAME}}": project_dir.name},
        outpath=project_dir / "README.md"
    )

    # setup.py
    utils.read_replace_write(
        inpath=template_dir / "setup.py",
        replacements={"{{PKG_NAME}}": package_name},
        outpath=project_dir / "setup.py"
    )

    # Makefile
    utils.read_replace_write(
        inpath=template_dir / "Makefile",
        replacements={"{{PKG_NAME}}": package_name},
        outpath=project_dir / "Makefile"
    )

    # Dockerfile
    utils.read_replace_write(
        inpath=template_dir / "Dockerfile",
        replacements={"{{PKG_NAME}}": package_name},
        outpath=project_dir / "Dockerfile"
    )

    # example_module.py
    utils.read_replace_write(
        inpath=template_dir / "example_module.py",
        replacements={"{{PKG_NAME}}": package_name},
        outpath=pkg_dir / "example_module.py"
    )

    # serving.py
    utils.read_replace_write(
        inpath=template_dir / "serving.py",
        replacements={"{{PKG_NAME}}": package_name},
        outpath=pkg_dir / "serving.py"
    )

    # test_serving.py
    utils.read_replace_write(
        inpath=template_dir / "test_serving.py",
        replacements={"{{PKG_NAME}}": package_name},
        outpath=pkg_dir / "test_serving.py"
    )

    # TODO: make protobuf schema optional
    #
    # read_replace_write(
    #     inpath=template_dir / "schema.proto",
    #     replacements={"{{PKG_NAME}}": args.libname},
    #     outpath=project_dir / "schema.proto"
    # )

    # files that are simply copied unmodified
    shutil.copy(template_dir / "requirements.txt", project_dir)
    shutil.copy(template_dir / "VERSION", project_dir)
    shutil.copy(template_dir / ".gitignore", project_dir)
    shutil.copy(
        template_dir / "example_request.json", project_dir / "examples"
    )
    shutil.copy(
        template_dir / "example_requests.py", project_dir / "examples"
    )
    utils.write_file("", pkg_dir / "__init__.py")

    with open(project_dir / "project.json", "w") as f:
        f.write(json.dumps({"package": package_name}))

    print(
        f"""

        Finished bootstrapping a new project at: {project_dir},
        The python library is called {package_name}
        To install your project, do: `cd {project_dir} && make dev`
        (you probably want to create a new virtual environment first though.)

        To run the web service, do: `make run`
        To run the tests, do: `make test`

        The datascience quickstarter is maintained at: https://github.com/AYLIEN/datascience-project-quickstarter
        we are happy to accept your feedback and pull-requests.
        Have a nice day :-)
        """
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        help="path to project directory"
    )
    parser.add_argument(
        "--libname",
        help="name of Python library/package associated with the project"
    )
    return parser.parse_args()
