from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    String,
    Float,
    InputSelector,
    CaptureType,
    ToolArgument,
    MemorySelector,
)
from janis_core import get_value_for_hints_and_ordered_resource_tuple

from janis_bioinformatics.data_types import (
    BamBai,
    Bed,
    FastaWithDict,
    VcfIdx,
    Vcf,
    VcfTabix,
)
from ..gatk4toolbase import Gatk4ToolBase
from janis_core import ToolMetadata

CORES_TUPLE = [
    # (CaptureType.key(), {
    #     CaptureType.CHROMOSOME: 2,
    #     CaptureType.EXOME: 2,
    #     CaptureType.THIRTYX: 2,
    #     CaptureType.NINETYX: 2,
    #     CaptureType.THREEHUNDREDX: 2
    # })
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 32,
            CaptureType.CHROMOSOME: 64,
            CaptureType.EXOME: 64,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4Mutect2Base(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "Mutect2"

    @staticmethod
    def tool():
        return "gatkmutect2"

    def friendly_name(self):
        return "GATK4: MuTect2"

    @staticmethod
    def tumor_normal_inputs():
        return [
            ToolInput(
                "tumor",
                BamBai(),
                position=6,
                prefix="-I",
                doc="BAM/SAM/CRAM file containing reads",
            ),
            ToolInput(
                "tumorName",
                String(),
                position=6,
                prefix="-tumor",
                doc="BAM sample name of tumor. May be URL-encoded as output by GetSampleName with -encode.",
            ),
            ToolInput(
                "normal",
                BamBai(),
                position=5,
                prefix="-I",
                doc="BAM/SAM/CRAM file containing reads",
            ),
            ToolInput(
                "normalName",
                String(),
                position=6,
                prefix="-normal",
                doc="BAM sample name of normal. May be URL-encoded as output by GetSampleName with -encode.",
            ),
        ]

    def inputs(self):
        return [
            *super(Gatk4Mutect2Base, self).inputs(),
            *Gatk4Mutect2Base.additional_args,
            *Gatk4Mutect2Base.tumor_normal_inputs(),
            ToolInput(
                "intervals",
                Bed(optional=True),
                position=7,
                prefix="-L",
                doc="One or more genomic intervals over which to operate",
            ),
            ToolInput(
                "reference",
                FastaWithDict(),
                position=8,
                prefix="-R",
                doc="Reference sequence file",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf.gz"),
                position=20,
                prefix="-O",
            ),
            ToolInput(
                "germlineResource",
                VcfIdx(optional=True),
                position=10,
                prefix="--germline-resource",
            ),
            ToolInput(
                "afOfAllelesNotInResource",
                Float(optional=True),
                position=11,
                prefix="--af-of-alleles-not-in-resource",
                doc="Population allele fraction assigned to alleles not found in germline resource. "
                "Please see docs/mutect/mutect2.pdf fora derivation of the default value.",
            ),
            ToolInput(
                "panelOfNormals",
                VcfIdx(optional=True),
                position=10,
                prefix="--panel-of-normals",
                doc="A panel of normals can be a useful (optional) input to help filter out "
                "commonly seen sequencing noise that may appear as low allele-fraction somatic variants.",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                VcfTabix(),
                glob=InputSelector("outputFilename"),
                doc="To determine type",
            )
        ]

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

    additional_args = []

    def metadata(self):
        from datetime import date

        return ToolMetadata(
            creator="Michael Franklin",
            maintainer="Michael Franklin",
            maintainerEmail="michael.franklin@petermac.org",
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 1, 24),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "mutect2"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.10.0/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php",
            documentation="""
Call somatic short variants via local assembly of haplotypes. Short variants include single nucleotide (SNV) 
and insertion and deletion (indel) variants. The caller combines the DREAM challenge-winning somatic 
genotyping engine of the original MuTect (Cibulskis et al., 2013) with the assembly-based machinery of HaplotypeCaller.

This tool is featured in the Somatic Short Mutation calling Best Practice Workflow. See Tutorial#11136 
for a step-by-step description of the workflow and Article#11127 for an overview of what traditional 
somatic calling entails. For the latest pipeline scripts, see the Mutect2 WDL scripts directory. 
Although we present the tool for somatic calling, it may apply to other contexts, 
such as mitochondrial variant calling.
""".strip(),
        )

    def arguments(self):
        return [
            # ToolArgument(MemorySelector(prefix="-Xmx", suffix="G", default=8), prefix="--java-options", position=0)
        ]
