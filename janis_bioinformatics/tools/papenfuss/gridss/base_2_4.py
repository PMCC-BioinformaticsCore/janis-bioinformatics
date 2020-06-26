from datetime import date
from typing import List, Dict, Any

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
    CpuSelector,
    CaptureType,
    get_value_for_hints_and_ordered_resource_tuple,
)

from janis_bioinformatics.data_types import Bam, BamBai, FastaWithDict, Bed, Vcf
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 8,
            CaptureType.CHROMOSOME: 8,
            CaptureType.EXOME: 8,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 16,
            CaptureType.THREEHUNDREDX: 16,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            # https://github.com/PapenfussLab/gridss#how-much-memory-should-i-give-gridss
            CaptureType.TARGETED: 31,
            CaptureType.CHROMOSOME: 31,
            CaptureType.EXOME: 31,
            CaptureType.THIRTYX: 31,
            CaptureType.NINETYX: 31,
            CaptureType.THREEHUNDREDX: 31,
        },
    )
]


class GridssBase_2_4(BioinformaticsTool):
    def tool(self) -> str:
        return "gridss"

    def tool_provider(self):
        return "Papenfuss Labs"

    def friendly_name(self) -> str:
        return "Gridss"

    def base_command(self):
        return "gridss.sh"

    def inputs(self):
        return [
            ToolInput("bams", Array(Bam()), position=10),
            ToolInput("reference", FastaWithDict(), position=1, prefix="--reference"),
            ToolInput(
                "outputFilename",
                Filename(suffix=".svs", extension=".vcf"),
                position=2,
                prefix="--output",
            ),
            ToolInput(
                "assemblyFilename",
                Filename(suffix=".assembled", extension=".bam"),
                position=3,
                prefix="--assembly",
            ),
            ToolInput(
                "threads", Int(optional=True), default=CpuSelector(), prefix="--threads"
            ),
            ToolInput(
                "blacklist", Bed(optional=True), position=4, prefix="--blacklist"
            ),
            ToolInput(
                "tmpdir", String(optional=True), default="./TMP", prefix="--workingdir"
            ),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Vcf(), glob=InputSelector("outputFilename")),
            ToolOutput("assembly", BamBai(), glob=InputSelector("assemblyFilename")),
        ]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 8

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 31

    def bind_metadata(self):

        self.metadata.contributors = ["Michael Franklin"]
        self.metadata.dateCreated = date(2019, 6, 19)
        self.metadata.dateUpdated = date(2019, 8, 20)
        self.metadata.documentationUrl = (
            "https://github.com/PapenfussLab/gridss/wiki/GRIDSS-Documentation"
        )
        self.metadata.doi = "10.1101/gr.222109.117"
        self.metadata.citation = (
            "Daniel L. Cameron, Jan Schröder, Jocelyn Sietsma Penington, Hongdo Do, "
            "Ramyar Molania, Alexander Dobrovic, Terence P. Speed and Anthony T. Papenfuss. "
            "GRIDSS: sensitive and specific genomic rearrangement detection using positional "
            "de Bruijn graph assembly. Genome Research, 2017 doi: 10.1101/gr.222109.117"
        )
        self.metadata.documentation = """\
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
