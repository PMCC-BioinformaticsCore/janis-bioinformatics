import datetime
from abc import ABC
from typing import List, Dict, Any

from janis_core import (
    ToolOutput,
    ToolInput,
    Filename,
    InputSelector,
    CaptureType,
    get_value_for_hints_and_ordered_resource_tuple,
)

from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools import BioinformaticsTool

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
            CaptureType.CHROMOSOME: 8,
            CaptureType.EXOME: 32,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class ExtractStrelkaSomaticADDPBase(BioinformaticsTool, ABC):
    def tool(self) -> str:
        return "extractStrelkaSomaticADDP"

    def friendly_name(self) -> str:
        return "Extract Strelka Somatic AD DP"

    def base_command(self):
        return "extract_strelka_somatic_DP_AF.py"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("vcf", Vcf(), prefix="-i", doc="input vcf"),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf"),
                prefix="-o",
                doc="output vcf",
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("out", Vcf(), InputSelector("outputFilename")),
        ]

    def bind_metadata(self):
        self.metadata.creator = "Jiaan Yu"
        self.metadata.dateUpdated = datetime.datetime(2020, 7, 27)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """
 - Extract and calculate AD and AF value for each variant (both SNVs and INDELs)
Based on https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/README.md#somatic
        """
        self.metadata.documentationUrl = (
            "https://github.com/PMCC-BioinformaticsCore/scripts/tree/master/vcf_utils"
        )
