import argparse
import shutil
from pathlib import Path


def read_file(path):
    with open(path) as f:
        content = f.read()
    return content


def write_file(content, path):
    with open(path, "w") as f:
        f.write(content)


def main(args):
    assert(args.project_dir.strip() != "")
    assert(args.pkg_name.strip() != "")

    template_dir = Path("resources/project_template")
    project_dir = Path(args.project_dir)
    pkg_dir = project_dir / args.pkg_name
    project_dir.mkdir()
    pkg_dir.mkdir()

    # Makefile
    makefile_content = read_file(template_dir / "Makefile")
    makefile_content = makefile_content.replace("PKG_NAME_", args.pkg_name)
    write_file(makefile_content, project_dir / "Makefile")

    # Readme
    readme_content = read_file(template_dir / "README.md")
    readme_content = readme_content.replace("PROJECT_NAME", project_dir.name)
    write_file(readme_content, project_dir / "README.md")

    # setup.py
    setup_py_content = read_file(template_dir / "setup.py")
    setup_py_content = setup_py_content.replace("PKG_NAME", args.pkg_name)
    write_file(setup_py_content, project_dir / "setup.py")

    # requirements.txt, VERSION, pkg/__init__.py
    shutil.copy(template_dir / "requirements.txt", project_dir)
    shutil.copy(template_dir / "VERSION", project_dir)
    write_file("", pkg_dir / "__init__.py")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-dir', required=True)
    parser.add_argument('--pkg-name', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
