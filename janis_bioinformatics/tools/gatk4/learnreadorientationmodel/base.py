from abc import ABC
from typing import Dict, Any

from janis_core import (
    Array,
    CaptureType,
    Filename,
    InputSelector,
    Int,
    ToolInput,
    ToolMetadata,
    ToolOutput,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_unix import TarFileGz

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


class Gatk4LearnReadOrientationModelBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "LearnReadOrientationModel"

    def tool(self):
        return "Gatk4LearnReadOrientationModel"

    def friendly_name(self):
        return "GATK4: LearnReadOrientationModel"

    def inputs(self):
        return [
            *super(Gatk4LearnReadOrientationModelBase, self).inputs(),
            *Gatk4LearnReadOrientationModelBase.additional_args,
            ToolInput(
                "f1r2CountsFiles",
                Array(TarFileGz),
                position=0,
                prefix="-I",
                prefix_applies_to_all_elements=True,
                doc="Counts for the read orientation of fragments",
            ),
            ToolInput(
                "numEmIterations",
                Int(optional=True),
                position=1,
                prefix="--num-em-iterations",
                default=30,  # Sebastian thinks this is best
                doc="Amount of iterations for the em process before it bails",
            ),
            ToolInput(
                "modelFileOut", Filename(extension=".tar.gz"), position=3, prefix="-O"
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                TarFileGz(),
                glob=InputSelector("modelFileOut"),
                doc="Model file containing information about fragment orientations",
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
        return 32

    additional_args = []

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Hollizeck Sebastian"],
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
