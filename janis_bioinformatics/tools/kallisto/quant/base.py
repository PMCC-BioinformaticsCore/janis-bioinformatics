from abc import ABC
from typing import Any, Dict

from janis_core import ToolInput, ToolOutput, ToolMetadata, Array, Boolean, String, Int, Double, Filename, File, InputSelector

from janis_bioinformatics.data_types import Fasta, Fastq
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

from ..data_types import KallistoIdx


class KallistoQuantBase(BioinformaticsTool, ABC):
    def tool(self):
        return "kallistoQuant"

    def friendly_name(self):
        return "Kallisto-Quant"

    def tool_provider(self):
        return "Kallisto"

    def base_command(self):
        return ["kallisto", "quant"]

    def inputs(self):
        return [
            ToolInput(
                "index",
                KallistoIdx,
                prefix="-i",
                position=2,
                doc="Filename for the kallisto index to be constructed",
            ),
            ToolInput(
                "outdir",
                Filename,
                prefix="-o",
                position=3,
                doc="directory to put outputs in"
            ),
            ToolInput(
                "fastq",
                Array(Fastq),
                position=4,
                doc="FASTQ files to process"
            ),
            ToolInput(
                "bias",
                Boolean(optional=True),
                prefix="--bias",
                doc="Perform sequence based bias correction",
            ),
            ToolInput(
                "fusion",
                Boolean(optional=True),
                prefix="--fusion",
                doc="Search for fusions for Pizzly",
            ),
            ToolInput(
                "single",
                Boolean(optional=True),
                prefix="--single",
                doc="Quantify single-end reads",
            ),
            ToolInput(
                "overhang",
                Boolean(optional=True),
                prefix="--single-overhang",
                doc="Include reads where unobserved rest of fragment is predicted to lie outside a transcript",
            ),
            ToolInput(
                "fr_stranded",
                Boolean(optional=True),
                prefix="--fr-stranded",
                doc="Strand specific reads, first read forward",
            ),
            ToolInput(
                "rf_stranded",
                Boolean(optional=True),
                prefix="--rf-stranded",
                doc="Strand specific reads, first read reverse",
            ),
            ToolInput(
                "fragment_length",
                Double(optional=True),
                prefix="-l",
                doc="Estimated average fragment length",
            ),
            ToolInput(
                "fragment_sd",
                Double(optional=True),
                prefix="-s",
                doc="Estimated standard deviation of fragment length",
            )
        ]

    def outputs(self):
        return [ToolOutput("out", File, glob=InputSelector("outdir") + "/abundance.tsv"),
                ToolOutput("stats", File, glob=InputSelector("outdir") + "/run_info.json")]

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
            documentation="Builds a kallisto index"
        )
