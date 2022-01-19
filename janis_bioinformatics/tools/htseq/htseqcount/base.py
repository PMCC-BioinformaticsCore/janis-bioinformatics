from abc import ABC

from janis_core import (
    ToolInput,
    String,
    File,
    Filename,
    Array,
    Int,
    Float,
    ToolOutput,
    InputSelector,
)
from janis_bioinformatics.data_types import Bam
from janis_bioinformatics.tools.htseq.htseqtoolbase import HTSeqToolBase


class HTSeqCountBase(HTSeqToolBase, ABC):
    def tool(self):
        return "HTSeqCount"

    def friendly_name(self):
        return "HTSeq-Count"

    def base_command(self):
        return ["htseq-count"]

    def inputs(self):
        return [
            ToolInput("bams", Array(Bam), position=1),
            ToolInput("gff_file", File, position=2),
            ToolInput(
                "format",
                String(optional=True),
                prefix="--format=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "order",
                String(optional=True),
                prefix="--order=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "max_reads_in_buffer",
                Int(optional=True),
                prefix="--max-reads-in-buffer=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "stranded",
                String(optional=True),
                prefix="--stranded=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "minaqual",
                Float(optional=True),
                prefix="--a=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "type",
                String(optional=True),
                prefix="--type=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "id",
                String(optional=True),
                prefix="--idattr=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "additional_attr",
                String(optional=True),
                prefix="--additional-attr=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "mode",
                String(optional=True),
                prefix="--type=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "nonunique",
                String(optional=True),
                prefix="--nonunique=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "secondary_alignments",
                String(optional=True),
                prefix="--secondary-alignments=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "supplementary_alignments",
                String(optional=True),
                prefix="--supplementary-alignments=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "samout",
                String(optional=True),
                prefix="--samout=",
                separate_value_from_prefix=False,
                position=3,
            ),
            ToolInput(
                "outputFilename",
                Filename(suffix=".htseq-count", extension=".txt"),
                prefix=">",
                doc="",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("outputFilename"))]

    def bind_metadata(self):
        from datetime import date

        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.dateCreated = date(2022, 1, 17)
        self.metadata.dateUpdated = date(2022, 1, 17)
        self.metadata.doi = (
            "https://htseq.readthedocs.io/en/release_0.11.1/overview.html"
        )
        self.metadata.citation = (
            "G Putri, S Anders, PT Pyl, JE Pimanda, F Zanini"
            "Analysing high-throughput sequencing data with HTSeq 2.0"
            "arXiv:2112.00939 (2021)"
        )
        self.metadata.documentationUrl = (
            "https://htseq.readthedocs.io/en/release_0.11.1/count.html#count"
        )
