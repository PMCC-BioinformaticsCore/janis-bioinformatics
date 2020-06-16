from abc import ABC
from typing import Any, Dict

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolMetadata,
    String,
    Int,
    Filename,
    InputSelector,
)

from janis_bioinformatics.data_types import Fasta
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

from ..data_types import KallistoIdx


class KallistoIndexBase(BioinformaticsTool, ABC):
    def tool(self):
        return "kallistoIndex"

    def friendly_name(self):
        return "Kallisto-Index"

    def tool_provider(self):
        return "Kallisto"

    def base_command(self):
        return ["kallisto", "index"]

    def inputs(self):
        return [
            ToolInput(
                "kmer_size",
                Int(optional=True),
                prefix="-k",
                position=1,
                doc="k-mer (odd) length (default: 31, max value: 31)",
            ),
            ToolInput(
                "index",
                Filename(extension=".kidx"),
                prefix="-i",
                position=2,
                doc="Filename for the kallisto index to be constructed",
            ),
            ToolInput(
                "reference",
                Fasta,
                position=3,
                localise_file=True,
                doc="Filename for a reference transcriptome",
            ),
            # --make-unique           Replace repeated target names with unique names
        ]

    def outputs(self):
        return [ToolOutput("out", KallistoIdx, glob=InputSelector("index"))]

    def memory(self, hints: Dict[str, Any]):
        return 2

    def cpus(self, hints: Dict[str, Any]):
        return 1

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Thomas Conway"],
            dateCreated=date(2020, 5, 25),
            dateUpdated=date(2020, 5, 25),
            institution="Pachter Lab",
            doi="https://doi.org/10.1038/nbt.3519",
            citation="NL Bray, H Pimentel, P Melsted and L Pachter, Near optimal probabilistic RNA-seq quantification, Nature Biotechnology 34, p 525--527 (2016).",
            keywords=["kallisto", "index", "reference"],
            documentationUrl="https://pachterlab.github.io/kallisto/manual.html",
            documentation="Builds a kallisto index",
        )
