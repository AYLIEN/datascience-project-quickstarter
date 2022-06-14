import argparse
import os
import shutil
import json
from pathlib import Path


HERE = Path(os.path.abspath(__file__)).parent


def read_file(path):
    with open(path) as f:
        content = f.read()
    return content


def write_file(content, path):
    with open(path, "w") as f:
        f.write(content)


def read_replace_write(inpath, replacements, outpath):
    content = read_file(inpath)
    for k, v in replacements.items():
        content = content.replace(k, v)
    write_file(content, outpath)


def main():
    args = parse_args()

    assert args.name.strip() != ""

    project_dir = Path(args.project)
    template_dir = HERE / "templates" / "demo"
    demo_name = args.name
    demo_dir = project_dir /  Path("demos") / demo_name
    if demo_dir.exists():
        if input(f"Demo directory '{demo_dir}' already exists. Override? [yes/no] ") == "yes":
            shutil.rmtree(demo_dir)
    demo_dir.mkdir(parents=True)

    with open(project_dir / "project.json") as f:
        pkg_name = json.load(f)["package"]

    # Dockerfile
    read_replace_write(
        inpath=template_dir / "Dockerfile",
        replacements={"{{PKG_NAME}}": pkg_name, "{{DEMO_NAME}}": demo_name},
        outpath=demo_dir / "Dockerfile"
    )

    # files that are simply copied unmodified
    shutil.copy(template_dir / "Makefile", demo_dir)
    shutil.copy(template_dir / "README.md", demo_dir)
    shutil.copy(template_dir / "VERSION", demo_dir)
    shutil.copy(template_dir / "demo.py", demo_dir)

    print(f"Finished creating new demo: {args.name}")
    print(f"To run, do: cd demos/{args.name} && make run")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--name", required=True)
    return parser.parse_args()
