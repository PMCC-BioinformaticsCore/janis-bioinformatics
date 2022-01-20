from abc import ABC
from typing import Dict, Any

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
    get_value_for_hints_and_ordered_resource_tuple,
    CaptureType,
)
from janis_bioinformatics.data_types import Bam
from janis_bioinformatics.tools.htseq.htseqtoolbase import HTSeqToolBase

CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 1,
            CaptureType.EXOME: 1,
            CaptureType.THIRTYX: 1,
            CaptureType.NINETYX: 1,
            CaptureType.THREEHUNDREDX: 1,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 16,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class HTSeqCountBase(HTSeqToolBase, ABC):
    def tool(self):
        return "HTSeqCount"

    def friendly_name(self):
        return "HTSeq-Count"

    def base_command(self):
        return ["htseq-count"]

    def inputs(self):
        return [
            ToolInput("bams", Array(Bam), position=3),
            ToolInput("gff_file", File, position=4),
            ToolInput(
                "outputFilename",
                Filename(suffix=".htseq-count", extension=".txt"),
                prefix=">",
                doc="",
                position=5,
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("outputFilename"))]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 1

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

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

    additional_args = [
        ToolInput(
            "format",
            String(optional=True),
            prefix="--format=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "order",
            String(optional=True),
            prefix="--order=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "max_reads_in_buffer",
            Int(optional=True),
            prefix="--max-reads-in-buffer=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "stranded",
            String(optional=True),
            prefix="--stranded=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "minaqual",
            Int(optional=True),
            prefix="-a",
            position=1,
        ),
        ToolInput(
            "type",
            String(optional=True),
            prefix="--type=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "id",
            String(optional=True),
            prefix="--idattr=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "additional_attr",
            String(optional=True),
            prefix="--additional-attr=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "mode",
            String(optional=True),
            prefix="--mode=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "nonunique",
            String(optional=True),
            prefix="--nonunique=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "secondary_alignments",
            String(optional=True),
            prefix="--secondary-alignments=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "supplementary_alignments",
            String(optional=True),
            prefix="--supplementary-alignments=",
            separate_value_from_prefix=False,
            position=1,
        ),
        ToolInput(
            "samout",
            String(optional=True),
            prefix="--samout=",
            separate_value_from_prefix=False,
            position=1,
        ),
    ]
