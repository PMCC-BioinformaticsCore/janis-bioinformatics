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
                .joined(" "),
                shell_quote=False,
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


class Jaffa_2_0(JaffaBase):
    def container(self) -> str:
        return "beccyl/jaffa:2.0"

    def version(self) -> str:
        return "v2.0"


if __name__ == "__main__":
    j = Jaffa_2_0()
    j.translate("wdl")
