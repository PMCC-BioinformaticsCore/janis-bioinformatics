from datetime import datetime
from typing import List, Optional, Union

from janis_bioinformatics.data_types import Fasta, FastqGzPair, FastqPair
from janis_core import (
    ToolOutput,
    ToolInput,
    String,
    Array,
    Int,
    CpuSelector,
    WildcardSelector,
    File,
    ToolArgument,
    Directory,
    InputSelector,
    Metadata,
)

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


def BPipeToolInput(tag: str, datatype, prefix, **kwargs):
    return ToolInput(
        tag=tag,
        input_type=datatype,
        prefix=f"-p {prefix}=",
        shell_quote=False,
        separate_value_from_prefix=False,
        **kwargs,
    )


SCRIPT_POSITION = 2


class JaffaBase(BioinformaticsTool):
    def tool(self) -> str:
        return "Jaffa"

    def base_command(self) -> Optional[Union[str, List[str]]]:
        return ["bpipe", "run"]

    def arguments(self) -> Optional[List[ToolArgument]]:
        return [
            ToolArgument("/opt/JAFFA/JAFFA_direct.groovy", position=SCRIPT_POSITION),
            ToolArgument(
                InputSelector("fastqs", type_hint=Array(FastqPair))
                .flattened()
                .joined("' '"),
            ),
        ]

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "fastqs",
                Array(FastqPair),
                doc="Space separated, this gets bound using a ToolArgument",
            ),
            BPipeToolInput("genome", String, default="hg38", prefix="genome",),
            BPipeToolInput(
                "annotation", String, default="genCode22", prefix="annotation"
            ),
            BPipeToolInput("reference", Directory, prefix="refBase"),
            ToolInput(
                "threads", Int(optional=True), default=CpuSelector(), prefix="-n"
            ),
            BPipeToolInput(
                "readLayout",
                String,
                prefix="readLayout",
                default="paired",
                doc="paired | single | single-end",
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("out_reference", Fasta, selector=WildcardSelector("*.fasta"))
        ]

    def memory(self, hints):
        return 12

    def cpus(self, hints):
        return 8

    def friendly_name(self) -> str:
        return "Jaffa"

    def tool_provider(self):
        return "oshlack"

    def bind_metadata(self) -> Metadata:
        self.metadata.contributors = ["Michael Franklin"]
        self.metadata.dateCreated = datetime(2020, 12, 1)
        self.metadata.documentationUrl = "https://github.com/Oshlack/JAFFA/wiki"
        self.metadata.citation = "Davidson, N.M., Majewski, I.J. & Oshlack, A. JAFFA: High sensitivity transcriptome-focused fusion gene detection. Genome Med 7, 43 (2015). https://doi.org/10.1186/s13073-015-0167-x"
        self.metadata.doi = "https://doi.org/10.1186/s13073-015-0167-x"

        return self.metadata


class Jaffa_2_0(JaffaBase):
    def container(self) -> str:
        return "beccyl/jaffa:2.0"

    def version(self) -> str:
        return "v2.0"


if __name__ == "__main__":
    j = Jaffa_2_0()
    j.translate("wdl")
