from abc import ABC
from datetime import datetime
from typing import Dict, Any

from janis_core import (
    ToolInput,
    ToolOutput,
    String,
    InputSelector,
    Filename,
    ToolMetadata,
    CaptureType,
)
from janis_core import get_value_for_hints_and_ordered_resource_tuple

from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.bcftools.bcftoolstoolbase import BcfToolsToolBase

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
            CaptureType.NINETYX: 16,
            CaptureType.THREEHUNDREDX: 16,
        },
    )
]


class BcfToolsSortBase(BcfToolsToolBase, ABC):
    @staticmethod
    def tool() -> str:
        return "bcftoolssort"

    def friendly_name(self) -> str:
        return "BCFTools: Sort"

    @staticmethod
    def base_command():
        return ["bcftools", "sort"]

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

    def inputs(self):
        return [
            ToolInput("vcf", Vcf(), position=1, doc="The VCF file to sort"),
            ToolInput(
                "outputFilename",
                Filename(suffix=".sorted", extension=".vcf"),
                prefix="--output-file",
                doc="(-o) output file name [stdout]",
            ),
            ToolInput(
                "outputType",
                String(optional=True),
                prefix="--output-type",
                doc="(-O) b: compressed BCF, u: uncompressed BCF, z: compressed VCF, v: uncompressed VCF [v]",
            ),
            ToolInput(
                "tempDir",
                String(optional=True),
                prefix="--temp-dir",
                doc="(-T) temporary files [/tmp/bcftools-sort.XXXXXX/]",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Vcf(), glob=InputSelector("outputFilename"))]

    def metadata(self):
        return ToolMetadata(
            creator=None,
            maintainer=None,
            maintainerEmail=None,
            dateCreated=datetime(2019, 5, 9),
            dateUpdated=datetime(2019, 7, 11),
            institution=None,
            doi=None,
            citation=None,
            keywords=["BCFTools", "sort"],
            documentationUrl="",
            documentation="""About:   Sort VCF/BCF file.
Usage:   bcftools sort [OPTIONS] <FILE.vcf>""",
        )
