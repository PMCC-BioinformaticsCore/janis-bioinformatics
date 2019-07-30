from setuptools import setup, find_packages

######## SHOULDN'T NEED EDITS BELOW THIS LINE ########

vsn = {}
with open("./janis_bioinformatics/__meta__.py") as fp:
    exec(fp.read(), vsn)
version = vsn["__version__"]
description = vsn["description"]

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="janis-pipelines.bioinformatics",
    version=version,
    description=description,
    url="https://github.com/PMCC-BioinformaticsCore/janis-bioinformatics",
    author="Michael Franklin, Evan Thomas, Mohammad Bhuyan",
    author_email="michael.franklin@petermac.org",
    license="GNU",
    packages=["janis_bioinformatics"]
    + [
        "janis_bioinformatics." + p
        for p in sorted(find_packages("./janis_bioinformatics"))
    ],
    entry_points={"janis.extension": ["bioinformatics=janis_bioinformatics"]},
    install_requires=["janis-pipelines.core>=0.5.0"],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
