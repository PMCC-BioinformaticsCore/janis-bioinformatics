from abc import ABC
from typing import List

from janis_core import File, ToolOutput, InputSelector, WildcardSelector

from janis_bioinformatics.data_types import Bam, Sam

from janis_bioinformatics.tools.star.base import StarBase


class StarAlignReadsBase(StarBase, ABC):
    def run_mode(self):
        return "alignReads"

    def memory(self, hints):
        return 64

    def cpus(self, hints):
        return 4

    def outputs(self) -> List[ToolOutput]:
        return [
            # Bam files
            ToolOutput(
                "out_unsorted_bam",
                Bam(optional=True),
                glob=InputSelector("outFileNamePrefix") + "Aligned.out.bam",
            ),
            ToolOutput(
                "out_sorted_bam",
                Bam(optional=True),
                glob=InputSelector("outFileNamePrefix")
                + "Aligned.sortedByCoord.out.bam",
            ),
            ToolOutput(
                "out_transcriptome_bam",
                Bam(optional=True),
                glob=InputSelector("outFileNamePrefix")
                + "Aligned.toTranscriptome.out.bam",
            ),
            # Chimeric alignments files
            ToolOutput(
                "out_chimeric_out_junction",
                File(optional=True),
                glob=InputSelector("outFileNamePrefix") + "Chimeric.out.junction",
            ),
            ToolOutput(
                "out_chimeric_out_sam",
                Sam(optional=True),
                glob=InputSelector("outFileNamePrefix") + "Chimeric.out.sam",
            ),
            # Gene counts
            ToolOutput(
                "out_gene_counts",
                File(optional=True),
                glob=InputSelector("outFileNamePrefix") + "ReadsPerGene.out.tab",
            ),
            ToolOutput(
                "SJ_out_tab",
                File,
                glob=InputSelector("outFileNamePrefix") + "SJ.out.tab",
                doc="Each splicing is counted in the numbers of splices, which would correspond to summing the counts in SJ.out.tab.",
            ),
            ToolOutput(
                "Log_out",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.out",
                doc="main log file with a lot of detailed information about the run. This file is most useful for troubleshooting and debugging.",
            ),
            ToolOutput(
                "Log_progress_out",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.progress.out",
                doc="reports job progress statistics, such as the number of processed reads, % of mapped reads etc.",
            ),
            ToolOutput(
                "Log_final_out",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.final.out",
                doc="summary mapping statistics after mapping job is complete, very useful for quality control.",
            ),
        ]
