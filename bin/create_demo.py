import argparse
import shutil
import json
from pathlib import Path


def read_file(path):
    with open(path) as f:
        content = f.read()
    return content


def write_file(content, path):
    with open(path, "w") as f:
        f.write(content)


def main(args):
    assert(args.dirname.strip() != "")

    project_dir = Path(".")
    template_dir = Path("resources/demo_template")
    demo_dirname = args.dirname
    demo_dir = Path("demos") / demo_dirname
    if demo_dir.exists():
        raise FileExistsError("This demo directory exists.")
    demo_dir.mkdir()

    with open("project.json") as f:
        pkg_name = json.load(f)["package"]

    # Readme
    readme_content = read_file(template_dir / "README.md")
    readme_content = readme_content.replace("PROJECT_NAME", project_dir.name)
    write_file(readme_content, demo_dir / "README.md")

    # Makefile
    makefile_content = read_file(template_dir / "Makefile")
    makefile_content = makefile_content.replace("PKG_NAME", pkg_name)
    makefile_content = makefile_content.replace("DEMO_DIRNAME", demo_dirname)
    write_file(makefile_content, demo_dir / "Makefile")

    # Dockerfile
    dockerfile_content = read_file(template_dir / "Dockerfile")
    dockerfile_content = dockerfile_content.replace("PKG_NAME", pkg_name)
    dockerfile_content = dockerfile_content.replace("DEMO_DIRNAME", demo_dirname)
    write_file(dockerfile_content, demo_dir / "Dockerfile")

    # files that are simply copied unmodified
    shutil.copy(template_dir / "VERSION", demo_dir)
    shutil.copy(template_dir / "demo.py", demo_dir)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirname', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
