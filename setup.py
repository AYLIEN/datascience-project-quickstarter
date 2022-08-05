from setuptools import setup

setup(
    name="quickstarter",
    version=0.1,
    packages=["quickstarter"],
    entry_points={
        "console_scripts": [
            "quickstart=quickstarter.create_project:main",
        ]
    },
    include_package_data=True,
)
