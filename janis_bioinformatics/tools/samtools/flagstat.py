import janis_core as j
from janis_bioinformatics.data_types.bam import Bam


SamToolsFlagstat_1_9 = j.CommandToolBuilder(
    tool="samtoolsflagstat",
    base_command=["samtools", "flagstat"],
    inputs=[
        # 1. Positional bam input
        j.ToolInput("bam", Bam, position=1),
        # 2. `threads` inputs
        j.ToolInput("threads", j.Int(optional=True), prefix="--threads"),
    ],
    outputs=[j.ToolOutput("stats", j.Stdout)],
    container="quay.io/biocontainers/samtools:1.9--h8571acd_11",
    version="v1.9.0",
)
