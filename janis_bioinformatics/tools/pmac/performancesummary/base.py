from abc import ABC

from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import ToolInput, ToolOutput, File, Filename, InputSelector, Boolean

class PerformanceSummaryBase(BioinformaticsTool, ABC):
    def tool(self):
        return "performanceSummary"
    
    def friendly_name(self):
        return "Performance Summary"

    def base_command(self):
        return "performance_summary.py"
    
    def inputs(self):
        return [
            ToolInput("flagstat", File(), prefix="--flagstat",
            doc="output of samtools flagstat on bam"),
            ToolInput("collectInsertSizeMetrics", File, prefix="--collect_insert_metrics",
            doc="output of CollectInsertMetrics (GATK or Picard) on bam"),
            ToolInput("coverage", File(), prefix="--coverage",
            doc="output of bedtools coverageBed for targeted bam; bedtools genomeCoverageBed for whole genome bam"),
            ToolInput("outputFilename", Filename(), prefix="-o",
            doc="output summary csv name"),
            *self.additional_args,
        ]
    
    def outputs(self):
        return [
            ToolOutput("out", File(), glob=InputSelector("outputFilename")+".csv")
        ]

    additional_args = [
        ToolInput("targetFlagstat", File(optional=True), prefix="--target_flagstat",
        doc="output of samtools flagstat of bam target on target bed. Only specified for targeted bam"),
        ToolInput("rmdupFlagstat", File(optional=True), prefix="--rmdup_flagstat",
        doc="output of samtools flagstat of removed duplicates bam. File to be used to extract mapping infomation if specified, instead of the --flagstat file."),
        ToolInput("genome", Boolean(optional=True), prefix="--genome",
        doc="calculate statistics for whole genome data.--target_flagstat must not be speicified")
    ]