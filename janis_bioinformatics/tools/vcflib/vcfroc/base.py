from abc import ABC

from janis_core import ToolInput, Int, ToolOutput, Stdout
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import FastaWithDict, CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfToolsToolBase


class VcfRocBase(VcfToolsToolBase, ABC):
    @staticmethod
    def tool():
        return "vcfroc"

    def friendly_name(self):
        return "VcfLib: Vcf ROC generator"

    @staticmethod
    def base_command():
        return "vcfroc"

    def inputs(self):
        return [
            ToolInput("vcf", CompressedVcf, position=3),
            ToolInput(
                "truth",
                CompressedVcf(),
                prefix="-t",
                doc="use this VCF as ground truth for ROC generation",
            ),
            ToolInput(
                "windowSize",
                Int(optional=True),
                prefix="-w",
                default=30,
                doc="compare records up to this many bp away (default 30)",
            ),
            ToolInput(
                "reference", FastaWithDict, prefix="-r", doc="FASTA reference file"
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
            documentation="usage: vcfroc [options] [<vcf file>]\n\noptions:\n\t-t, --truth-vcf FILE\tuse this VCF as ground truth for ROC generation\n\t-w, --window-size N       compare records up to this many bp away (default 30)\n\t-r, --reference FILE\tFASTA reference file",
        )
