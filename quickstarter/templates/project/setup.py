from setuptools import setup

with open("VERSION") as f:
    version = f.read().strip()

setup(
    name="{{PKG_NAME}}",
    version=version,
    packages=["{{PKG_NAME}}"],
)
