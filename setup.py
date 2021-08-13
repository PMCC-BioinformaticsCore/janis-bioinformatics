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
    # Note: pip is not smart enough to include subdirectories (** also does not work)
    package_data={"": ["*/test_data/*", "*/test_data/*/*", "*/test_data/*/*/*"]},
    include_package_data=True,
    entry_points={
        "janis.extension": ["bioinformatics=janis_bioinformatics"],
        "janis.tools": ["bioinformatics=janis_bioinformatics.tools"],
        "janis.types": ["bioinformatics=janis_bioinformatics.data_types"],
        "janis.datatype_transformations": [
            "bioinformatics=janis_bioinformatics.transformations:transformations"
        ],
    },
    install_requires=["janis-pipelines.core >= 0.11.0"],
    extras_require={
        "tests": [
            "nose",
            "parameterized",
            "janis-pipelines.unix >= 0.11.0",
            "janis-pipelines.runner >= 0.11.0",
        ],
        "ci": ["setuptools", "wheel", "twine",],
    },
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
