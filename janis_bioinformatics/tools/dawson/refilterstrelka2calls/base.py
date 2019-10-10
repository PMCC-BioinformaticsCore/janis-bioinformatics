from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    CpuSelector,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
)

from janis_unix import TextFile

from janis_bioinformatics.data_types import (
    VcfTabix,
    Vcf,
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
            CaptureType.TARGETED: 12,
            CaptureType.CHROMOSOME: 12,
            CaptureType.EXOME: 12,
            CaptureType.THIRTYX: 12,
            CaptureType.NINETYX: 12,
            CaptureType.THREEHUNDREDX: 12,
        },
    )
]

class RefilterStrelka2CallsBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool() -> str:
        return "refilterStrelka2Calls"

    def friendly_name(self) -> str:
        return "Refilter Strelka2 Variant Calls"

    @staticmethod
    def base_command():
        return "Rscript filterStrelkaCalls.R"

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

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                tag="input",
                input_type=Array(VcfTabix),
                prefix="-i",
                separator=',',
                doc="comma seperated list of vcfs"
            ),
            ToolInput(
                tag="MQ",
                input_type=Int(),
                default=15,
                prefix="--mq",
                doc="minimum mapping quality for a variant to be accepted (default: 15)"
            ),
            ToolInput(
                tag="DP",
                input_type=Int(),
                default=10,
                prefix="--dp",
                doc="minimum depth of coverage for a variant to be accepted (default: 10)"
            ),
            ToolInput(
                tag="EVS",
                input_type=Int(),
                default=10,
                prefix="--evs",
                doc="minimum phred scaled evidence for a variant to be accepted (default: 20)"
            ),
            ToolInput(
                tag="RPRS",
                input_type=Int(),
                default=-10,
                prefix="--rprs",
                doc="minimum phred scaled evidence for a variant to be accepted (default: 20)"
            ),
            ToolInput(
                tag="threads",
                input_type=Int(),
                default=CpuSelector(),
                prefix="-t",
                doc="amount of threads to use for parallelization (default: 4)"
            ),
            ToolInput(
                tag="interval",
                input_type=String(optional=True),
                prefix="-L",
                doc="interval to call on (default: everything)"
            ),
            ToolInput(
                tag="normalName",
                input_type=String(optional=True),
                prefix="-n",
                doc="Name of the normal sample (defaul: infered from all sample names)"
            ),
            ToolInput(
                tag="outputFolder",
                input_type=String(),
                prefix="-o",
                default='./',
                doc="Name of the normal sample (defaul: infered from all sample names)"
            ),

        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Array(Vcf),
                glob=WildcardSelector("*.refiltered.vcf"),
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
            documentation="Usage: filterStrelkaCalls.R [options]\n",
        )
