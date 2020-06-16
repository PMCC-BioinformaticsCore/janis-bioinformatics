from abc import ABC
from typing import Any, Dict

from janis_core import (
    ToolInput,
    ToolArgument,
    WildcardSelector,
    Int,
    Float,
    Boolean,
    String,
    ToolOutput,
    Filename,
    InputSelector,
    CaptureType,
    CpuSelector,
    Stdout,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
)

from janis_bioinformatics.data_types import Sam, FastaWithDict, FastqGzPair, Bam, File
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

BAMSORMADUP_MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 8,
            CaptureType.EXOME: 12,
            CaptureType.CHROMOSOME: 12,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 20,
            CaptureType.THREEHUNDREDX: 24,
        },
    )
]

BAMSORMADUP_CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 16,
            CaptureType.EXOME: 20,
            CaptureType.CHROMOSOME: 24,
            CaptureType.THIRTYX: 30,
            CaptureType.NINETYX: 32,
            CaptureType.THREEHUNDREDX: 32,
        },
    )
]


class BamSorMaDupBase(BioinformaticsTool, ABC):
    def tool(self):
        return "bamsormadup"

    def friendly_name(self):
        return "BamSorMaDup"

    def tool_provider(self):
        return "BioBamBam"

    def base_command(self):
        return ["bamsormadup"]

    def inputs(self):
        return [
            ToolInput("alignedReads", Bam(), position=200),
            ToolInput("outputFilename", Filename(extension=".bam")),
            *BamSorMaDupBase.additional_inputs,
        ]

    def arguments(self):
        return [
            ToolArgument(
                "metrics.txt",
                prefix="M=",
                separate_value_from_prefix=False,
                doc="file containing metrics from duplicate removal",
            ),
            ToolArgument(
                "bam",
                prefix="inputformat=",
                separate_value_from_prefix=False,
                doc="input data format",
            ),
            ToolArgument(
                "bam",
                prefix="outputFormat=",
                separate_value_from_prefix=False,
                doc="output data format",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Stdout(Bam())),
            ToolOutput("metrics", File(), glob=WildcardSelector("metrics.txt")),
        ]

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(
            hints, BAMSORMADUP_MEM_TUPLE
        )
        if val:
            return val
        return 16

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(
            hints, BAMSORMADUP_CORES_TUPLE
        )
        if val:
            return val
        return 4

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Matthias De Smet (@mattdsm)"],
            dateCreated=date(2020, 2, 26),
            dateUpdated=date(2020, 2, 26),
            institution="None",
            doi=None,
            keywords=["duplicates", "sort"],
            documentationUrl="https://gitlab.com/german.tischler/biobambam2",
            documentation="bamsormadup: parallel sorting and duplicate marking",
        )

    additional_inputs = [
        ToolInput(
            "level",
            Int(optional=True),
            prefix="level=",
            separate_value_from_prefix=False,
            default=0,
            doc="compression settings for output bam file (-1=zlib default,0=uncompressed,1=fast,9=best)",
        ),
        ToolInput(
            "tempLevel",
            Int(optional=True),
            prefix="templevel=",
            separate_value_from_prefix=False,
            default=0,
            doc="compression settings for temporary bam files (-1=zlib default,0=uncompressed,1=fast,9=best)",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            default=CpuSelector(),
            prefix="threads=",
            separate_value_from_prefix=False,
            doc="Number of threads. (default = 1)",
        ),
        ToolInput(
            "sortOrder",
            String(optional=True),
            prefix="SO=",
            separate_value_from_prefix=False,
            default="coordinate",
            doc="output sort order(coordinate by default)",
        ),
        ToolInput(
            "optMinPixelDif",
            Int(optional=True),
            prefix="optminpixeldif=",
            separate_value_from_prefix=False,
            default=2500,
            doc="pixel difference threshold for optical duplicates (patterned flowcell: 12000, unpatterned flowcell: 2500)",
        ),
    ]
