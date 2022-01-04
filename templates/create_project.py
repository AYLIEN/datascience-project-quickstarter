import argparse
import os
import shutil
import json
from pathlib import Path


path_to_file = Path(os.path.dirname(os.path.abspath(__file__)))


def read_file(path):
    with open(path) as f:
        content = f.read()
    return content


def write_file(content, path):
    with open(path, "w") as f:
        f.write(content)


def main(args):
    try:
        assert args.project_dir.strip() != ""
        project_dir = Path(args.project_dir)
    except AssertionError:
        project_dir = input(
            "Please name the project directory "
            "(cannot already exist):")

    try:
        assert args.pkg_name.strip() != ""
        package_name = args.pkg_name
    except AssertionError:
        package_name = input(
            'Please name your python package (i.e. "aylien_zs_classification"'
        )
    pkg_dir = project_dir / package_name
    template_dir = Path(path_to_file / 'project_template')
    if project_dir.exists():
        raise FileExistsError(f"Error: directory {project_dir} already exists.")

    project_dir.mkdir(parents=True)
    (project_dir / 'demos').mkdir()
    (project_dir / 'bin').mkdir()
    (project_dir / 'templates').mkdir()
    (project_dir / 'resources').mkdir()
    (project_dir / 'research').mkdir()
    pkg_dir.mkdir()

    # Readme
    readme_content = read_file(template_dir / 'README.md')
    readme_content = readme_content.replace('PROJECT_NAME', project_dir.name)
    write_file(readme_content, project_dir / 'README.md')

    # setup.py
    setup_py_content = read_file(template_dir / 'setup.py')
    setup_py_content = setup_py_content.replace('PKG_NAME', args.pkg_name)
    write_file(setup_py_content, project_dir / 'setup.py')

    # Makefile
    makefile_content = read_file(template_dir / 'Makefile')
    # using placeholder PKG_NAME_ instead of PKG_NAME because PKG_NAME
    # needs to remain a placeholder for "make init" command
    makefile_content = makefile_content.replace('PKG_NAME_', args.pkg_name)
    write_file(makefile_content, project_dir / 'Makefile')

    # Dockerfile
    dockerfile_content = read_file(template_dir / 'Dockerfile')
    dockerfile_content = dockerfile_content.replace('PKG_NAME', args.pkg_name)
    write_file(dockerfile_content, project_dir / 'Dockerfile')

    # schema.proto
    schema_content = read_file(template_dir / 'schema.proto')
    schema_content = schema_content.replace('PKG_NAME', args.pkg_name)
    write_file(schema_content, project_dir / 'schema.proto')

    # files that are simply copied unmodified
    shutil.copy(template_dir / 'requirements.txt', project_dir)
    shutil.copy(template_dir / 'VERSION', project_dir)
    write_file('', pkg_dir / '__init__.py')
    shutil.copy(path_to_file / 'create_project.py', project_dir / 'templates')
    shutil.copy(path_to_file / 'create_demo.py', project_dir / 'templates')
    shutil.copytree(
        'templates/project_template',
        (project_dir / 'templates' / 'project_template')
    )
    shutil.copytree(
        'templates/demo_template',
        (project_dir / 'templates' / 'demo_template')
    )

    with open(project_dir / 'project.json', 'w') as f:
        f.write(json.dumps({'package': args.pkg_name}))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-dir', required=True)
    parser.add_argument('--pkg-name', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
