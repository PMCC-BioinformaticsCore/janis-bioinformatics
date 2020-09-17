from abc import ABC
import datetime

from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import (
    ToolInput,
    ToolOutput,
    File,
    Filename,
    Int,
    InputSelector,
    String,
    Array,
)
from janis_unix import TextFile, Csv


class GenerateCountsForALLSortsBase(BioinformaticsTool, ABC):
    def tool(self):
        return "generateCountsForALLSorts"

    def friendly_name(self):
        return "generateCountsForALLSorts"

    def base_command(self):
        return "generate_counts_for_allsorts.py"

    def inputs(self):
        return [
            ToolInput(
                "inp", Array(TextFile), prefix="-i", doc="One or more input files"
            ),
            ToolInput(
                "outputFilename", Filename(extension=".csv"), doc="Output csv filename"
            ),
            ToolInput(
                "type",
                String,
                prefix="--type",
                doc="Specity from which tool input file(s) are generated, must featureCounts or htseq-count",
            ),
            ToolInput(
                "samples",
                Array(String),
                prefix="--samples",
                doc="One or more labels (samples) for input file(s) in the same order",
            ),
            ToolInput(
                "geneColumn",
                String(optional=True),
                prefix="--gene_column",
                doc="Specify which column to use to obtain gene_id, htseq-count only",
            ),
            ToolInput(
                "countColumn",
                String(optional=True),
                prefix="--count_column",
                doc="Specify which column to use to obtain count for genes, htseq-count only",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Csv(), glob=InputSelector("outputFilename"))]

    def bind_metadata(self):
        self.metadata.creator = "Jiaan Yu"
        self.metadata.dateUpdated = datetime.datetime(2020, 9, 11)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """usage: generate_counts_for_allsorts.py [-h] -i I -o O --type
                                       {featureCounts,htseq-count} --samples
                                       SAMPLES [--gene_column GENE_COLUMN]
                                       [--count_column COUNT_COLUMN]

Generate csv files from featureCounts or htseq-count for ALLSorts input

required arguments:
  -i I                  One or more input files
  -o O                  Output csv filename
  --type {featureCounts,htseq-count}
                        Specity from which tool input file(s) are generated,
                        must featureCounts or htseq-count
  --samples SAMPLES     One or more labels (samples) for input file(s) in the
                        same order
  --gene_column GENE_COLUMN
                        Specify which column to use to obtain gene_id, htseq-
                        count only
  --count_column COUNT_COLUMN
                        Specify which column to use to obtain count for genes,
                        htseq-count only

optional arguments:
  -h, --help            show this help message and exit

"""
