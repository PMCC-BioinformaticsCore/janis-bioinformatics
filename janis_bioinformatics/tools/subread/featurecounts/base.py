from abc import ABC

from janis_unix import TextFile
from janis_core import (
    ToolInput,
    Int,
    Boolean,
    ToolOutput,
    Array,
    Stdout,
    InputSelector,
    Filename,
    File,
    String,
)
from janis_core import ToolMetadata
from janis_bioinformatics.data_types import Bam
from janis_bioinformatics.tools.subread.subreadtoolbase import SubreadToolBase


class featureCountsBase(SubreadToolBase, ABC):
    def tool(self):
        return "featureCounts"

    @classmethod
    def subread_command(cls):
        return "featureCounts"

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput(
                "bam",
                Array(Bam),
                position=10,
                doc="A list of SAM or BAM format files. They can be either name or location sorted. If no files provided, <stdin> input is expected. Location-sorted paired-end reads are automatically sorted by read names.",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".txt"),
                prefix="-o",
                doc="Name of output file including read counts. A separate file including summary statistics of counting results is also included in the output ('<string>.summary'). Both files are in tab delimited format.",
            ),
            ToolInput(
                "annotationFile",
                File,
                prefix="-a",
                doc="Name of an annotation file. GTF/GFF format by default. See -F option for more format information. Inbuilt annotations (SAF format) is available in 'annotation' directory of the package. Gzipped file is also accepted.",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", TextFile, glob=InputSelector("outputFilename"))]

    def friendly_name(self):
        return "featureCounts"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 7, 16),
            dateUpdated=date(2020, 7, 16),
            institution="Walter and Eliza Hall Institute of Medical Research",
            doi=None,
            citation=None,
            keywords=["subread", "featureCounts"],
            documentationUrl="https://www.rdocumentation.org/packages/Rsubread/versions/1.22.2/topics/featureCounts",
            documentation="""FeatureCounts: A General-Purpose Read Summarization Function
This function assigns mapped sequencing reads to genomic features""".strip(),
        )

    additional_inputs = []

