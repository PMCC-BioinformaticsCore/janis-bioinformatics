from abc import ABC
from datetime import date

from janis_core import (
    ToolInput,
    ToolOutput,
    Int,
    Filename,
    InputSelector,
)
from janis_bioinformatics.data_types.bam import File
from janis_bioinformatics.tools.sequenza.sequenza_base import SequenzaBase
from janis_core import ToolMetadata


class SeqzBinningBase(SequenzaBase, ABC):
    def tool(self):
        return "SeqzBinning"

    @classmethod
    def sequenza_command(cls):
        return "seqz_binning"

    def inputs(self):
        return [
            *super(SeqzBinningBase, self).inputs(),
            ToolInput("seqz", File(), prefix="--seqz", position=2, doc="A seqz file."),
            ToolInput(
                "window",
                Int(),
                prefix="--window",
                position=4,
                doc="Window size used for binning the original seqz file. Default is 50.",
            ),
            ToolInput(
                "output_filename",
                Filename(extension=".gz"),
                prefix="-o",
                position=6,
                doc='Output file "-" for STDOUT',
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("output_filename"))]

    def friendly_name(self):
        return "Sequenza: seqz binning"

    def bind_metadata(self):
        self.metadata = ToolMetadata(
            contributors=["mumbler", "evanwehi"],
            dateCreated=date(2019, 12, 16),
            dateUpdated=date(2019, 12, 16),
            institution="DTU",
            doi=None,
            citation=None,  # find citation
            keywords=["sequenza", "seqz_binning"],
            documentationUrl="http://www.cbs.dtu.dk/biotools/sequenza/",
            documentation="""""".strip(),
        )
        return self.metadata

    def arguments(self):
        return []

    additional_inputs = []
