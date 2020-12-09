from datetime import datetime
from typing import List, Optional, Union

from janis_core import ToolOutput, ToolInput, InputSelector, Int, String, ToolMetadata

from janis_bioinformatics.data_types import (
    Fasta,
    FastaBwa,
    FastaFai,
    FastaDict,
    FastaWithIndexes,
)
from janis_bioinformatics.tools import BioinformaticsWorkflow, BioinformaticsTool
from janis_bioinformatics.tools.bwa import BwaIndexLatest
from janis_bioinformatics.tools.gatk4 import Gatk4CreateSequenceDictionaryLatest
from janis_bioinformatics.tools.samtools.faidx.versions import SamToolsFaidxLatest


class _JoinIndexedFasta(BioinformaticsTool):
    def tool(self) -> str:
        return "join_indexed_fastas"

    def base_command(self) -> Optional[Union[str, List[str]]]:
        return ["echo", "Joining fastas"]

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "ref_bwa", FastaBwa, localise_file=True, presents_as="reference.fasta"
            ),
            ToolInput(
                "ref_samtools",
                FastaFai,
                localise_file=True,
                presents_as="reference.fasta",
            ),
            ToolInput(
                "ref_dict", FastaDict, localise_file=True, presents_as="reference.fasta"
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out_reference", FastaWithIndexes, selector=InputSelector("ref_bwa")
            )
        ]

    def container(self) -> str:
        return "ubuntu:latest"

    def version(self) -> str:
        return "v0.1.0"

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 2, 14),
            dateUpdated=datetime(2020, 11, 10),
            documentation="",
        )

    def skip_test(cls) -> bool:
        return True


class IndexFasta(BioinformaticsWorkflow):
    def id(self):
        return "IndexFasta"

    def friendly_name(self):
        return "Index Fasta reference"

    def tool_provider(self):
        return "common"

    def version(self):
        return "1.0.0"

    def constructor(self):

        self.input("reference", Fasta)

        # Change the default BWA index algorithm to bwtsw (for human genome), and up blockSize to 50M
        self.input("bwa_algorithm", String(optional=True), default="bwtsw")
        self.input("bwa_block_size", Int(optional=True), default=int(5e7))

        self.step(
            "create_bwa",
            BwaIndexLatest(
                reference=self.reference,
                algorithm=self.bwa_algorithm,
                blockSize=self.bwa_block_size,
            ),
        )
        self.step("create_samtools", SamToolsFaidxLatest(reference=self.reference))
        self.step(
            "create_dict", Gatk4CreateSequenceDictionaryLatest(reference=self.reference)
        )

        self.step(
            "merge",
            _JoinIndexedFasta(
                ref_bwa=self.create_bwa,
                ref_samtools=self.create_samtools,
                ref_dict=self.create_dict,
            ),
        )

        self.output("out_reference", source=self.merge.out_reference)
        self.output("out_bwa", source=self.create_bwa, output_name="reference")
        self.output(
            "out_samtools", source=self.create_samtools, output_name="reference"
        )
        self.output("out_dict", source=self.create_dict, output_name="reference")

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 2, 14),
            dateUpdated=datetime(2020, 11, 10),
            documentation="",
        )


if __name__ == "__main__":
    IndexFasta().translate(
        "wdl",
        export_path="~/Desktop/tmp/wdltests/indexfasta",
        to_disk=True,
        validate=True,
    )
