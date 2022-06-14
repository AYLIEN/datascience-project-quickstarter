from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("VERSION") as f:
    version = f.read().strip()

setup(
    name="aylien_zs_classifier",
    version=version,
    packages=["aylien_zs_classifier"],
    install_requires=requirements
)
