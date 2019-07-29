from typing import List, Dict, Any
from janis_core import get_value_for_hints_and_ordered_resource_tuple
from janis_bioinformatics.data_types import FastaWithDict
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import (
    ToolOutput,
    ToolInput,
    Filename,
    ToolArgument,
    InputSelector,
    CaptureType,
)


CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 1,
            CaptureType.EXOME: 1,
            CaptureType.THIRTYX: 1,
            CaptureType.NINETYX: 1,
            CaptureType.THREEHUNDREDX: 1,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 8,
            CaptureType.EXOME: 8,
            CaptureType.THIRTYX: 8,
            CaptureType.NINETYX: 12,
            CaptureType.THREEHUNDREDX: 16,
        },
    )
]


class SplitMultiAllele(BioinformaticsTool):
    @staticmethod
    def tool():
        return "SplitMultiAllele"

    @staticmethod
    def tool_provider():
        return "Peter MacCallum Cancer Centre"

    def friendly_name(self):
        return "Split Multiple Alleles"

    @staticmethod
    def base_command():
        return None

    @staticmethod
    def container():
        return "heuermh/vt"  # "SEE (mfranklin's notes in) DOCUMENTATION"

    @staticmethod
    def version():
        return "v0.5772"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 1

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("vcf", Vcf(), position=2, shell_quote=False),
            ToolInput(
                "reference", FastaWithDict(), prefix="-r", position=7, shell_quote=False
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf", suffix=".norm"),
                prefix=">",
                position=10,
                shell_quote=False,
            ),
        ]

    def arguments(self):
        return [
            ToolArgument(
                "sed 's/ID=AD,Number=./ID=AD,Number=R/' <",
                position=1,
                shell_quote=False,
            ),
            ToolArgument("|", position=3, shell_quote=False),
            ToolArgument("vt decompose -s - -o -", position=4, shell_quote=False),
            ToolArgument("|", position=5, shell_quote=False),
            ToolArgument("vt normalize -n -q - -o -", position=6, shell_quote=False),
            ToolArgument("|", position=8, shell_quote=False),
            ToolArgument(
                "sed 's/ID=AD,Number=./ID=AD,Number=1/'", position=9, shell_quote=False
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Vcf(), glob=InputSelector("outputFilename"))]

    def doc(self):
        return """
    VcfSplitMultiAllele.sh
    
    Currently stored at: '/researchers/jiaan.yu/WGS_pipeline/VcfSplitMultiAllele.sh’
    
    This CommandTool is an attempt to translate the shell script as a CommandTool.
    
    It uses the commands 'sed' and 'vt' (where $0: input, $1: output) as the following:
    
        > sed 's/ID=AD,Number=./ID=AD,Number=R/' < $1       |\
            vt decompose -s - -o -                          |\
            vt normalize -n -q - -o - -r $HumanREF          |\
            sed 's/ID=AD,Number=./ID=AD,Number=1/' > $2
    
    ========
    
    SED documentation:
        Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...
        
          -n, --quiet, --silent
                         suppress automatic printing of pattern space
          -e script, --expression=script
                         add the script to the commands to be executed
          -f script-file, --file=script-file
                         add the contents of script-file to the commands to be executed
          --follow-symlinks
                         follow symlinks when processing in place
          -i[SUFFIX], --in-place[=SUFFIX]
                         edit files in place (makes backup if SUFFIX supplied)
          -c, --copy
                         use copy instead of rename when shuffling files in -i mode
          -b, --binary
                         does nothing; for compatibility with WIN32/CYGWIN/MSDOS/EMX (
                         open files in binary mode (CR+LFs are not treated specially))
          -l N, --line-length=N
                         specify the desired line-wrap length for the `l' command
          --posix
                         disable all GNU extensions.
          -r, --regexp-extended
                         use extended regular expressions in the script.
          -s, --separate
                         consider files as separate rather than as a single continuous
                         long stream.
          -u, --unbuffered
                         load minimal amounts of data from the input files and flush
                         the output buffers more often
          -z, --null-data
                         separate lines by NUL characters
          --help
                         display this help and exit
          --version
                         output version information and exit
        
        If no -e, --expression, -f, or --file option is given, then the first
        non-option argument is taken as the sed script to interpret.  All
        remaining arguments are names of input files; if no input files are
        specified, then the standard input is read.
        
        GNU sed home page: <http://www.gnu.org/software/sed/>.
        General help using GNU software: <http://www.gnu.org/gethelp/>.
        
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
              -?  displays help 
        """.strip()


if __name__ == "__main__":
    print(SplitMultiAllele().help())
