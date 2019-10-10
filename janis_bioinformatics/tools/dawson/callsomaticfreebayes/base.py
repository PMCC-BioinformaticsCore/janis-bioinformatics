from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    CpuSelector,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
    CaptureType,
)

from janis_unix import TextFile

from janis_bioinformatics.data_types import (
    VcfTabix,
    Vcf,
)

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

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
    def base_command():
        return "Rscript callSomaticFreeBayes.R"

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
            ToolInput(
                tag="input",
                input_type=VcfTabix,
                prefix="-i",
                doc="input vcf"
            ),
            ToolInput(
                tag="normalSampleName",
                input_type=String(optional=True),
                prefix="-n",
                doc="the normal sample name in the vcf (default: first sample in vcf)"
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(extension=".vcf"),
                prefix="-o",
                doc="output file name (default: STDOUT)"
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Vcf,
                glob=InputSelector("outputFilename"),
                doc="To determine type",
            ),

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
            creator="Sebastian Hollizeck",
            maintainer="Sebastian Hollizeck",
            maintainerEmail="sebastian.hollizeck@petermac.org",
            dateCreated=date(2019, 10, 19),
            dateUpdated=date(2019, 10, 19),
            institution="PMCC",
            doi=None,
            citation=None,
            keywords=["strelka2"],
            documentationUrl=None,
            documentation="Usage: callSomaticFreeBayes.R [options]\n",
        )
