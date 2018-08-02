import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="supplypy",
    version="0.0.2",
    author="Jared Ervin",
    author_email="j.ervin@supply.com",
    description="A package of usefull tools for working with data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jhelicher@bitbucket.org/supplydev/supplypy.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
