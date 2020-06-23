from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    InputSelector,
    CaptureType,
    Array,
    ToolMetadata,
    String,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_unix import TextFile

from janis_bioinformatics.data_types import BamBai, VcfIdx, Bed, VcfTabix
from ..gatk4toolbase import Gatk4ToolBase

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


class Gatk4GetPileUpSummariesBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "GetPileupSummaries"

    def tool(self):
        return "Gatk4GetPileupSummaries"

    def friendly_name(self):
        return "GATK4: GetPileupSummaries"

    def inputs(self):
        return [
            *super().inputs(),
            *Gatk4GetPileUpSummariesBase.additional_args,
            ToolInput(
                "bam",
                Array(BamBai()),
                prefix="-I",
                prefix_applies_to_all_elements=True,
                doc="The SAM/BAM/CRAM file containing reads.",
                position=0,
            ),
            ToolInput(
                "sites",
                VcfTabix(),
                prefix="-V",
                doc="sites of common biallelic variants",
            ),
            ToolInput(
                "intervals",
                Bed(optional=True),
                prefix="--intervals",
                doc="-L (BASE) One or more genomic intervals over which to operate",
            ),
            ToolInput(
                "pileupTableOut", Filename(extension=".txt"), position=1, prefix="-O"
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                TextFile,
                glob=InputSelector("pileupTableOut"),
                doc="Table containing the pileup info",
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
        return 64

    additional_args = []

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Hollizeck Sebastian"],
            dateCreated=date(2019, 9, 9),
            dateUpdated=date(2019, 9, 9),
            institution="Broad Institute",
            doi=None,
            citation="TBD",
            keywords=["gatk", "gatk4", "broad", "mutect2", "FilterMutectCalls"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.0.0/org_broadinstitute_hellbender_tools_walkers_contamination_GetPileupSummaries.php",
            documentation="""
Summarizes counts of reads that support reference, alternate and other alleles for given sites. Results can be used with CalculateContamination.
The tool requires a common germline variant sites VCF, e.g. the gnomAD resource, with population allele frequencies (AF) in the INFO field. This resource must contain only biallelic SNPs and can be an eight-column sites-only VCF. The tool ignores the filter status of the sites. See the GATK Resource Bundle for an example human file.
""".strip(),
        )
