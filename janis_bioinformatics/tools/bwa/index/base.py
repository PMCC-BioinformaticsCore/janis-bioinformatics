from abc import ABC
from typing import Any, Dict

from janis_core import ToolInput, ToolOutput, ToolMetadata, String, Int, InputSelector

from janis_bioinformatics.data_types import Fasta, FastaBwa
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class BwaIndexBase(BioinformaticsTool, ABC):
    def tool(self):
        return "bwaIndex"

    def friendly_name(self):
        return "BWA-Index"

    def tool_provider(self):
        return "BWA"

    def base_command(self):
        return ["bwa", "index"]

    def inputs(self):
        return [
            ToolInput("reference", Fasta, position=1, localise_file=True),
            # ToolInput(
            #     "prefix",
            #     String(optional=True),
            #     prefix="-p",
            #     doc="prefix of the index [same as fasta name]",
            # ),
            ToolInput(
                "blockSize",
                Int(optional=True),
                prefix="-b",
                doc="block size for the bwtsw algorithm (effective with -a bwtsw) [10000000]",
            ),
            ToolInput(
                "algorithm",
                String(optional=True),
                prefix="-a",
                doc="""\
BWT construction algorithm: bwtsw, is or rb2 [auto]
    - is	IS linear-time algorithm for constructing suffix array. It requires 5.37N memory where N is the size of the database. IS is moderately fast, but does not work with database larger than 2GB. IS is the default algorithm due to its simplicity. The current codes for IS algorithm are reimplemented by Yuta Mori.
    - bwtsw	Algorithm implemented in BWT-SW. This method works with the whole human genome.
""",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", FastaBwa, glob=InputSelector("reference"))]

    def memory(self, hints: Dict[str, Any]):
        return 8

    def cpus(self, hints: Dict[str, Any]):
        return 1

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2020, 2, 14),
            dateUpdated=date(2020, 2, 14),
            institution="Sanger Institute",
            doi=None,
            citation="The BWA-MEM algorithm has not been published yet.",
            keywords=["bwa", "index", "reference"],
            documentationUrl="http://bio-bwa.sourceforge.net/bwa.shtml#3",
            documentation="""bwa - Burrows-Wheeler Alignment Tool
Index database sequences in the FASTA format.

Warning: `-a bwtsw' does not work for short genomes, while `-a is' and
         `-a div' do not work not for long genomes.
""".strip(),
        )
