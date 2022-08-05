from setuptools import setup

with open("VERSION") as f:
    version = f.read().strip()

setup(
    name="aylien_zs_classifier",
    version=version,
    packages=["aylien_zs_classifier"]
)
