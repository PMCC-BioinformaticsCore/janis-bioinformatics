from abc import ABC
from typing import List

from janis_core import File, ToolOutput, InputSelector

from janis_bioinformatics.data_types import Bam

from janis_bioinformatics.tools.star.base import StarBase


class StarAlignReadsBase(StarBase, ABC):
    def run_mode(self):
        return "alignReads"

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "bam",
                Bam(optional=True),
                glob=InputSelector("outFileNamePrefix")
                + "Aligned.sortedByCoord.out.bam",
            ),
            ToolOutput(
                "out",
                File,
                glob=InputSelector("outFileNamePrefix") + "SJ.out.tab",
                doc="Each splicing is counted in the numbers of splices, which would correspond to summing the counts in SJ.out.tab.",
            ),
            ToolOutput(
                "outLog",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.out",
                doc="main log file with a lot of detailed information about the run. This file is most useful for troubleshooting and debugging.",
            ),
            ToolOutput(
                "outProgressOut",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.progress.out",
                doc="reports job progress statistics, such as the number of processed reads, % of mapped reads etc.",
            ),
            ToolOutput(
                "logFinalOut",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.final.out",
                doc="summary mapping statistics after mapping job is complete, very useful for quality control.",
            ),
        ]
