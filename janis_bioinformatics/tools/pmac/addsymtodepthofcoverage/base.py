from abc import ABC
import datetime

from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import ToolInput, ToolOutput, File, Filename, InputSelector
from janis_bioinformatics.data_types import Bed
from janis_unix import TextFile


class AddSymToDepthOfCoverageBase(BioinformaticsTool, ABC):
    def tool(self):
        return "addSymToDepthOfCoverage"

    def friendly_name(self):
        return "Add Sym to DepthOfCoverage"

    def base_command(self):
        return "add_sym_to_DepthOfCoverage.py"

    def inputs(self):
        return [
            ToolInput(
                "inputFile",
                File(),
                prefix="-i",
                doc="Gatk3 DepthOfCoverage interval_summary output",
            ),
            ToolInput(
                "outputFilename", Filename(), prefix="-o", doc="Output file name"
            ),
            ToolInput("bed", Bed(), prefix="-bed", doc="Annotated bed file"),
        ]

    def outputs(self):
        return [ToolOutput("out", TextFile(), glob=InputSelector("outputFilename"))]

    def bind_metadata(self):
        self.metadata.creator = "Jiaan Yu"
        self.metadata.dateUpdated = datetime.datetime(2020, 4, 9)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentationUrl = (
            "https://github.com/PMCC-BioinformaticsCore/scripts/tree/master/performance"
        )
        self.metadata.documentation = """usage: add_sym_to_DepthOfCoverage.py [-h] -i INPUT -o OUTPUT -bed BED

Performance summary of bam

optional arguments:
  -h, --help  show this help message and exit
  -i INPUT    Gatk3 DepthOfCoverage interval_summary output
  -o OUTPUT   Output file name
  -bed BED    Annotated bed file
        """
