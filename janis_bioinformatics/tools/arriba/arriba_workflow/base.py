from abc import ABC
from datetime import datetime

from janis_unix import Tsv

from janis_bioinformatics.data_types import Fasta, FastqGzPairedEnd
from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    Double,
    Float,
    InputSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
    Array,
    Directory,
)
from janis_bioinformatics.tools.arriba.base import ArribaBase


class ArribaWorkflowBase(ArribaBase, ABC):
    @classmethod
    def arriba_command(self):
        return "run_arriba.sh"

    def friendly_name(self) -> str:
        return "Arriba Workflow Wrapper"

    def tool(self) -> str:
        return "ArribaWorkflow"

    # set a bigger default memory
    def memory(self, hints):
        return 64

    def inputs(self):
        return [
            ToolInput(
                "starGenomeDir",
                Directory(),
                position=1,
                doc="STAR_INDEX_DIR",
            ),
            ToolInput("gtf_file", File(), position=2, doc="ANNOTATION_GTF"),
            ToolInput("reference", Fasta(), position=3, doc="ASSEMBLY_FA"),
            ToolInput("blacklist", File(), position=4, doc="BLACKLIST_TSV"),
            ToolInput("known_fusions", File(), position=5, doc="KNOWN_FUSIONS_TSV"),
            ToolInput(
                "protein_domains_gff", File(), position=6, doc="PROTEIN_DOMAINS_GFF3"
            ),
            ToolInput("threads", Int(), position=7, doc="THREADS"),
            ToolInput("reads", FastqGzPairedEnd(), position=8, doc="READ1 [READ2]"),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Tsv, selector="fusions.tsv"),
            ToolOutput(
                "out_discarded",
                Tsv,
                selector="fusions.discarded.tsv",
            ),
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 4, 22),
            dateUpdated=datetime(2021, 4, 22),
            documentation="",
        )
