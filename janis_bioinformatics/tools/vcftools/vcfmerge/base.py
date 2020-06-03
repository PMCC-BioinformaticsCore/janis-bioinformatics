from abc import ABC

from janis_core import ToolInput, Int, Boolean, ToolOutput, Array, Stdout, String, File
from janis_core import ToolMetadata
from janis_bioinformatics.data_types import Vcf, VcfTabix
from janis_bioinformatics.tools.vcftools.vcftoolstoolbase import VcfToolsToolBase


class VcfToolsVcfMergeBase(VcfToolsToolBase, ABC):
    def tool(self):
        return "VcfToolsVcfMerge"

    @classmethod
    def vcftools_command(cls):
        return "vcf-merge"

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput("vcfTabix", Array(VcfTabix), position=10),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf))]

    def friendly_name(self):
        return "VcfTools: VcfMerge"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 5, 21),
            dateUpdated=date(2020, 5, 21),
            institution="VCFtools",
            doi=None,
            citation=None,
            keywords=["vcftools", "vcf-merge"],
            documentationUrl="http://vcftools.sourceforge.net/perl_module.html#vcf-merge",
            documentation="""Merges two or more VCF files into one so that, for example, if two source files had one column each, on output will be printed a file with two columns. See also vcf-concat for concatenating VCFs split by chromosome.

vcf-merge A.vcf.gz B.vcf.gz C.vcf.gz | bgzip -c > out.vcf.gz

Note that this script is not intended for concatenating VCF files. For this, use vcf-concat instead.
Note: A fast htslib C version of this tool is now available (see bcftools merge).""".strip(),
        )

    additional_inputs = [
        ToolInput(
            "collapse",
            String(optional=True),
            prefix="-c",
            doc="treat as identical sites with differing alleles [any] <snps|indels|both|any|none> ",
        ),
        ToolInput(
            "removeDuplicates",
            Boolean(optional=True),
            prefix="--remove-duplicates",
            doc="If there should be two consecutive rows with the same chr:pos, print only the first one.",
        ),
        ToolInput(
            "vcfHeader",
            File(optional=True),
            prefix="--vcf-header",
            doc="Use the provided VCF header",
        ),
        ToolInput(
            "regionsList",
            Array(String, optional=True),
            separator=",",
            prefix="--regions",
            doc="Do only the given regions (comma-separated list).",
        ),
        ToolInput(
            "regionsFile",
            File(optional=True),
            prefix="--regions",
            doc="Do only the given regions (one region per line in a file).",
        ),
        ToolInput(
            "refForMissing",
            String(optional=True),
            prefix="--ref-for-missing",
            doc="Use the REF allele instead of the default missing genotype. Because it is not obvious what ploidy should be used, a user-defined string is used instead (e.g. 0/0).",
        ),
        ToolInput(
            "silent",
            Boolean(optional=True),
            prefix="--silent",
            doc="Try to be a bit more silent, no warnings about duplicate lines.",
        ),
        ToolInput(
            "trimALTs",
            Boolean(optional=True),
            prefix="--trim-ALTs",
            doc="If set, redundant ALTs will be removed",
        ),
    ]
