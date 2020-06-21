import pathlib
from setuptools import setup, find_packages

# Thanks to https://realpython.com/pypi-publish-python-package/
# for the template

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="callmemaybe",
    version="1.0.1",
    description="A CLI tool to talk to you",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SamuelYvon/CallMeMaybe",
    author="Samuel Yvon",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cmm=callmemaybe.cmm:main",
        ]
    },
    packages=find_packages(exclude="tests")
)
