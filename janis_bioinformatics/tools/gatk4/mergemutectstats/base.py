from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    InputSelector,
    CaptureType,
    Array,
    ToolMetadata,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_unix.data_types import TextFile

from ..gatk4toolbase import Gatk4ToolBase

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
            CaptureType.TARGETED: 32,
            CaptureType.CHROMOSOME: 64,
            CaptureType.EXOME: 64,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4MergeMutectStatsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MergeMutectStats"

    @staticmethod
    def tool():
        return "GATK4MergeMutectStats"

    def friendly_name(self):
        return "GATK4: MergeMutectStats"

    def inputs(self):
        return [
            *super().inputs(),
            *Gatk4MergeMutectStatsBase.additional_args,
            ToolInput(
                "statsFiles",
                Array(TextFile),
                position=0,
                prefix="--stats",
                prefix_applies_to_all_elements=True,
                doc="Callability stats",
            ),
            ToolInput(
                "mergedStatsOut", Filename(extension=".txt"), position=1, prefix="-O"
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                TextFile,
                glob=InputSelector("mergedStatsOut"),
                doc="Merged callability stats",
            )
        ]

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

    additional_args = []

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            creator="Hollizeck Sebastian",
            maintainer="Hollizeck Sebastian",
            maintainerEmail="sebastian.hollizeck@petermac.org",
            dateCreated=date(2019, 9, 9),
            dateUpdated=date(2019, 9, 9),
            institution="Broad Institute",
            doi=None,
            citation="TBD",
            keywords=["gatk", "gatk4", "broad", "mutect2", "FilterMutectCalls"],
            documentationUrl="TBD",
            documentation="""
TBD
""".strip(),
        )

    def arguments(self):
        return [
            # ToolArgument(MemorySelector(prefix="-Xmx", suffix="G", default=8), prefix="--java-options", position=0)
        ]
