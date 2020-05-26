from typing import List

from janis_bioinformatics.data_types import Vcf, FastaWithDict, CompressedVcf
from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import (
    ToolOutput,
    ToolInput,
    Filename,
    ToolArgument,
    InputSelector,
)


class SplitMultiAlleleNormaliseVcf(BioinformaticsTool):
    def tool(self):
        return "SplitMultiAlleleNormaliseVcf"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def friendly_name(self):
        return "Split Multiple Alleles and Normalise Vcf"

    def base_command(self):
        return None

    def container(self):
        return "heuermh/vt"

    def version(self):
        return "v0.5772"

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("vcf", Vcf(optional=True), position=1, shell_quote=False),
            ToolInput(
                "compressedVcf",
                CompressedVcf(optional=True),
                position=1,
                shell_quote=False,
            ),
            ToolInput(
                "reference", FastaWithDict(), prefix="-r", position=4, shell_quote=False
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf.gz", suffix=".norm"),
                position=6,
                prefix="-o",
                shell_quote=False,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("out", CompressedVcf(), glob=InputSelector("outputFilename"))
        ]

    def arguments(self):
        return [
            ToolArgument("vt decompose -s ", position=0, shell_quote=False),
            ToolArgument("| vt normalize -n -q - ", position=2, shell_quote=False),
        ]

    def doc(self):
        return """Use vt to split multiallelic variants, and left-most align normalisation.
        Original command:
        vt decompose -s $input.vcf | vt normalize -n -q - -r $reference -o $output.vcf
            VT decompose documentation:
        options : -s  smart decomposition [false]
              -d  debug [false]
              -f  filter expression []
              -o  output VCF file [-]
              -I  file containing list of intervals []
              -i  intervals []
              -?  displays help
              
    VT normalize documentation:
        options : -o  output VCF file [-]
              -d  debug [false]
              -q  do not print options and summary [false]
              -m  warns but does not exit when REF is inconsistent
                  with masked reference sequence for non SNPs.
                  This overides the -n option [false]
              -n  warns but does not exit when REF is inconsistent
                  with reference sequence for non SNPs [false]
              -f  filter expression []
              -w  window size for local sorting of variants [10000]
              -I  file containing list of intervals []
              -i  intervals []
              -r  reference sequence fasta file []
              -?  displays help """.strip()
