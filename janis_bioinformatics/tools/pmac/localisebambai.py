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
            ToolInput("bam", BamBai, localise_file=True),
        ]

    def outputs(self):
        return [ToolOutput("out", BamBai, selector=InputSelector("bam").basename())]

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.dateCreated = datetime(2022, 1, 7)
        self.metadata.dateUpdated = datetime(2022, 1, 7)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """\
Localise BamBai
        """
