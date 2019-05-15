from datetime import datetime
from janis import CommandTool, ToolInput, ToolOutput, File, Boolean, String, Int, InputSelector, Filename, ToolMetadata
from janis.types import MemorySelector
from janis_bioinformatics.data_types import Vcf


class BCFToolsSortBase(CommandTool):

    def friendly_name(self) -> str:
        return "BCFTools Sort"

    @staticmethod
    def tool_provider():
        return "Samtools"

    @staticmethod
    def tool() -> str:
        return "BCFToolsSort"

    @staticmethod
    def base_command():
        return ['bcftools', 'sort']

    def inputs(self):
        return [
            ToolInput("vcf", Vcf(), position=1, doc="The VCF file to sort"),
            # ToolInput("maxMem", String(optional=True), default=MemorySelector(suffix="G"), prefix="--max-mem", doc="(-m) maximum memory to use [768M]"),
            ToolInput("outputFilename", Filename(), prefix="--output-file", doc="(-o) output file name [stdout]"),
            ToolInput("outputType", String(optional=True), prefix="--output-type",
                      doc="(-O) b: compressed BCF, u: uncompressed BCF, z: compressed VCF, v: uncompressed VCF [v]"),
            ToolInput("tempDir", String(optional=True), prefix="--temp-dir",
                      doc="(-T) temporary files [/tmp/bcftools-sort.XXXXXX/]"),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Vcf(), glob=InputSelector("outputFilename"))
        ]

    def metadata(self):
        return ToolMetadata(
            creator=None,
            maintainer=None, maintainer_email=None,
            date_created=datetime(2019, 5, 9), date_updated=datetime(2019, 5, 9),
            institution=None, doi=None,
            citation=None,
            keywords=["BCFToolsSort"],
            documentation_url="",
            documentation="""About:   Sort VCF/BCF file.
Usage:   bcftools sort [OPTIONS] <FILE.vcf>
""")