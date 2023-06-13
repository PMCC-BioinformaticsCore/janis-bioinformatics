# Janis - Bioinformatics Toolbox

[![Documentation Status](https://readthedocs.org/projects/janis/badge/?version=latest)](https://janis.readthedocs.io/en/latest/tools/bioinformatics/index.html)
[![Build Status](https://travis-ci.org/PMCC-BioinformaticsCore/janis-bioinformatics.svg?branch=master)](https://travis-ci.org/PMCC-BioinformaticsCore/janis-bioinformatics)
[![PyPI version](https://badge.fury.io/py/janis-pipelines.bioinformatics.svg)](https://badge.fury.io/py/janis-pipelines.bioinformatics)

This repository is the bioinformatics toolbox for [Janis](https://github.com/PMCC-BioinformaticsCore/janis). 
It contains tools and data types directly related to the bioinformatics field.

You can see a full list of tools in the [documentation](https://janis.readthedocs.io/en/latest/tools/bioinformatics/index.html).


## Data types

The data types are a way of encapsulating information about the file (including secondary files), and it allows clarity
when connecting inputs and steps together. Sometimes bioinformatics data types have associated files (like an indexed bam, or a fasta with various indexes); when you use these types, Janis will bundle your files together to be transported around.

### Indexed Bam

> Further information: [Secondary / Accessory files](https://janis.readthedocs.io/en/latest/references/secondaryfiles.html)

Janis is opinionated about the `.bai` index for a Bam. Specifically we use the pattern:

- `mysample.bam`
- `mysample.bam.bai`

If your tool expects, or creates a file in the other common format (`.bam` and `.bai`), you can use the `secondaries_present_as` attribute on a:

- [`ToolInput`](https://janis.readthedocs.io/en/latest/references/commandtool.html#tool-input) to localise the index using a specific format (see: )
- [`ToolOutput`](https://janis.readthedocs.io/en/latest/references/commandtool.html#tool-output) to prepare your input for .


## Documentation

Documentation is generated on [Janis](https://github.com/PMCC-BioinformaticsCore/janis). 
To generate new documentation you will need to: 
1. Commit your changes here,
2. Update the submodule pointer on Janis,
3. Checkout Janis (recursively),
4. Run the regenerate script `janis/docs/regeneratedocumentation.py`,
5. Commit these changes and the documentation will autobuild on ReadTheDocs.