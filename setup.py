from setuptools import setup

with open("VERSION") as f:
    version = f.read().strip()

setup(
    name="datascience-quickstarter",
    version=version,
    description="A tool for quick-starting new datascience projects, build by AYLIEN Labs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    packages=["quickstarter"],
    data_files=["LICENSE", "VERSION", "README.md"],
    entry_points={
        "console_scripts": [
            "quickstart=quickstarter.create_project:main",
        ]
    },
    include_package_data=True,
)
