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
    assert args.project_dir.strip() != ""
    assert args.pkg_name.strip() != ""

    template_dir = Path("resources/project_template")
    project_dir = Path(args.project_dir)
    if project_dir.exists():
        raise FileExistsError("This project directory exists.")

    pkg_dir = project_dir / args.pkg_name
    project_dir.mkdir()
    (project_dir / "demos").mkdir()
    (project_dir / "bin").mkdir()
    (project_dir / "resources").mkdir()
    (project_dir / "research").mkdir()
    pkg_dir.mkdir()

    # Readme
    readme_content = read_file(template_dir / "README.md")
    readme_content = readme_content.replace("PROJECT_NAME", project_dir.name)
    write_file(readme_content, project_dir / "README.md")

    # setup.py
    setup_py_content = read_file(template_dir / "setup.py")
    setup_py_content = setup_py_content.replace("PKG_NAME", args.pkg_name)
    write_file(setup_py_content, project_dir / "setup.py")

    # Makefile
    makefile_content = read_file(template_dir / "Makefile")
    # using placeholder PKG_NAME_ instead of PKG_NAME because PKG_NAME
    # needs to remain a placeholder for "make init" command
    makefile_content = makefile_content.replace("PKG_NAME_", args.pkg_name)
    write_file(makefile_content, project_dir / "Makefile")

    # Dockerfile
    dockerfile_content = read_file(template_dir / "Dockerfile")
    dockerfile_content = dockerfile_content.replace("PKG_NAME", args.pkg_name)
    write_file(dockerfile_content, project_dir / "Dockerfile")

    # schema.proto
    schema_content = read_file(template_dir / "schema.proto")
    schema_content = schema_content.replace("PKG_NAME", args.pkg_name)
    write_file(schema_content, project_dir / "schema.proto")

    # files that are simply copied unmodified
    shutil.copy(template_dir / "requirements.txt", project_dir)
    shutil.copy(template_dir / "VERSION", project_dir)
    write_file("", pkg_dir / "__init__.py")
    shutil.copy("bin/create_project.py", project_dir / "bin")
    shutil.copy("bin/create_demo.py", project_dir / "bin")
    shutil.copytree(
        "resources/project_template",
        (project_dir / "resources" / "project_template")
    )
    shutil.copytree(
        "resources/demo_template",
        (project_dir / "resources" / "demo_template")
    )

    with open(project_dir / "project.json", "w") as f:
        f.write(json.dumps({"package": args.pkg_name}))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir", required=True)
    parser.add_argument("--pkg-name", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
