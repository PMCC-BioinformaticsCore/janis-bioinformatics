from abc import ABC
from typing import Dict, Any, List

from janis_bioinformatics.data_types import Vcf

from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import CaptureType, ToolInput, Filename, ToolOutput, InputSelector
from janis_core import get_value_for_hints_and_ordered_resource_tuple


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
            CaptureType.CHROMOSOME: 2,
            CaptureType.EXOME: 2,
            CaptureType.THIRTYX: 4,
            CaptureType.NINETYX: 4,
            CaptureType.THREEHUNDREDX: 4,
        },
    )
]


class TrimIUPACBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool() -> str:
        return "trimIUPAC"

    def friendly_name(self) -> str:
        return "Trim IUPAC Bases"

    @staticmethod
    def base_command():
        return "trimIUPAC.py"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 1

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 1

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "vcf", Vcf(), position=0, doc="The VCF to remove the IUPAC bases from"
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf", suffix=".trimmed"),
                position=2,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Vcf(), InputSelector("outputFilename"))]
