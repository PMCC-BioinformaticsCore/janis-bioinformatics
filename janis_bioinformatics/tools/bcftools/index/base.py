from abc import ABC

from janis_core import (
    ToolInput,
    Boolean,
    Filename,
    Int,
    ToolOutput,
    InputSelector,
    CpuSelector,
)

from janis_bioinformatics.data_types import Vcf, CompressedVcf, VcfTabix
from janis_bioinformatics.tools.bcftools.bcftoolstoolbase import BcfToolsToolBase


class BcfToolsIndexBase(BcfToolsToolBase, ABC):
    @staticmethod
    def tool():
        return "bcftoolsIndex"

    def friendly_name(self):
        return "BCFTools: Index"

    @staticmethod
    def base_command():
        return ["bcftools", "index"]

    def inputs(self):
        return [
            ToolInput("vcf", CompressedVcf, position=1, localise_file=True),
            ToolInput(
                tag="csi",
                input_type=Boolean(optional=True),
                prefix="--csi",
                doc="(-c) generate CSI-format index for VCF/BCF files [default]",
            ),
            ToolInput(
                tag="force",
                input_type=Boolean(optional=True),
                prefix="--force",
                doc="(-f) overwrite index if it already exists",
            ),
            ToolInput(
                tag="minShift",
                input_type=Int(optional=True),
                prefix="--min-shift",
                doc="(-m) set minimal interval size for CSI indices to 2^INT [14]",
            ),
            # ToolInput(
            #     tag="outputFilename",
            #     input_type=Filename(suffix=".indexed", extension=".vcf.gz"),
            #     prefix="--output-file",
            #     doc="(-o) optional output index file name",
            # ),
            ToolInput(
                tag="tbi",
                input_type=Boolean(optional=True),
                default=True,
                prefix="--tbi",
                doc="(-t) generate TBI-format index for VCF files",
            ),
            ToolInput(
                tag="threads",
                input_type=Int(optional=True),
                default=CpuSelector(),
                prefix="--threads",
                doc="sets the number of threads [0]",
            ),
            ToolInput(
                tag="nrecords",
                input_type=Boolean(optional=True),
                prefix="--nrecords",
                doc="(-n) print number of records based on existing index file",
            ),
            ToolInput(
                tag="stats",
                input_type=Boolean(optional=True),
                prefix="--stats",
                doc="(-s) print per contig stats based on existing index file",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", VcfTabix, glob=InputSelector("vcf"))]

    def bind_metadata(self):
        from datetime import date

        self.metadata.dateCreated = date(2019, 1, 24)
        self.metadata.doi = "http://www.ncbi.nlm.nih.gov/pubmed/19505943"
        self.metadata.citation = (
            "Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R, "
            "and 1000 Genome Project Data Processing Subgroup, The Sequence alignment/map (SAM) "
            "format and SAMtools, Bioinformatics (2009) 25(16) 2078-9"
        )
        self.metadata.documentationUrl = (
            "https://samtools.github.io/bcftools/bcftools.html#norm"
        )
        self.metadata.documentation = (
            "Index bgzip compressed VCF/BCF files for random access."
        )

    additional_args = []
