from abc import ABC
from datetime import date

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolArgument,
    Boolean,
    Int,
    Filename,
    InputSelector,
)
from janis_bioinformatics.data_types.bam import BamBai, File
from janis_bioinformatics.data_types.fasta import FastaFai
from janis_bioinformatics.tools.sequenza.sequenza_base import SequenzaBase
from janis_core import ToolMetadata


class SeqzBam2SeqBase(SequenzaBase, ABC):
    def tool(self):
        return "SeqzBam2Seqz"

    @classmethod
    def sequenza_command(cls):
        return "bam2seqz"

    def inputs(self):
        return [
            *super(SeqzBam2SeqBase, self).inputs(),
            ToolInput(
                "normal",
                BamBai(),
                prefix="--normal",
                position=2,
                doc="Name of the BAM/pileup file from the reference/normal sample",
            ),
            ToolInput(
                "tumour",
                BamBai(),
                prefix="--tumor",  # How do you spell tumour?
                position=4,
                doc="Name of the BAM/pileup file from the reference/normal sample",
            ),
            ToolInput(
                "wiggle_file",
                File(),
                prefix="-gc",
                position=6,
                doc="The GC-content wiggle file",
            ),
            ToolInput(
                "fasta_reference",
                FastaFai(),
                prefix="--fasta",
                position=8,
                doc="The reference FASTA file used to generate the intermediate pileup. Required when input are BAM",
            ),
            ToolInput(
                "output_filename",
                Filename(extension=".gz"),
                prefix="--output",
                position=10,
                doc="Name of the output file. To use gzip compression name the file ending in .gz. Default STDOUT.",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("output_filename"))]

    def friendly_name(self):
        return "Sequenza: bam2seqz"

    def bind_metadata(self):
        self.metadata = ToolMetadata(
            contributors=["mumbler", "evanwehi"],
            dateCreated=date(2019, 12, 10),
            dateUpdated=date(2019, 12, 10),
            institution="DTU",
            doi=None,
            citation=None,  # find citation
            keywords=["sequenza", "bam2seqz"],
            documentationUrl="http://www.cbs.dtu.dk/biotools/sequenza/",
            documentation="""""".strip(),
        )
        return self.metadata

    def arguments(self):
        return []

    additional_inputs = []
