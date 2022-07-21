import argparse
import os
import shutil
import json
import re
from quickstarter import utils
from pathlib import Path


HERE = Path(os.path.abspath(__file__)).parent


def main():
    args = parse_args()

    if args.project is None:
        project_dir = None
        current_dir = Path.cwd()
        if utils.is_quickstarter_project(current_dir):
            if input(
                f"You're in the project {current_dir.name}. "
                f"Want to create a new demo in {current_dir.name}/demos? [y/n] "
            ) == "y":
                project_dir = current_dir
        if project_dir is None:
            project_dir = Path(input(
                "Please select an existing project directory to create a demo for: "
            ))
    else:
        project_dir = Path(args.project)

    if not project_dir.exists():
        raise FileNotFoundError(f"Project directory {project_dir} not found.")

    if args.name is None:
        demo_name = input(
            "Please pick a name for the demo: "
        )
    else:
        demo_name = args.name

    template_dir = HERE / "templates" / "demo"
    demo_dir = project_dir / Path("demos") / demo_name
    if demo_dir.exists():
        if input(f"Demo directory '{demo_dir}' already exists. Override? [yes/no] ") == "yes":
            shutil.rmtree(demo_dir)
    demo_dir.mkdir(parents=True)

    try:
        with open(project_dir / "project.json") as f:
            pkg_name = json.load(f)["package"]
    except FileNotFoundError:
        print(f'`project.json` was not found in {project_dir}')
        pkg_name = re.sub('-', '_', demo_name)
        print(f'Initializing Dockerfile for demo with Python package name: {pkg_name}')

    # Dockerfile
    utils.read_replace_write(
        inpath=template_dir / "Dockerfile",
        replacements={"{{PKG_NAME}}": pkg_name, "{{DEMO_NAME}}": demo_name},
        outpath=demo_dir / "Dockerfile"
    )

    # files that are simply copied unmodified
    shutil.copy(template_dir / "Makefile", demo_dir)
    shutil.copy(template_dir / "README.md", demo_dir)
    shutil.copy(template_dir / "requirements.txt", demo_dir)
    shutil.copy(template_dir / "VERSION", demo_dir)
    shutil.copy(template_dir / "demo.py", demo_dir)

    print(f"Finished creating new demo: {demo_name}")
    print(f"To run, do: cd {demo_dir} && make run")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        help="path to project directory to which the new demo should belong"
    )
    parser.add_argument(
        "--name",
        help="name of the demo; used as directory name"
    )
    return parser.parse_args()
