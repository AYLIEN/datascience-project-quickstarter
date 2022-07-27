import readline
import shutil
import sys
from pathlib import Path


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


def complete_path(text, state):
    """
    Temporary solution from stackoverflow for autocompleting paths when
    creating/selecting a project directory.
    """
    incomplete_path = Path(text)
    if incomplete_path.is_dir():
        completions = [p.as_posix() for p in incomplete_path.iterdir()]
    elif incomplete_path.exists():
        completions = [incomplete_path]
    else:
        exists_parts = Path(".")
        for part in incomplete_path.parts:
            test_next_part = exists_parts / part
            if test_next_part.exists():
                exists_parts = test_next_part

        completions = []
        for p in exists_parts.iterdir():
            p_str = p.as_posix()
            if p_str.startswith(text):
                completions.append(p_str)
    return completions[state]


# we want to treat '/' as part of a word, so override the delimiters
readline.set_completer_delims(" \t\n;")
readline.parse_and_bind("tab: complete")
readline.set_completer(complete_path)


def is_quickstarter_project(project_dir):
    return all([
        (project_dir / fname).exists() for fname in [
            "README.md",
            "Dockerfile",
            "project.json",
            "setup.py",
            "requirements.txt",
            "VERSION"
        ]
    ])


def override_old_project(project_dir):
    if input(
        "Project directory '{project_dir}' already exists. "
        "Override? [yes/no] "
    ) == "yes":
        if is_quickstarter_project(project_dir):
            shutil.rmtree(project_dir)
        else:
            print("Does not look like a previous project. Aborting.")
            sys.exit()
    else:
        print("Aborting.")
        sys.exit()
