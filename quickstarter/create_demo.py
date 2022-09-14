import argparse
import os
import shutil
import json
import re
from quickstarter import utils
from pathlib import Path


HERE = Path(os.path.abspath(__file__)).parent


class NoProjectException(Exception):
    pass


def main():
    args = parse_args()

    current_dir = Path.cwd()
    if not utils.is_quickstarter_project(current_dir):
        raise NoProjectException(
            f"{current_dir} is not a (quickstarter-)project directory. "
            "You need to be in a project directory to create a demo."
        )
    else:
        project_dir = current_dir

    if args.name is None:
        demo_name = input(
            "Please pick a name for the demo: "
        )
    else:
        demo_name = args.name

    template_dir = HERE / "templates" / "demo"
    demo_dir = project_dir / Path("demos") / demo_name
    if demo_dir.exists():
        if input(
            f"Demo directory '{demo_dir}' already exists. Override? [yes/no] "
        ) == "yes":
            shutil.rmtree(demo_dir)
    demo_dir.mkdir(parents=True)

    try:
        with open(project_dir / "project.json") as f:
            pkg_name = json.load(f)["package"]
    except FileNotFoundError:
        print(f'`project.json` was not found in {project_dir}')
        pkg_name = re.sub('-', '_', demo_name)
        print(
            "Initializing Dockerfile for demo with "
            f"Python package name: {pkg_name}"
        )

    # demo.py
    utils.read_replace_write(
        inpath=template_dir / "demo.py",
        replacements={"{{PKG_NAME}}": pkg_name, "{{DEMO_NAME}}": demo_name},
        outpath=demo_dir / "demo.py"
    )

    # Dockerfile
    utils.read_replace_write(
        inpath=template_dir / "Dockerfile",
        replacements={"{{PKG_NAME}}": pkg_name, "{{DEMO_NAME}}": demo_name},
        outpath=demo_dir / "Dockerfile"
    )

    # Makefile
    utils.read_replace_write(
        inpath=template_dir / "Makefile",
        replacements={"{{PKG_NAME}}": pkg_name, "{{DEMO_NAME}}": demo_name},
        outpath=demo_dir / "Makefile"
    )

    # files that are simply copied unmodified
    shutil.copy(template_dir / "README.md", demo_dir)
    shutil.copy(template_dir / "requirements_demo.txt", demo_dir)
    shutil.copy(template_dir / "VERSION", demo_dir)

    print(f"Finished creating new demo: {demo_name}")
    print(f"To run, do: cd demos/{demo_name} && make run")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        help="name of the demo; used as directory name"
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
