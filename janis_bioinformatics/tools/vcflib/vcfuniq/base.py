from abc import ABC

from janis_core import ToolInput, ToolOutput, Stdout
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfToolsToolBase


class VcfUniqBase(VcfToolsToolBase, ABC):
    def tool(self):
        return "vcfuniq"

    def friendly_name(self):
        return "VcfLib: VcfUniq"

    def base_command(self):
        return "vcfuniq"

    def inputs(self):
        return [ToolInput("vcf", CompressedVcf, position=3)]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf), doc="VCF output")]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Sebastian Hollizeck"],
            dateCreated=date(2019, 10, 18),
            dateUpdated=date(2019, 10, 18),
            institution=None,
            doi=None,
            citation=None,
            keywords=["freebayes", "bayesian", "variant calling"],
            documentationUrl="https://github.com/vcflib/vcflib",
            documentation="usage: vcffuniq [file]\nLike GNU uniq, but for VCF records. Remove records which have the same positon, ref, and alt as the previous record.",
        )
