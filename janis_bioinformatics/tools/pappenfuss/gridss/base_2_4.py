from datetime import date
from typing import List

from janis_core import (
    ToolOutput,
    ToolInput,
    Filename,
    File,
    String,
    Float,
    Int,
    Boolean,
    Array,
    InputSelector,
    CpuSelector)

from janis_bioinformatics.data_types import Bam, FastaWithDict, Bed, Vcf
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class GridssBase_2_4(BioinformaticsTool):
    @staticmethod
    def tool() -> str:
        return "gridss"

    @staticmethod
    def tool_provider():
        return "Papenfuss Labs"

    def friendly_name(self) -> str:
        return "Gridss"

    @staticmethod
    def base_command():
        return "gridss.sh"

    def inputs(self):
        return [
            ToolInput("bams", Array(Bam()), position=1),
            ToolInput("reference", FastaWithDict(), prefix="--reference"),
            ToolInput("outputFilename", Filename(extension=".vcf"), prefix="--output"),
            ToolInput("assemblyFilename", Filename(extension=".bam"), prefix="--assembly"),
            ToolInput("threads", Int(optional=True), default=CpuSelector(), prefix="--threads"),
            ToolInput("blacklist", Bed(optional=True), prefix="--blacklist"),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Vcf(), glob=InputSelector("outputFilename")),
            ToolOutput("assembly", Bam(), glob=InputSelector("assemblyFilename"))
        ]

    def metadata(self):

        self._metadata.maintainer = "Michael Franklin"
        self._metadata.dateCreated = date(2019, 6, 19)
        self._metadata.dateUpdated = date(2019, 7, 24)
        self._metadata.documentationUrl = (
            "https://github.com/PapenfussLab/gridss/wiki/GRIDSS-Documentation"
        )
        self._metadata.doi = "10.1101/gr.222109.117"
        self._metadata.citation = "Daniel L. Cameron, Jan Schröder, Jocelyn Sietsma Penington, Hongdo Do, " \
                                  "Ramyar Molania, Alexander Dobrovic, Terence P. Speed and Anthony T. Papenfuss. " \
                                  "GRIDSS: sensitive and specific genomic rearrangement detection using positional " \
                                  "de Bruijn graph assembly. Genome Research, 2017 doi: 10.1101/gr.222109.117"
        self._metadata.documentation = """\
GRIDSS: the Genomic Rearrangement IDentification Software Suite

GRIDSS is a module software suite containing tools useful for the detection of genomic rearrangements. 
GRIDSS includes a genome-wide break-end assembler, as well as a structural variation caller for Illumina 
sequencing data. GRIDSS calls variants based on alignment-guided positional de Bruijn graph genome-wide 
break-end assembly, split read, and read pair evidence.

GRIDSS makes extensive use of the standard tags defined by SAM specifications. Due to the modular design, 
any step (such as split read identification) can be replaced by another implementation that also outputs 
using the standard tags. It is hoped that GRIDSS can serve as an exemplar modular structural variant 
pipeline designed for interoperability with other tools.

If you have any trouble running GRIDSS, please raise an issue using the Issues tab above. Based on feedback 
from users, a user guide will be produced outlining common workflows, pitfalls, and use cases.
"""
