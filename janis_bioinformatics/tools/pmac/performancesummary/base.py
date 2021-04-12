import operator
import os
from abc import ABC
import datetime

from janis_core.tool.test_classes import (
    TTestCase,
    TTestExpectedOutput,
    TTestPreprocessor,
)

from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import ToolInput, ToolOutput, File, Filename, InputSelector, Boolean
from janis_unix import Csv, TextFile


class PerformanceSummaryBase(BioinformaticsTool, ABC):
    def tool(self):
        return "performanceSummary"

    def friendly_name(self):
        return "Performance Summary"

    def base_command(self):
        return "performance_summary.py"

    def inputs(self):
        return [
            ToolInput(
                "flagstat",
                File(),
                prefix="--flagstat",
                doc="output of samtools flagstat on bam",
            ),
            ToolInput(
                "collectInsertSizeMetrics",
                File,
                prefix="--collect_insert_metrics",
                doc="output of CollectInsertMetrics (GATK or Picard) on bam",
            ),
            ToolInput(
                "coverage",
                File(),
                prefix="--coverage",
                doc="output of bedtools coverageBed for targeted bam; bedtools genomeCoverageBed for whole genome bam",
            ),
            ToolInput(
                "outputPrefix",
                Filename(extension=".csv"),
                prefix="-o",
                doc="prefix of output summary csv",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [ToolOutput("out", Csv(), glob=InputSelector("outputPrefix") + ".csv")]

    additional_args = [
        ToolInput(
            "targetFlagstat",
            File(optional=True),
            prefix="--target_flagstat",
            doc="output of samtools flagstat of bam target on target bed. Only specified for targeted bam",
        ),
        ToolInput(
            "rmdupFlagstat",
            File(optional=True),
            prefix="--rmdup_flagstat",
            doc="output of samtools flagstat of removed duplicates bam. File to be used to extract mapping infomation if specified, instead of the --flagstat file.",
        ),
        ToolInput(
            "genome",
            Boolean(optional=True),
            prefix="--genome",
            doc="calculate statistics for whole genome data.--target_flagstat must not be speicified",
        ),
    ]

    def bind_metadata(self):
        self.metadata.dateCreated = datetime.datetime(2020, 4, 3)
        self.metadata.dateUpdated = datetime.datetime(2020, 4, 3)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """usage: performance_summary.py [-h] --flagstat FLAGSTAT
                              --collect_insert_metrics COLLECT_INSERT_METRICS
                              --coverage COVERAGE -o O
                              [--target_flagstat TARGET_FLAGSTAT]
                              [--rmdup_flagstat RMDUP_FLAGSTAT] [--genome]

Performance summary of bam

required arguments:
  --flagstat FLAGSTAT   output of samtools flagstat on bam
  --collect_insert_metrics COLLECT_INSERT_METRICS
                        output of CollectInsertMetrics (GATK or Picard) on bam
  --coverage COVERAGE   output of bedtools coverageBed for targeted bam;
                        bedtools genomeCoverageBed for whole genome bam
  -o O                  output summary csv name

optional arguments:
  -h, --help            show this help message and exit
  --target_flagstat TARGET_FLAGSTAT
                        output of samtools flagstat of bam target on target
                        bed. Only specified for targeted bam
  --rmdup_flagstat RMDUP_FLAGSTAT
                        output of samtools flagstat of removed duplicates bam.
                        File to be used to extract mapping infomation if
                        specified, instead of the --flagstat file.
  --genome              calculate statistics for whole genome data.
                        --target_flagstat must not be speicified
        """
        self.metadata.documentationUrl = (
            "https://github.com/PMCC-BioinformaticsCore/scripts/tree/master/performance"
        )

    def tests(self):
        with open(
            os.path.join(
                BioinformaticsTool.test_data_path(),
                "wgsgermline_data",
                "NA12878-BRCA1_performance_summary.csv",
            ),
            "r",
        ) as f:
            expected_content = f.read()
        return [
            TTestCase(
                name="basic",
                input={
                    "flagstat": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam.flagstat",
                    ),
                    "collectInsertSizeMetrics": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.metrics.txt",
                    ),
                    "coverage": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.genomeCoverageBed.stdout",
                    ),
                    "rmdupFlagstat": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam.bam.flagstat",
                    ),
                    "genome": True,
                },
                output=TextFile.basic_test(
                    "out", 948, expected_content, 2, "575354942cfb8d0367725f9020181443"
                ),
            )
        ]
