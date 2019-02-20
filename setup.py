from setuptools import setup, find_packages

VERSION = "v0.0.4"
DESCRIPTION = "Bioinformatics tools for Janis; the Pipeline creation helper"

######## SHOULDN'T NEED EDITS BELOW THIS LINE ########

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="janis-pipelines.bioinformatics",
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/PMCC-BioinformaticsCore/janis-bioinformatics",
    author="Michael Franklin, Evan Thomas, Mohammad Bhuyan",
    author_email="michael.franklin@petermac.org",
    license="GNU",
    packages=["janis_bioinformatics"] + ["janis_bioinformatics." + p for p in sorted(find_packages('./janis_bioinformatics'))],
    install_requires=["janis-pipelines"],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ]
)
