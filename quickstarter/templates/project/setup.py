from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("VERSION") as f:
    version = f.read().strip()

setup(
    name="{{PKG_NAME}}",
    version=version,
    packages=["{{PKG_NAME}}"],
    install_requires=requirements
)
