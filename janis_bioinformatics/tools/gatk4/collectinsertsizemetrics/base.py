import operator
import os
from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    String,
    Array,
    File,
    Int,
    Boolean,
    ToolOutput,
    InputSelector,
    CaptureType,
    Double,
    Float,
)
from janis_core import get_value_for_hints_and_ordered_resource_tuple
from janis_core import ToolMetadata
from janis_core.tool.test_classes import (
    TTestCase,
    TTestExpectedOutput,
    TTestPreprocessor,
)
from janis_unix import TextFile

from janis_bioinformatics.data_types import Bam, BamBai, FastaWithDict
from ..gatk4toolbase import Gatk4ToolBase
from ... import BioinformaticsTool

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
            CaptureType.THIRTYX: 32,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4CollectInsertSizeMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectInsertSizeMetrics"

    def tool(self):
        return "Gatk4CollectInsertSizeMetrics"

    def friendly_name(self):
        return "GATK4: CollectInsertSizeMetrics"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 2, 17),
            dateUpdated=date(2020, 2, 17),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "picard", "CollectInsertSizeMetrics"],
            documentationUrl="https://gatk.broadinstitute.org/hc/en-us/articles/360036715591-CollectInsertSizeMetrics-Picard-",
            documentation="Provides useful metrics for validating library construction including the insert size distribution and read orientation of paired-end libraries",
        )

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
            *super(Gatk4CollectInsertSizeMetricsBase, self).inputs(),
            ToolInput(
                "bam",
                BamBai(optional=False),
                prefix="-I",
                doc="Input SAM or BAM file.  Required.",
                position=10,
            ),
            ToolInput(
                "outputFilename",
                Filename(
                    prefix=InputSelector("bam", remove_file_extension=True),
                    extension=".txt",
                    suffix=".metrics",
                ),
                prefix="-O",
                doc="File to write the output to.  Required.",
            ),
            ToolInput(
                "outputHistogram",
                Filename(
                    prefix=InputSelector("bam", remove_file_extension=True),
                    extension=".pdf",
                    suffix=".histogram",
                ),
                prefix="-H",
                doc="File to write insert size Histogram chart to.  Required. ",
            ),
            *Gatk4CollectInsertSizeMetricsBase.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput("out", TextFile(), glob=InputSelector("outputFilename")),
            ToolOutput(
                "outHistogram",
                File(extension=".pdf"),
                glob=InputSelector("outputHistogram"),
            ),
        ]

    additional_args = [
        ToolInput(
            "argumentsFile",
            Array(File(), optional=True),
            prefix="--arguments_file",
            position=10,
            prefix_applies_to_all_elements=True,
            doc="read one or more arguments files and add them to the command line",
        ),
        ToolInput(
            "assumeSorted",
            Boolean(optional=True),
            prefix="--ASSUME_SORTED",
            position=11,
            doc="If true (default), then the sort order in the header file will be ignored.  Default value: true. Possible values: {true, false}",
        ),
        ToolInput(
            "deviations",
            Double(optional=True),
            prefix="--DEVIATIONS",
            position=11,
            doc="Generate mean, sd and plots by trimming the data down to MEDIAN + DEVIATIONS*MEDIAN_ABSOLUTE_DEVIATION. This is done because insert size data typically includes enough anomalous values from chimeras and other artifacts to make the mean and sd grossly misleading regarding the real distribution.  Default value: 10.0. ",
        ),
        ToolInput(
            "histogramWidth",
            Int(optional=True),
            prefix="--HISTOGRAM_WIDTH",
            position=11,
            doc="Explicitly sets the Histogram width, overriding automatic truncation of Histogram tail. Also, when calculating mean and standard deviation, only bins <= Histogram_WIDTH will be included.  Default value: null. ",
        ),
        ToolInput(
            "includeDuplicates",
            Boolean(optional=True),
            prefix="--INCLUDE_DUPLICATES",
            position=11,
            doc="If true, also include reads marked as duplicates in the insert size histogram.  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            "metricAccumulationLevel",
            String(optional=True),
            prefix="--METRIC_ACCUMULATION_LEVEL",
            position=11,
            doc="The level(s) at  which to accumulate metrics.    This argument may be specified 0 or more times. Default value: [ALL_READS]. Possible values: {ALL_READS, SAMPLE, LIBRARY, READ_GROUP} .",
        ),
        ToolInput(
            "minimumPCT",
            Float(optional=True),
            prefix="--MINIMUM_PCT",
            position=11,
            doc="When generating the Histogram, discard any data categories (out of FR, TANDEM, RF) that have fewer than this percentage of overall reads. (Range: 0 to 1).  Default value: 0.05.",
        ),
        ToolInput(
            "stopAfter",
            Int(optional=True),
            prefix="--STOP_AFTER",
            position=11,
            doc="Stop after  processing N reads, mainly for debugging.  Default value: 0. ",
        ),
        ToolInput(
            "version",
            Boolean(optional=True),
            prefix="--version",
            position=11,
            doc="display the version number for this tool Default value: false. Possible values: {true, false}",
        ),
        ToolInput(
            "showHidden",
            Boolean(optional=True),
            prefix="--showHidden",
            position=11,
            doc="display hidden  arguments  Default  value: false.  Possible values: {true, false} ",
        ),
    ]

    def tests(self):
        # The first 5 lines of the file include headers that change with every run (time, etc)
        with open(
            os.path.join(
                BioinformaticsTool.test_data_path(),
                "wgsgermline_data",
                "NA12878-BRCA1.markduped.metrics.txt",
            ),
            "r",
        ) as f:
            for i in range(5):
                next(f)
            expected_content = f.read()
        return [
            TTestCase(
                name="basic",
                input={
                    "bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam",
                    ),
                    "javaOptions": ["-Xmx6G"],
                },
                output=TextFile.basic_test("out", 7260, expected_content, 905)
                + [
                    TTestExpectedOutput(
                        tag="outHistogram",
                        preprocessor=TTestPreprocessor.FileSize,
                        operator=operator.ge,
                        expected_value=15600,
                    ),
                ],
            )
        ]
