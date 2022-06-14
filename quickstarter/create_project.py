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

    try:
        assert args.path.strip() != ""
        project_dir = Path(args.path)
    except AssertionError:
        project_dir = input(
            "Please name the project directory "
            "(cannot already exist):")

    try:
        assert args.libname.strip() != ""
        package_name = args.libname
    except AssertionError:
        package_name = input(
            "Please name your python package (i.e. 'aylien_zs_classification'"
        )
    pkg_dir = project_dir / package_name
    template_dir = HERE / "templates" / "project"

    print("HERE:", HERE)
    print("PARENT:", HERE.parent)
    print("template dir:", template_dir)

    if project_dir.exists():
        if input(f"Project directory '{project_dir}' already exists. Override? [yes/no] ") == "yes":
            shutil.rmtree(project_dir)

    project_dir.mkdir(parents=True)
    (project_dir / "demos").mkdir()
    (project_dir / "bin").mkdir()
    (project_dir / "resources").mkdir()
    (project_dir / "research").mkdir()
    pkg_dir.mkdir()

    # Readme
    read_replace_write(
        inpath=template_dir / "README.md",
        replacements={"{{PROJECT_NAME}}": project_dir.name},
        outpath=project_dir / "README.md"
    )

    # setup.py
    read_replace_write(
        inpath=template_dir / "setup.py",
        replacements={"{{PKG_NAME}}": args.libname},
        outpath=project_dir / "setup.py"
    )

    # Makefile
    read_replace_write(
        inpath=template_dir / "Makefile",
        replacements={"{{PKG_NAME}}": args.libname},
        outpath=project_dir / "Makefile"
    )

    # Dockerfile
    read_replace_write(
        inpath=template_dir / "Dockerfile",
        replacements={"{{PKG_NAME}}": args.libname},
        outpath=project_dir / "Dockerfile"
    )

    # serving.py
    read_replace_write(
        inpath=template_dir / "serving.py",
        replacements={"{{PKG_NAME}}": args.libname},
        outpath=pkg_dir / "serving.py"
    )

    # test_serving.py
    read_replace_write(
        inpath=template_dir / "test_serving.py",
        replacements={"{{PKG_NAME}}": args.libname},
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
    write_file("", pkg_dir / "__init__.py")

    with open(project_dir / "project.json", "w") as f:
        f.write(json.dumps({"package": args.libname}))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        required=True,
        help="path to project directory"
    )
    parser.add_argument(
        "--libname",
        required=True,
        help="name of Python library/package associated with the project"
    )
    return parser.parse_args()
