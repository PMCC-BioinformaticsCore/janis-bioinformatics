from abc import ABC

from janis_core import ToolInput, String, Int, ToolOutput, Float, Stdout, ToolMetadata

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfLibToolBase


class VcfLengthBase(VcfLibToolBase, ABC):
    def tool(self):
        return "vcflength"

    def friendly_name(self):
        return "VcfLib: Vcf Length"

    def base_command(self):
        return "vcflength"

    def inputs(self):
        return [
            ToolInput(
                "vcf",
                CompressedVcf,
                position=1,
                doc="VCF to add length of variant record relative to the reference allele to.",
            )
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Stdout(Vcf),
                doc="VCF with length of the variant record added to each record",
            )
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2020, 6, 4),
            dateUpdated=date(2020, 6, 4),
            institution=None,
            doi=None,
            citation=None,
            keywords=["vcflib", "length"],
            documentationUrl="https://github.com/vcflib/vcflib",
            documentation="Adds the length of the variant record (in [-/+]) relative to the reference allele to each VCF record.",
        )
