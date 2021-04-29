# grep ^@SQ reference.dict | cut -f2,3 | sed 's/SN://' | sed 's/LN://'
import os
from datetime import datetime
from typing import List, Dict, Any

from janis_core import TOutput, File, Filename, OutputDocumentation
from janis_core.tool.test_classes import TTestCase
from janis_unix import TextFile

from janis_bioinformatics.data_types import FastaDict
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool
from janis_bioinformatics.tools import BioinformaticsTool


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
        self.metadata.dateCreated = datetime(2020, 7, 21)
        self.metadata.dateUpdated = datetime(2020, 6, 2)
        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.documentation = """\
Generate --genome FILE for BedToolsCoverage      
        """

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                },
                output=TextFile.basic_test("out", 15, "chr17\t83257441\n", 1),
            ),
            TTestCase(
                name="minimal",
                input={
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                },
                output=self.minimal_test(),
            ),
        ]
