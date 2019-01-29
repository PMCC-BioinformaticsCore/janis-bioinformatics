from janis import ToolInput, Filename, String, ToolArgument, Array, File, Int, Boolean, ToolOutput, CommandTool
from janis.bioinformatics.data_types.bam import Bam
from janis.bioinformatics.data_types.fasta import FastaWithDict
from janis.bioinformatics.data_types.sam import Sam
from janis.bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase


class SampleBase(CommandTool):
    @staticmethod
    def tool():
        return "sample-tool-name"

    def doc(self):
        return """Documentation""".strip()

    def inputs(self):
        return [
            *super(SampleBase, self).inputs(),
            ToolInput("sampleInput", File(), prefix="--input1"),
            *SampleBase.additional_args
        ]

    def arguments(self):
        return [
            *super(SampleBase, self).arguments(),
        ]

    def outputs(self):
        return [
            *super(SampleBase, self).outputs()
        ]

    additional_args = [

    ]

