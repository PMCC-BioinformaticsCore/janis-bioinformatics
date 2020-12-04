from abc import ABC
import datetime

from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import ToolInput, ToolOutput, File, Filename, Int, InputSelector, String
from janis_unix import TextFile


class GeneCoveragePerSampleBase(BioinformaticsTool, ABC):
    def tool(self):
        return "geneCoveragePerSample"

    def friendly_name(self):
        return "Gene Coverage Per Sample"

    def base_command(self):
        return "gene_coverage_per_sample.py"

    def inputs(self):
        return [
            ToolInput(
                "listFile",
                File(optional=True),
                prefix="--list",
                doc="List file: A tsv file contains SampleName\tPathToBedtoolsOutput on each line",
            ),
            ToolInput(
                "sampleName",
                String(optional=True),
                prefix="--name",
                doc="Sample name if list not used",
            ),
            ToolInput(
                "bedtoolsOutputPath",
                File(optional=True),
                prefix="--path",
                doc="Path to bedtools output if list not used",
            ),
            ToolInput(
                "outputGeneFile",
                Filename(extension=".txt", suffix=".gene"),
                prefix="--gene",
                doc="Output gene file",
            ),
            ToolInput(
                "outputRegionFile",
                Filename(extension=".txt", suffix=".region"),
                prefix="--region",
                doc="Output region file",
            ),
            ToolInput(
                "fold",
                String(optional=True),
                prefix="--fold",
                doc="Folds, quoted and commna sepparated, default 1,10,20,100",
            ),
            ToolInput(
                "threads",
                Int(optional=True),
                prefix="--threads",
                doc="number of threads, default:32",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput("geneFileOut", TextFile(), glob=InputSelector("outputGeneFile")),
            ToolOutput(
                "regionFileOut", TextFile(), glob=InputSelector("outputRegionFile")
            ),
        ]

    def bind_metadata(self):
        self.metadata.dateCreated = datetime.datetime(2020, 4, 3)
        self.metadata.dateUpdated = datetime.datetime(2020, 4, 3)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """usage: gene_coverage_per_sample.py [-h] [-l LIST] [-n NAME] [-p PATH] [-b BED]
                                   [-g GENE] [-r REGION] [-f FOLDS] [-d]
                                   [-t THREADS]

Gene or region coverage of bam

optional arguments:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  List file: A tsv file contains SampleName
                        PathToBedtoolsOutput on each line
  -n NAME, --name NAME  Sample name if list not used
  -p PATH, --path PATH  Path to bedtools output if list not used
  -b BED, --bed BED     (Deprecated option) Bed file
  -g GENE, --gene GENE  Output gene file
  -r REGION, --region REGION
                        Output region file
  -f FOLDS, --folds FOLDS
                        Folds, quoted and commna sepparated, default
                        1,10,20,100
  -d, --remove_duplicates
                        (Deprecated option) Remove marked duplicates in
                        analysis, default:false
  -t THREADS, --threads THREADS
                        number of threads, default:32
        """
        self.metadata.documentationUrl = (
            "https://github.com/PMCC-BioinformaticsCore/scripts/tree/master/performance"
        )
