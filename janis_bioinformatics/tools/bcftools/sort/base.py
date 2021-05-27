import os
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
from janis_core.tool.test_classes import TTestCase
from janis_core.types import UnionType

from janis_bioinformatics.data_types import Vcf, CompressedVcf
from janis_bioinformatics.tools import BioinformaticsTool
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
    def tool(self) -> str:
        return "bcftoolssort"

    def friendly_name(self) -> str:
        return "BCFTools: Sort"

    def base_command(self):
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
            ToolInput(
                "vcf",
                UnionType(Vcf, CompressedVcf),
                position=1,
                doc="The VCF file to sort",
            ),
            ToolInput(
                "outputFilename",
                Filename(suffix=".sorted", extension=".vcf.gz"),
                prefix="--output-file",
                doc="(-o) output file name [stdout]",
            ),
            ToolInput(
                "outputType",
                String(optional=True),
                prefix="--output-type",
                default="z",
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
        return [ToolOutput("out", CompressedVcf, glob=InputSelector("outputFilename"))]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
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

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "outputType": "z",
                    "vcf": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.generated.gathered.vcf.gz",
                    ),
                },
                output=CompressedVcf.basic_test(
                    "out",
                    11602,
                    221,
                    ["GATKCommandLine"],
                    "fcc35adbb0624abc91f6de2e9042f749",
                ),
            )
        ]
