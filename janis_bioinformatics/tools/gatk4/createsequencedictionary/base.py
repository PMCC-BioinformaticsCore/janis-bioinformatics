from abc import ABC
from typing import Dict, Any

from janis_core import ToolInput, ToolOutput, InputSelector, ToolMetadata

from janis_bioinformatics.data_types import Fasta, FastaDict
from ..gatk4toolbase import Gatk4ToolBase


class Gatk4CreateSequenceDictionaryBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CreateSequenceDictionary"

    def tool(self):
        return "Gatk4CreateSequenceDictionary"

    def friendly_name(self):
        return "GATK4: CreateSequenceDictionary"

    def inputs(self):
        return [
            *super().inputs(),
            ToolInput(
                "reference",
                Fasta,
                prefix="--REFERENCE",
                localise_file=True,
                doc="(-R) Input reference fasta or fasta.gz  Required.",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                FastaDict,
                glob=InputSelector("reference"),
                doc="Output reference with ^.dict reference",
            )
        ]

    def cpus(self, hints: Dict[str, Any]):
        return 1

    def memory(self, hints: Dict[str, Any]):
        return 2

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2020, 2, 14),
            dateUpdated=date(2020, 2, 14),
            institution="Broad Institute",
            doi=None,
            citation="TBD",
            keywords=["gatk", "gatk4", "broad", "CreateSequenceDictionary"],
            documentationUrl="https://gatk.broadinstitute.org/hc/en-us/articles/360036509572-CreateSequenceDictionary-Picard-",
            documentation="""
Creates a sequence dictionary for a reference sequence.  This tool creates a sequence dictionary file (with ".dict"
extension) from a reference sequence provided in FASTA format, which is required by many processing and analysis tools.
The output file contains a header but no SAMRecords, and the header contains only sequence records.

The reference sequence can be gzipped (both .fasta and .fasta.gz are supported).

Usage example:

    java -jar picard.jar CreateSequenceDictionary \\
        R=reference.fasta \\
        O=reference.dict
""".strip(),
        )
