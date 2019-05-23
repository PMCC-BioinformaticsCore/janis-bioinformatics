from abc import ABC
from typing import List, Dict, Any
from janis.utils import get_value_for_hints_and_ordered_resource_tuple

from janis import ToolOutput, ToolInput, Array, File, String, Int, Filename, InputSelector, CaptureType
from janis.unix.data_types.tsv import Tsv

from janis_bioinformatics.data_types import Vcf

from janis_bioinformatics.tools import BioinformaticsTool


CORES_TUPLE = [
    (CaptureType.key(), {
        CaptureType.CHROMOSOME: 2,
        CaptureType.EXOME: 2,
        CaptureType.THIRTYX: 2,
        CaptureType.NINETYX: 2,
        CaptureType.THREEHUNDREDX: 2
    })
]

MEM_TUPLE = [
    (CaptureType.key(), {
        CaptureType.CHROMOSOME: 8,
        CaptureType.EXOME: 8,
        CaptureType.THIRTYX: 8,
        CaptureType.NINETYX: 12,
        CaptureType.THREEHUNDREDX: 16
    })
]


class CombineVariantsBase(ABC, BioinformaticsTool):
    @staticmethod
    def tool() -> str:
        return "combinevariants"

    def friendly_name(self) -> str:
        return "Combine Variants"

    @staticmethod
    def base_command():
        return "combine_vcf.py"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val: return val
        return 2

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val: return val
        return 8

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("outputFilename", Filename(extension=".vcf", suffix=".combined"), prefix="-o"),

            ToolInput("regions", Filename(extension=".tsv"), prefix="--regions",
                      doc="Region file containing all the variants, used as samtools mpileup"),

            ToolInput("vcfs", Array(Vcf()), prefix="-i",
                      doc="input vcfs, the priority of the vcfs will be based on the order of the input"),
            ToolInput("type", String(), prefix="--type", doc="germline | somatic"),

            ToolInput("columns", Array(String(), optional=True), prefix="--columns",
                      doc="Columns to keep, seperated by space output vcf (unsorted)"),

            ToolInput("normal", String(optional=True), prefix="--normal",
                      doc="Sample id of germline vcf, or normal sample id of somatic vcf"),
            ToolInput("tumor", String(optional=True), prefix="--tumor", doc="tumor sample ID, required if inputs are somatic vcfs"),
            ToolInput("priority", Int(optional=True), prefix="--priority",
                      doc="The priority of the callers, must match with the callers in the source header")
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("vcf", Vcf(), InputSelector("outputFilename")),
            (ToolOutput("tsv", Tsv(), InputSelector("regions")))
        ]
