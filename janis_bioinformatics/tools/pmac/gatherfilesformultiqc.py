from janis_core import (
    Array,
    File,
    ToolInput,
    ToolOutput,
    Filename,
    InputSelector,
    ToolArgument,
    Directory,
    String,
)
from janis_unix.tools.unixtool import UnixTool


class GatherFilesForMultiqc(UnixTool):
    def tool(self):
        return "GatherFilesForMultiqc"

    def friendly_name(self):
        return "GatherFilesForMultiqc"

    def base_command(self):
        return None

    def inputs(self):
        return [
            ToolInput(
                "inp_files",
                Array(File),
                position=4,
            ),
            ToolInput(
                "inp_files2",
                Array(File),
                position=5,
            ),
            ToolInput(
                "output_dir", String(optional=True), default="output_dir", position=8
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Directory, selector=InputSelector("output_dir"))]

    def arguments(self):
        return [
            ToolArgument("mkdir", position=0, shell_quote=False),
            ToolArgument(
                InputSelector("output_dir"),
                position=1,
                shell_quote=False,
            ),
            ToolArgument(";", position=2, shell_quote=False),
            ToolArgument("cp", position=3, shell_quote=False),
        ]

    def bind_metadata(self):
        self.metadata.documentation = """gather files to a folder for multiqc"""
