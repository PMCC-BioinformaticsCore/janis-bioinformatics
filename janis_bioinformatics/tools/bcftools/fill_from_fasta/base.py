from datetime import datetime
from abc import ABC
from typing import Dict, Any, List

from janis_core import (
    get_value_for_hints_and_ordered_resource_tuple,
    ToolInput,
    ToolOutput,
    String,
    InputSelector,
    Filename,
    ToolMetadata,
    CaptureType,
    ToolArgument,
    File,
)
from janis_core.tool.test_classes import TTestCase
from janis_core.types import UnionType
from janis_core.types.common_data_types import Boolean

from janis_bioinformatics.data_types import Vcf, CompressedVcf, Fasta
from janis_bioinformatics.tools import BioinformaticsTool
from janis_bioinformatics.tools.bcftools.bcftoolstoolbase import BcfToolsToolBase

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
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 16,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 16,
            CaptureType.THREEHUNDREDX: 16,
        },
    )
]


class BcfToolsFillFromFastaBase(BcfToolsToolBase, ABC):
    def tool(self) -> str:
        return "bcftoolsFillFromFasta"

    def friendly_name(self) -> str:
        return "BCFTools: fill-from-fasta"

    def base_command(self):
        return ["bcftools", "+fill-from-fasta"]

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

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "vcf",
                UnionType(Vcf, CompressedVcf),
                position=1,
                doc="Input vcf",
            ),
            ToolInput(
                "outputFilename",
                Filename(
                    InputSelector("vcf", remove_file_extension=True),
                    suffix=".fill",
                    extension=".vcf",
                ),
                position=6,
                doc="Output vcf",
            ),
            ToolInput(
                "column",
                String(),
                prefix="--column",
                position=3,
                doc="REF or INFO tag, e.g. AA for ancestral allele",
            ),
            ToolInput("fasta", Fasta(), prefix="--fasta", position=3, doc="fasta file"),
            ToolInput(
                "header_lines",
                File(optional=True),
                prefix="--header-lines",
                position=3,
                doc="optional file containing header lines to append",
            ),
            ToolInput(
                "include",
                String(optional=True),
                prefix="--include",
                position=3,
                doc="annotate only records passing filter expression",
            ),
            ToolInput(
                "exclude",
                String(optional=True),
                prefix="--exclude",
                position=3,
                doc="annotate only records failing filter expression",
            ),
            ToolInput(
                "replace_non_ACGTN",
                Boolean(optional=True),
                prefix="--replace-non-ACGTN",
                position=3,
                doc="replace non-ACGTN characters with N",
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out",
                Vcf(),
                glob=InputSelector("outputFilename"),
            )
        ]

    def arguments(self):
        return [
            ToolArgument(
                "--",
                position=2,
                shell_quote=False,
            ),
            ToolArgument(
                ">",
                position=5,
                shell_quote=False,
            ),
        ]

    def doc(self):
        return """About:   Fill INFO or REF field based on values in a fasta file.
         The fasta file must be indexed with samtools faidx.
Usage:   bcftools +fill-from-fasta [General Options] -- [Plugin Options]
        Bash command:
         bcftools +fill-from-fasta $input -- -c REF -f $ref > $output"""

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 5, 19),
            dateUpdated=datetime(2021, 5, 19),
            documentation="",
        )
