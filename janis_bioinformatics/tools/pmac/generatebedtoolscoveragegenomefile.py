# grep ^@SQ reference.dict | cut -f2,3 | sed 's/SN://' | sed 's/LN://'

from datetime import datetime
from typing import List, Dict, Any

from janis_core import TOutput, File, Filename, OutputDocumentation
from janis_unix import TextFile

from janis_bioinformatics.data_types import FastaDict
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool


class GenerateGenomeFileForBedtoolsCoverage(BioinformaticsPythonTool):
    @staticmethod
    def code_block(
        reference: FastaDict, output_filename: str = "genome_file.txt"
    ) -> Dict[str, Any]:
        """
        :param reference: Reference file to generate genome for (must have ^.dict) pattern
        :param output_filename: Filename to output to
        """
        from re import sub

        ref_dict = sub("\.fa(sta)?$", ".dict", reference)

        with open(ref_dict) as inp, open(output_filename, "w+") as out:
            for line in inp:
                if not line.startswith("@SQ"):
                    continue
                pieces = line.split("\t")
                chrom = pieces[1].replace("SN:", "")
                length = pieces[2].replace("LN:", "")

                out.write(f"{chrom}\t{length}\n")

            return {"out": output_filename}

    def outputs(self) -> List[TOutput]:
        return [
            TOutput(
                "out",
                TextFile,
                doc=OutputDocumentation(doc="Genome file for BedToolsCoverage"),
            )
        ]

    def id(self) -> str:
        return "GenerateGenomeFileForBedtoolsCoverage"

    def friendly_name(self) -> str:
        return "Generate genome for BedtoolsCoverage"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.dateUpdated = datetime(2020, 6, 2)
        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.documentation = """\
Generate --genome FILE for BedToolsCoverage      
        """
