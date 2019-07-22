from ..data_types.bam import Bam
from janis_core import File, CommandTool, ToolOutput, ToolInput


class Gather(CommandTool):
    bamFile = ToolInput("bamFile", Bam())
    bamIndex = ToolInput("bamIndex", File())

    out = ToolOutput("out", Bam())

    @staticmethod
    def tool():
        return "gather"

    @staticmethod
    def base_command():
        return "javac"
