from datetime import datetime
from janis_core import ToolInput, ToolOutput, ToolArgument, InputSelector, Filename

from janis_unix.tools.unixtool import UnixTool
from janis_bioinformatics.data_types import FastaWithDict


class LocaliseFastaWithDict(UnixTool):
    def tool(self):
        return "LocaliseFastaWithDict"

    def friendly_name(self):
        return "LocaliseFastaWithDict"

    def base_command(self):
        return None

    def inputs(self):
        return [
            ToolInput(
                "reference",
                FastaWithDict,
            ),
            ToolInput(
                "reference_all",
                Filename(prefix=InputSelector("reference"), extension="*"),
                position=2,
                shell_quote=False,
            ),
            ToolInput(
                "reference_dict",
                Filename(
                    prefix=InputSelector("reference", remove_file_extension=True),
                    extension=".dict",
                ),
                position=2,
                shell_quote=False,
            ),
            ToolInput(
                "reference_output",
                Filename(prefix=InputSelector("reference"), extension=".fasta"),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput("out", FastaWithDict, selector=InputSelector("reference_output"))
        ]

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
