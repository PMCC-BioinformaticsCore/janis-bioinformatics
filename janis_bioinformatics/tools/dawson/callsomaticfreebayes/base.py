from abc import ABC
from typing import Any, Dict

from janis_bioinformatics.data_types import Vcf, VcfTabix
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_core import (
    Array,
    Boolean,
    CaptureType,
    CpuSelector,
    Filename,
    Int,
    String,
    ToolInput,
    ToolMetadata,
    ToolOutput,
    get_value_for_hints_and_ordered_resource_tuple,
    InputSelector,
)
from janis_unix import TextFile


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
            CaptureType.TARGETED: 12,
            CaptureType.CHROMOSOME: 12,
            CaptureType.EXOME: 12,
            CaptureType.THIRTYX: 12,
            CaptureType.NINETYX: 12,
            CaptureType.THREEHUNDREDX: 12,
        },
    )
]


class CallSomaticFreeBayesBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool() -> str:
        return "callSomaticFreeBayes"

    def friendly_name(self) -> str:
        return "Call Somatic Variants from freebayes"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def base_command():
        return "callSomaticFreeBayes.R"

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

    def inputs(self):
        return [
            ToolInput(tag="vcf", input_type=VcfTabix, prefix="-i", doc="input vcf"),
            ToolInput(
                tag="normalSampleName",
                input_type=String(optional=True),
                prefix="-n",
                doc="the normal sample name in the vcf (default: first sample in vcf)",
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(extension=".vcf"),
                prefix="-o",
                doc="output file name (default: STDOUT)",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Vcf,
                glob=InputSelector("outputFilename"),
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
            dateCreated=date(2019, 10, 19),
            dateUpdated=date(2019, 10, 25),
            institution="PMCC",
            doi=None,
            citation=None,
            keywords=["strelka2"],
            documentationUrl=None,
            documentation="Usage: callSomaticFreeBayes.R [options]\n",
        )
