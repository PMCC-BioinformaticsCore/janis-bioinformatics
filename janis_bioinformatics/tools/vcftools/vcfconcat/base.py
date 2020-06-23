from abc import ABC

from janis_core import (
    ToolInput,
    Int,
    Boolean,
    ToolOutput,
    Array,
    Stdout,
)
from janis_core import ToolMetadata
from janis_bioinformatics.data_types import Vcf, VcfTabix
from janis_bioinformatics.tools.vcftools.vcftoolstoolbase import VcfToolsToolBase


class VcfToolsVcfConcatBase(VcfToolsToolBase, ABC):
    def tool(self):
        return "VcfToolsVcfConcat"

    @classmethod
    def vcftools_command(cls):
        return "vcf-concat"

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput("vcfTabix", Array(VcfTabix), position=10),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf))]

    def friendly_name(self):
        return "VcfTools: VcfConcat"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 5, 21),
            dateUpdated=date(2020, 5, 21),
            institution="VCFtools",
            doi=None,
            citation=None,
            keywords=["vcftools", "vcf-concat"],
            documentationUrl="http://vcftools.sourceforge.net/perl_module.html#vcf-concat",
            documentation="""Concatenates VCF files (for example split by chromosome). Note that the input and output VCFs will have the same number of columns, the script does not merge VCFs by position (see also vcf-merge).

In the basic mode it does not do anything fancy except for a sanity check that all files have the same columns. When run with the -s option, it will perform a partial merge sort, looking at limited number of open files simultaneously.""".strip(),
        )

    additional_inputs = [
        ToolInput(
            "checkColumns",
            Boolean(optional=True),
            prefix="-c",
            doc="Do not concatenate, only check if the columns agree.",
        ),
        # ToolInput(
        #     "files",
        #     File(optional=True),
        #     prefix="--files",
        #     doc="Read the list of files from a file.",
        # ),
        ToolInput(
            "padMissing",
            Boolean(optional=True),
            prefix="-p",
            doc="Write '.' in place of missing columns. Useful for joining chrY with the rest.",
        ),
        ToolInput(
            "mergeSort",
            Int(optional=True),
            prefix="--merge-sort",
            doc="Allow small overlaps in N consecutive files.",
        ),
    ]
