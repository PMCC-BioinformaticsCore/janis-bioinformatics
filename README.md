# Janis - Bioinformatics

[![Documentation Status](https://readthedocs.org/projects/janis/badge/?version=latest)](https://janis.readthedocs.io/en/latest/tools/bioinformatics/index.html)
[![Build Status](https://travis-ci.org/PMCC-BioinformaticsCore/janis-bioinformatics.svg?branch=master)](https://travis-ci.org/PMCC-BioinformaticsCore/janis-bioinformatics)
[![PyPI version](https://badge.fury.io/py/janis-pipelines.bioinformatics.svg)](https://badge.fury.io/py/janis-pipelines.bioinformatics)

This repository contains tools and data types for [Janis](https://github.com/PMCC-BioinformaticsCore/janis) 
directly related to the bioinformatics field.

Refer to the [documentation](https://janis.readthedocs.io/en/latest/tools/bioinformatics/index.html).


## Data types

The data types are a way of encapsulating information about the file (including secondary files), and it allows clarity
when connecting inputs and steps together (as you know a BAM file should be connected to BAM input).


## Documentation

Documentation is generated on [Janis](https://github.com/PMCC-BioinformaticsCore/janis). 
To generate new documentation you will need to: 
1. Commit your changes here,
2. Update the submodule pointer on Janis,
3. Checkout Janis (recursively),
4. Run the regenerate script `janis/docs/regeneratedocumentation.py`,
5. Commit these changes and the documentation will autobuild on ReadTheDocs.