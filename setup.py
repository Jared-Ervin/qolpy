import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qolpy",
    version="0.0.3",
    author="Jared Ervin",
    author_email="jared.ervin94@gmail.com",
    description="A package of quality of life (qol) functions for working with data in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jared-Ervin/qolpy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
