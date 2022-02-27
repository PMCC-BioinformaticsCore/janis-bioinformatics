from datetime import datetime
from janis_core import ToolInput, ToolOutput, ToolArgument, InputSelector, Filename

from janis_unix.tools.unixtool import UnixTool
from janis_bioinformatics.data_types import BamBai


class LocaliseBamBai(UnixTool):
    def tool(self):
        return "LocaliseBamBai"

    def friendly_name(self):
        return "LocaliseBamBai"

    def base_command(self):
        return None

    def inputs(self):
        return [
            ToolInput(
                "bam",
                BamBai,
            ),
            ToolInput(
                "bam_all",
                Filename(prefix=InputSelector("bam"), extension="*"),
                position=2,
            ),
            ToolInput(
                "bam_output",
                Filename(prefix=InputSelector("bam"), extension=".bam"),
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", BamBai, selector=InputSelector("bam_output"))]

    def arguments(self):
        return [
            ToolArgument("cp", position=1, shell_quote=False),
            ToolArgument(".", position=3, shell_quote=False),
        ]

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.dateCreated = datetime(2022, 1, 7)
        self.metadata.dateUpdated = datetime(2022, 1, 7)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """\
Localise Arrary of FastqGZ pairs
        """
