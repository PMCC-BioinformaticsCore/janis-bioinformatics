import datetime
from abc import ABC
from typing import List, Dict, Any

from janis_core import (
    ToolOutput,
    ToolInput,
    Array,
    String,
    Int,
    Filename,
    InputSelector,
    CaptureType,
)
from janis_unix import Tsv
from janis import get_value_for_hints_and_ordered_resource_tuple

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


class CombineVariantsBase(BioinformaticsTool, ABC):
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
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf", suffix=".combined"),
                prefix="-o",
            ),
            ToolInput(
                "regions",
                Filename(extension=".tsv"),
                prefix="--regions",
                doc="Region file containing all the variants, used as samtools mpileup",
            ),
            ToolInput(
                "vcfs",
                Array(Vcf()),
                prefix="-i",
                prefix_applies_to_all_elements=True,
                doc="input vcfs, the priority of the vcfs will be based on the order of the input",
            ),
            ToolInput("type", String(), prefix="--type", doc="germline | somatic"),
            ToolInput(
                "columns",
                Array(String(), optional=True),
                prefix="--columns",
                prefix_applies_to_all_elements=True,
                doc="Columns to keep, seperated by space output vcf (unsorted)",
            ),
            ToolInput(
                "normal",
                String(optional=True),
                prefix="--normal",
                doc="Sample id of germline vcf, or normal sample id of somatic vcf",
            ),
            ToolInput(
                "tumor",
                String(optional=True),
                prefix="--tumor",
                doc="tumor sample ID, required if inputs are somatic vcfs",
            ),
            ToolInput(
                "priority",
                Int(optional=True),
                prefix="--priority",
                doc="The priority of the callers, must match with the callers in the source header",
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("vcf", Vcf(), InputSelector("outputFilename")),
            (ToolOutput("tsv", Tsv(), InputSelector("regions"))),
        ]

    def metadata(self):
        self._metadata.creator = "Jiaan Yu"
        self._metadata.dateUpdated = datetime.datetime(2019, 7, 4)
        self._metadata.maintainer = "Michael Franklin"
        self._metadata.documentation = """
usage: combine_vcf.py [-h] -i I --columns COLUMNS -o O --type
                      {germline,somatic} [--regions REGIONS] [--normal NORMAL]
                      [--tumor TUMOR] [--priority PRIORITY [PRIORITY ...]]

Extracts and combines the information from germline / somatic vcfs into one

required arguments:
  -i I                  input vcfs, the priority of the vcfs will be based on
                        the order of the input. This parameter can be
                        specified more than once
  --columns COLUMNS     Columns to keep. This parameter can be specified more
                        than once
  -o O                  output vcf (unsorted)
  --type {germline,somatic}
                        must be either germline or somatic
  --regions REGIONS     Region file containing all the variants, used as
                        samtools mpileup
  --normal NORMAL       Sample id of germline vcf, or normal sample id of
                        somatic vcf
  --tumor TUMOR         tumor sample ID, required if inputs are somatic vcfs
  --priority PRIORITY [PRIORITY ...]
                        The priority of the callers, must match with the
                        callers in the source header

optional arguments:
  -h, --help            show this help message and exit
"""
        self._metadata.documentationUrl = (
            "https://github.com/PMCC-BioinformaticsCore/scripts/tree/master/vcf_utils"
        )
