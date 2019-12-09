from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    ToolOutput,
    File,
    InputSelector,
    CaptureType,
    Filename,
    ToolMetadata,
    get_value_for_hints_and_ordered_resource_tuple,
)

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


class Gatk4CalculateContaminationBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CalculateContamination"

    def tool(self):
        return "GATK4CalculateContamination"

    def friendly_name(self):
        return "GATK4: CalculateContamination"

    def inputs(self):
        return [
            *super(Gatk4CalculateContaminationBase, self).inputs(),
            *Gatk4CalculateContaminationBase.additional_args,
            ToolInput(
                "pileupTable",
                File(),
                prefix="-I",
                doc="pileup table from summarize pileup",
            ),
            ToolInput(
                "segmentationFileOut",
                Filename(),
                prefix="--tumor-segmentation",
                doc="Reference sequence file",
            ),
            ToolInput("contaminationFileOut", Filename(), position=2, prefix="-O"),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "contOut",
                File(),
                glob=InputSelector("contaminationFileOut"),
                doc="contamination Table",
            ),
            ToolOutput(
                "segOut",
                File(),
                glob=InputSelector("segmentationFileOut"),
                doc="segmentation based on baf",
            ),
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

    additional_args = [
        ToolInput(
            "contaminationTable",
            File(optional=True),
            prefix="--contamination-table",
            doc="Tables containing contamination information.",
        ),
        ToolInput(
            "segmentationFile",
            File(optional=True),
            prefix="--tumor-segmentation",
            doc="Tables containing tumor segments' minor allele fractions for germline hets emitted by CalculateContamination",
        ),
        ToolInput(
            "statsFile",
            File(optional=True),
            prefix="--stats",
            doc="The Mutect stats file output by Mutect2",
        ),
        ToolInput(
            "readOrientationModel",
            File(optional=True),
            prefix="--orientation-bias-artifact-priors",
            doc="One or more .tar.gz files containing tables of prior artifact probabilities for the read orientation filter model, one table per tumor sample",
        ),
    ]

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
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/4.1.2.0/org_broadinstitute_hellbender_tools_walkers_contamination_CalculateContamination.php",
            documentation="""
Calculates the fraction of reads coming from cross-sample contamination, given results from GetPileupSummaries. The resulting contamination table is used with FilterMutectCalls.

This tool is featured in the Somatic Short Mutation calling Best Practice Workflow. See Tutorial#11136 for a step-by-step description of the workflow and Article#11127 for an overview of what traditional somatic calling entails. For the latest pipeline scripts, see the Mutect2 WDL scripts directory.

This tool borrows from ContEst by Cibulskis et al the idea of estimating contamination from ref reads at hom alt sites. However, ContEst uses a probabilistic model that assumes a diploid genotype with no copy number variation and independent contaminating reads. That is, ContEst assumes that each contaminating read is drawn randomly and independently from a different human. This tool uses a simpler estimate of contamination that relaxes these assumptions. In particular, it works in the presence of copy number variations and with an arbitrary number of contaminating samples. In addition, this tool is designed to work well with no matched normal data. However, one can run GetPileupSummaries on a matched normal bam file and input the result to this tool.
""".strip(),
        )

    def arguments(self):
        return [
            # ToolArgument(MemorySelector(prefix="-Xmx", suffix="G", default=8), prefix="--java-options", position=0)
        ]
