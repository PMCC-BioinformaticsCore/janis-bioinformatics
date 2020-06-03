from datetime import datetime
from typing import List, Dict, Any

from janis_core import TOutput, File, Filename, OutputDocumentation

from janis_bioinformatics.data_types import FastaDict
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool


class GenerateVardictHeaderLines(BioinformaticsPythonTool):
    @staticmethod
    def code_block(
        reference: FastaDict, output_filename: str = "output.txt"
    ) -> Dict[str, Any]:
        """
        :param reference: Reference file to generate vardict header lines for (must have ^.dict) pattern
        :param output_filename: Filename to output to
        """
        from re import sub

        ref_dict = sub("\.fa(sta)?$", ".dict", reference)

        with open(output_filename, "w+") as out, open(ref_dict) as inp:
            out.write("##source=vardict\n")
            for line in inp:
                if not line.startswith("@SQ"):
                    continue
                pieces = line.split("\t")
                chrom = pieces[1].replace("SN:", "")
                length = pieces[2].replace("LN:", "")

                out.write(f"##contig=<ID={chrom},length={length}>\n")

            return {"out": output_filename}

    def outputs(self) -> List[TOutput]:
        return [
            TOutput(
                "out",
                File,
                doc=OutputDocumentation(
                    doc="Header file for VarDict, generated based on the reference index"
                ),
            )
        ]

    def id(self) -> str:
        return "GenerateVardictHeaderLines"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.dateUpdated = datetime(2020, 6, 2)
        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.documentation = """\
Generate VarDict Headerlines.       
        """
