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
            'Please name your python package (i.e. "aylien_zs_classification"'
        )
    pkg_dir = project_dir / package_name
    template_dir = HERE.parent / "templates" / "project"

    if project_dir.exists():
        if input(f"Project directory '{project_dir}' already exists. Override? [yes/no] ") == "yes":
            shutil.rmtree(project_dir)

    project_dir.mkdir(parents=True)
    (project_dir / 'demos').mkdir()
    (project_dir / 'bin').mkdir()
    (project_dir / 'resources').mkdir()
    (project_dir / 'research').mkdir()
    pkg_dir.mkdir()

    # Readme
    readme_content = read_file(template_dir / 'README.md')
    readme_content = readme_content.replace('{{PROJECT_NAME}}', project_dir.name)
    write_file(readme_content, project_dir / 'README.md')

    # setup.py
    setup_py_content = read_file(template_dir / 'setup.py')
    setup_py_content = setup_py_content.replace('{{PKG_NAME}}', args.libname)
    write_file(setup_py_content, project_dir / 'setup.py')

    # Makefile
    makefile_content = read_file(template_dir / 'Makefile')    
    makefile_content = makefile_content.replace('{{PKG_NAME}}', args.libname)
    write_file(makefile_content, project_dir / 'Makefile')

    # Dockerfile
    dockerfile_content = read_file(template_dir / 'Dockerfile')
    dockerfile_content = dockerfile_content.replace('{{PKG_NAME}}', args.libname)
    write_file(dockerfile_content, project_dir / 'Dockerfile')

    # TODO: make protobuf schema optional

    # schema.proto
    # schema_content = read_file(template_dir / 'schema.proto')
    # schema_content = schema_content.replace('{{PKG_NAME}}', args.libname)
    # write_file(schema_content, project_dir / 'schema.proto')

    # files that are simply copied unmodified
    shutil.copy(template_dir / 'requirements.txt', project_dir)
    shutil.copy(template_dir / 'VERSION', project_dir)
    shutil.copy(template_dir / '.gitignore', project_dir)
    write_file('', pkg_dir / '__init__.py')

    with open(project_dir / 'project.json', 'w') as f:
        f.write(json.dumps({'package': args.libname}))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        required=True,
        help="path to project directory"
    )
    parser.add_argument(
        '--libname',
        required=True,
        help="name of Python library/package associated with the project"
    )
    return parser.parse_args()
