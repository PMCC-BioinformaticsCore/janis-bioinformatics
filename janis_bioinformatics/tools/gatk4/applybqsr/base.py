import operator
import os
from abc import ABC
from typing import Dict, Any

from janis_core.tool.test_classes import (
    TTestCase,
    TTestExpectedOutput,
    TTestPreprocessor,
)

from ..gatk4toolbase import Gatk4ToolBase
from janis_bioinformatics.data_types import BamBai, FastaWithDict, Bed

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    String,
    InputSelector,
    CaptureType,
    ToolMetadata,
    Array,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_unix import Tsv

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

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
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4ApplyBqsrBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ApplyBQSR"

    def friendly_name(self):
        return "GATK4: Apply base quality score recalibration"

    def tool(self):
        return "Gatk4ApplyBQSR"

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

    def inputs(self):
        return [
            *super(Gatk4ApplyBqsrBase, self).inputs(),
            ToolInput(
                "bam",
                BamBai(),
                prefix="-I",
                doc="The SAM/BAM/CRAM file containing reads.",
                secondaries_present_as={".bai": "^.bai"},
                position=10,
            ),
            ToolInput(
                "reference", FastaWithDict(), prefix="-R", doc="Reference sequence"
            ),
            ToolInput(
                "outputFilename",
                Filename(
                    prefix=InputSelector("bam", remove_file_extension=True),
                    suffix=".recalibrated",
                    extension=".bam",
                ),
                prefix="-O",
                doc="Write output to this file",
            ),
            ToolInput(
                "recalFile",
                Tsv(optional=True),
                prefix="--bqsr-recal-file",
                doc="Input recalibration table for BQSR",
            ),
            ToolInput(
                "intervals",
                Bed(optional=True),
                prefix="--intervals",
                doc="-L (BASE) One or more genomic intervals over which to operate",
            ),
            ToolInput(
                "intervalStrings",
                Array(String, optional=True),
                prefix="--intervals",
                prefix_applies_to_all_elements=True,
                doc="-L (BASE) One or more genomic intervals over which to operate",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                BamBai(),
                glob=InputSelector("outputFilename"),
                secondaries_present_as={".bai": "^.bai"},
            )
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 1, 24),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_ApplyBQSR.php",
            documentation="""
Apply base quality score recalibration: This tool performs the second pass in a two-stage 
process called Base Quality Score Recalibration (BQSR). Specifically, it recalibrates the 
base qualities of the input reads based on the recalibration table produced by the 
BaseRecalibrator tool, and outputs a recalibrated BAM or CRAM file.

Summary of the BQSR procedure: The goal of this procedure is to correct for systematic bias 
that affect the assignment of base quality scores by the sequencer. The first pass consists 
of calculating error empirically and finding patterns in how error varies with basecall 
features over all bases. The relevant observations are written to a recalibration table. 
The second pass consists of applying numerical corrections to each individual basecall 
based on the patterns identified in the first step (recorded in the recalibration table) 
and write out the recalibrated data to a new BAM or CRAM file.

- This tool replaces the use of PrintReads for the application of base quality score 
    recalibration as practiced in earlier versions of GATK (2.x and 3.x).
- You should only run ApplyBQSR with the covariates table created from the input BAM or CRAM file(s).
- Original qualities can be retained in the output file under the "OQ" tag if desired. 
    See the `--emit-original-quals` argument for details.
""".strip(),
        )

    additional_args = [
        # Put more detail in here from documentation
        ToolInput(
            "tmpDir",
            String(optional=True),
            prefix="--tmp-dir",
            position=11,
            default="/tmp/",
            doc="Temp directory to use.",
        )
    ]

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam",
                    ),
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                    "recalFile": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.table",
                    ),
                    "intervals": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "BRCA1.hg38.bed",
                    ),
                },
                output=BamBai.basic_test(
                    "out",
                    2600000,
                    21000,
                    os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.recalibrated.flagstat",
                    ),
                ),
            ),
            TTestCase(
                name="minimal",
                input={
                    "bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam",
                    ),
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                    "recalFile": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.table",
                    ),
                    "intervals": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "BRCA1.hg38.bed",
                    ),
                },
                output=self.minimal_test(),
            ),
        ]
