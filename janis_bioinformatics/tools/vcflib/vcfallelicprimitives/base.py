from abc import ABC

from janis_core import ToolInput, String, Boolean, ToolOutput, Stdout, Int
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfToolsToolBase


class VcfAllelicPrimitivesBase(VcfToolsToolBase, ABC):
    @staticmethod
    def tool():
        return "vcfallelicprimitives"

    def friendly_name(self):
        return "VcfLib: VcfAllelicPrimitives"

    @staticmethod
    def base_command():
        return "vcfallelicprimitives"

    def inputs(self):
        return [
            ToolInput("vcf", CompressedVcf, position=3),
            ToolInput(
                "useMnpsFlag",
                Boolean(optional=True),
                prefix="-m",
                default=False,
                doc="Retain MNPs as separate events (default: false)",
            ),
            ToolInput(
                "tagParsed",
                String(optional=True),
                prefix="-t",
                doc="Tag records which are split apart of a complex allele with this flag",
            ),
            ToolInput(
                "keepInfoFlag",
                Boolean(optional=True),
                prefix="-k",
                doc="Maintain site and allele-level annotations when decomposing. Note that in many cases, such as multisample VCFs, these won't be valid post-decomposition.  For biallelic loci in single-sample VCFs, they should be usable with caution.",
            ),
            ToolInput(
                "keepGenoFlag",
                Boolean(optional=True),
                prefix="-g",
                doc="Maintain genotype-level annotations when decomposing.  Similar caution should be used for this as for --keep-info.",
            ),
            ToolInput(
                "maxLength",
                Int(optional=True),
                prefix="-L",
                doc="Do not manipulate records in which either the ALT or REF is longer than LEN (default: 200).",
            ),
        ]

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
            documentation="usage: vcfallelicprimitives [options] [file]\n\noptions:\n\t-m, --use-mnps\tRetain MNPs as separate events (default: false)\n\t-t, --tag-parsed FLAG\tTag records which are split apart of a complex allele with this flag",
        )
