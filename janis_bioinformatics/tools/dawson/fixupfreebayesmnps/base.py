from abc import ABC
from typing import Any, Dict

from janis_bioinformatics.data_types import VcfGz
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_core import (
    Boolean,
    CaptureType,
    CpuSelector,
    Filename,
    ToolInput,
    ToolMetadata,
    ToolOutput,
    get_value_for_hints_and_ordered_resource_tuple,
    InputSelector,
)


CORES_TUPLE = [
    # (CaptureType.key(), {
    #     CaptureType.CHROMOSOME: 2,
    #     CaptureType.EXOME: 2,
    #     CaptureType.THIRTYX: 2,
    #     CaptureType.NINETYX: 2,
    #     CaptureType.THREEHUNDREDX: 2
    # })
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.CHROMOSOME: 4,
            CaptureType.EXOME: 8,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 16,
            CaptureType.THREEHUNDREDX: 32,
        },
    )
]


class FixUpFreeBayesMNPsBase(BioinformaticsTool, ABC):
    def tool(self) -> str:
        return "FixUpFreeBayesMNPs"

    def friendly_name(self) -> str:
        return "FixUp FreeBayes MNPs"

    def tool_provider(self):
        return "Dawson Labs"

    def base_command(self):
        return "fixupFreeBayesMNPs.R"

    def inputs(self):
        return [
            # it can read CompressedVcf as well, but yea unionTypes are not a thing yet
            ToolInput(tag="vcf", input_type=Vcf, prefix="-i", doc="input vcf"),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(extension=".vcf"),
                prefix="-o",
                doc="output file name (default: reassembled.vcf.bgz)",
            ),
            ToolInput(
                tag="uncompressed",
                input_type=Boolean(optional=T),
                prefix="-o",
                doc="output file name (default: reassembled.vcf.bgz)",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                VcfGz,
                glob=InputSelector("outputFilename") + ".bgz",
                doc="To determine type",
            )
        ]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 12

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Sebastian Hollizeck"],
            dateCreated=date(2021, 06, 03),
            dateUpdated=date(2021, 06, 03),
            institution="PMCC",
            doi=None,
            citation=None,
            keywords=["freebayes"],
            documentationUrl=None,
            documentation="Usage: fixupFreeBayesMNPs.R [options]\n",
        )
