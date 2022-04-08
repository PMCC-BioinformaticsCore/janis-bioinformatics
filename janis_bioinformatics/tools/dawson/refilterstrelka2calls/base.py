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
    Array,
    Boolean,
    String,
    Int,
    WildcardSelector,
)

from janis_unix import TextFile

from janis_bioinformatics.data_types import VcfTabix, Vcf

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 5,
            CaptureType.CHROMOSOME: 5,
            CaptureType.EXOME: 20,
            CaptureType.THIRTYX: 20,
            CaptureType.NINETYX: 40,
            CaptureType.THREEHUNDREDX: 40,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 24,
            CaptureType.CHROMOSOME: 24,
            CaptureType.EXOME: 48,
            CaptureType.THIRTYX: 48,
            CaptureType.NINETYX: 48,
            CaptureType.THREEHUNDREDX: 48,
        },
    )
]


class RefilterStrelka2CallsBase(BioinformaticsTool, ABC):
    def tool(self) -> str:
        return "refilterStrelka2Calls"

    def friendly_name(self) -> str:
        return "Refilter Strelka2 Variant Calls"

    def tool_provider(self):
        return "Dawson Labs"

    def base_command(self):
        return "filterStrelkaCalls.R"

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
                tag="inputFiles",
                input_type=Array(VcfTabix),
                prefix="-i",
                separator=",",
                doc="comma seperated list of vcfs",
            ),
            ToolInput(
                tag="MQ",
                input_type=Int(),
                default=15,
                prefix="--mq",
                doc="minimum mapping quality for a variant to be accepted (default: 15)",
            ),
            ToolInput(
                tag="DP",
                input_type=Int(),
                default=10,
                prefix="--dp",
                doc="minimum depth of coverage for a variant to be accepted (default: 10)",
            ),
            ToolInput(
                tag="EVS",
                input_type=Int(),
                default=20,
                prefix="--evs",
                doc="minimum phred scaled evidence for a variant to be accepted (default: 20)",
            ),
            ToolInput(
                tag="RPRS",
                input_type=Int(),
                default=-10,
                prefix="--rprs",
                doc="minimum phred scaled evidence for a variant to be accepted (default: 20)",
            ),
            ToolInput(
                tag="minAD",
                input_type=Int(),
                default=2,
                prefix="--minAD",
                doc="minimum allelic depth for a variant to be accepted (default: 2)",
            ),
            ToolInput(
                tag="threads",
                input_type=Int(),
                default=CpuSelector(),
                prefix="-t",
                doc="amount of threads to use for parallelization (default: 5)",
            ),
            ToolInput(
                tag="interval",
                input_type=String(optional=True),
                prefix="-L",
                doc="interval to call on (default: everything)",
            ),
            ToolInput(
                tag="normalName",
                input_type=String(optional=True),
                prefix="-n",
                doc="Name of the normal sample (default: infered from all sample names)",
            ),
            ToolInput(
                tag="sampleNames",
                input_type=Array(String, optional=True),
                prefix="--sampleNames",
                separator=",",
                doc="Name of the normal sample (default: infered from all sample names)",
            ),
            ToolInput(
                tag="outputFolder",
                input_type=String(),
                prefix="-o",
                default="./",
                doc="Name of the normal sample (default: infered from all sample names)",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Array(Vcf),
                glob=WildcardSelector("*.refiltered.vcf"),
                doc="To determine type",
            )
        ]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 20

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 48

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
            documentation="Usage: filterStrelkaCalls.R [options]\n",
        )
