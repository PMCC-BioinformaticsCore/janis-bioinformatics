from abc import ABC

from janis_core import (
    ToolInput,
    String,
    Boolean,
    File,
    Filename,
    Array,
    Int,
    ToolOutput,
    InputSelector,
)
from janis_bioinformatics.data_types import FastaWithDict, CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.bcftools.bcftoolstoolbase import BcfToolsToolBase
from janis_core import ToolMetadata


class BcfToolsConcatBase(BcfToolsToolBase, ABC):
    def tool(self):
        return "bcftoolsConcat"

    def friendly_name(self):
        return "BCFTools: Concat"

    def base_command(self):
        return ["bcftools", "concat"]

    def inputs(self):
        return [
            ToolInput("vcf", Array(CompressedVcf()), position=15),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf.gz"),
                prefix="-o",
                doc="--output: When output consists of a single stream, "
                "write it to FILE rather than to standard output, where it is written by default.",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput("out", CompressedVcf(), glob=InputSelector("outputFilename"))
        ]

    def bind_metadata(self):
        from datetime import date

        self.metadata.dateUpdated = date(2019, 9, 9)
        self.metadata.doi = "http://www.ncbi.nlm.nih.gov/pubmed/19505943"
        self.metadata.citation = (
            "Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R, "
            "and 1000 Genome Project Data Processing Subgroup, The Sequence alignment/map (SAM) "
            "format and SAMtools, Bioinformatics (2009) 25(16) 2078-9"
        )
        self.metadata.documentationUrl = (
            "https://samtools.github.io/bcftools/bcftools.html#concat"
        )
        self.metadata.documentation = """
Concatenate or combine VCF/BCF files. All source files must have the same sample
columns appearing in the same order. The program can be used, for example, to
concatenate chromosome VCFs into one VCF, or combine a SNP VCF and an indel
VCF into one. The input files must be sorted by chr and position. The files
must be given in the correct order to produce sorted VCF on output unless
the -a, --allow-overlaps option is specified. With the --naive option, the files
are concatenated without being recompressed, which is very fast but dangerous
if the BCF headers differ.
"""

    additional_args = [
        ToolInput(
            "allowOverLaps",
            Boolean(optional=True),
            prefix="-a",
            doc="First coordinate of the next file can precede last record of the current file.",
        ),
        ToolInput(
            "compactPS",
            Boolean(optional=True),
            prefix="-c",
            doc="Do not output PS tag at each site, only at the start of a new phase set block.",
        ),
        ToolInput(
            "rmDups",
            String(optional=True),
            prefix="-d",
            doc="Output duplicate records present in multiple files only once: <snps|indels|both|all|none>",
        ),
        ToolInput(
            "rmDupsNone", Boolean(optional=True), prefix="-d", doc="Alias for -d none"
        ),
        ToolInput(
            "fileList",
            File(optional=True),
            prefix="-f",
            doc="Read the list of files from a file.",
        ),
        ToolInput(
            "ligate",
            Boolean(optional=True),
            prefix="-l",
            doc="Ligate phased VCFs by matching phase at overlapping haplotypes",
        ),
        ToolInput(
            "noVersion",
            Boolean(optional=True),
            prefix="--no-version",
            doc="Do not append version and command line information to the output VCF header.",
        ),
        ToolInput(
            "naive",
            Boolean(optional=True),
            prefix="-n",
            doc="Concatenate files without recompression (dangerous, use with caution)",
        ),
        ToolInput(
            "outputType",
            String(optional=True),
            prefix="-O",
            default="z",
            doc="--output-type b|u|z|v: Output compressed BCF (b), uncompressed BCF (u), "
            "compressed VCF (z), uncompressed VCF (v). Use the -Ou option when piping "
            "between bcftools subcommands to speed up performance by removing "
            "unnecessary compression/decompression and VCF←→BCF conversion.",
        ),
        ToolInput(
            "minPG",
            Int(optional=True),
            prefix="-q",
            doc="Break phase set if phasing quality is lower than <int> [30]",
        ),
        ToolInput(
            "regions",
            String(optional=True),
            prefix="-r",
            doc="--regions chr|chr:pos|chr:from-to|chr:from-[,…]: Comma-separated list of regions, "
            "see also -R, --regions-file. Note that -r cannot be used in combination with -R.",
        ),
        ToolInput(
            "regionsFile",
            File(optional=True),
            prefix="-R",
            doc="--regions-file: Regions can be specified either on command line or in a VCF, BED, or "
            "tab-delimited file (the default). The columns of the tab-delimited file are: CHROM, POS, "
            "and, optionally, POS_TO, where positions are 1-based and inclusive. The columns of the "
            "tab-delimited BED file are also CHROM, POS and POS_TO (trailing columns are ignored), "
            "but coordinates are 0-based, half-open. To indicate that a file be treated as BED rather "
            "than the 1-based tab-delimited file, the file must have the '.bed' or '.bed.gz' suffix "
            "(case-insensitive). Uncompressed files are stored in memory, while bgzip-compressed and "
            "tabix-indexed region files are streamed. Note that sequence names must match exactly, 'chr20'"
            " is not the same as '20'. Also note that chromosome ordering in FILE will be respected, "
            "the VCF will be processed in the order in which chromosomes first appear in FILE. "
            "However, within chromosomes, the VCF will always be processed in ascending genomic coordinate "
            "order no matter what order they appear in FILE. Note that overlapping regions in FILE can "
            "result in duplicated out of order positions in the output. This option requires indexed "
            "VCF/BCF files. Note that -R cannot be used in combination with -r.",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            prefix="--threads",
            doc="Number of output compression threads to use in addition to main thread. "
            "Only used when --output-type is b or z. Default: 0.",
        ),
    ]
