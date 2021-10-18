from datetime import datetime

from janis_core import (
    ToolInput,
    File,
    Boolean,
    String,
    Int,
    ToolMetadata,
    UnionType,
    InputSelector,
    StringFormatter,
    ToolOutput,
)
from janis_unix import Tsv
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_bioinformatics.data_types import Bam, BamBai, Bed, Fasta


class RNASeqQCBase(BioinformaticsTool):
    def friendly_name(self) -> str:
        return "RNASeqQC"

    def tool_provider(self):
        return "RNASeqQC"

    def tool(self) -> str:
        return "RNASeqQC"

    def base_command(self):
        return ["rnaseqc"]

    def inputs(self):
        return [
            ToolInput(
                "gtf",
                File,
                position=1,
                doc="The input GTF file containing features to check the bam against",
            ),
            ToolInput(
                "bam",
                BamBai,
                position=2,
                doc="The input SAM/BAM file containing reads to process",
            ),
            ToolInput(
                "output_dir",
                String(optional=True),
                position=3,
                default=".",
                doc="Output directory",
            ),
            ToolInput(
                "sample",
                String(optional=True),
                position=4,
                prefix="--sample",
                doc="The name of the current sample. Default: The bam's filename",
            ),
            ToolInput(
                "bed",
                Bed(optional=True),
                position=4,
                prefix="--bed",
                doc="Optional input BED file containing non-overlapping exons used for fragment size calculations",
            ),
            ToolInput(
                "fasta",
                Fasta(optional=True),
                position=4,
                prefix="--fasta",
                doc="Optional input FASTA/FASTQ file containing the reference sequence used for parsing CRAM files",
            ),
            ToolInput(
                "chimeric_distance",
                Int(optional=True),
                position=4,
                prefix="--chimeric-distance",
                doc="Set the maximum accepted distance between read mates. Mates beyond this distance will be counted as chimeric pairs. Default: 2000000 [bp]",
            ),
            ToolInput(
                "fragment_samples",
                Int(optional=True),
                position=4,
                prefix="--fragment-samples",
                doc="Set the number of samples to take when computing fragment sizes. Requires the --bed argument. Default: 1000000",
            ),
            ToolInput(
                "mapping_quality",
                Int(optional=True),
                position=4,
                prefix="--mapping-quality",
                doc="Set the lower bound on read quality for exon coverage counting. Reads below this number are excluded from coverage metrics. Default: 255",
            ),
            ToolInput(
                "base_mismatch",
                Int(optional=True),
                position=4,
                prefix="--base-mismatch",
                doc="Set the maximum number of allowed mismatches between a read and the reference sequence. Reads with more than this number of mismatches are excluded from coverage metrics. Default: 6",
            ),
            ToolInput(
                "offset",
                Int(optional=True),
                position=4,
                prefix="--offset",
                doc=" Set the offset into the gene for the 3' and 5' windows in bias calculation. A positive value shifts the 3' and 5' windows towards eachother, while a negative value shifts them apart. Default: 150 [bp]",
            ),
            ToolInput(
                "window_size",
                Int(optional=True),
                position=4,
                prefix="--window-size",
                doc="Set the size of the 3' and 5' windows in bias calculation. Default: 100 [bp]",
            ),
            ToolInput(
                "gene_length",
                Int(optional=True),
                position=4,
                prefix="--gene-length",
                doc="Set the minimum size of a gene for bias calculation. Genes below this size are ignored in the calculation. Default: 600 [bp]",
            ),
            ToolInput(
                "legacy",
                Boolean(optional=True),
                position=4,
                prefix="--legacy",
                doc="Use legacy counting rules. Gene and exon counts match output of RNA-SeQC 1.1.9",
            ),
            ToolInput(
                "stranded",
                String(optional=True),
                position=4,
                prefix="--stranded",
                doc="Use strand-specific metrics. Only features on the same strand of a read will be considered. Allowed values are 'RF', 'rf', 'FR', and 'fr'",
            ),
            ToolInput(
                "verbose",
                Boolean(optional=True),
                position=4,
                prefix="--verbose",
                doc="Give some feedback about what's going on. Supply this argument twice for progress updates while parsing the bam",
            ),
            ToolInput(
                "tag",
                String(optional=True),
                position=4,
                prefix="--tag",
                doc="Filter out reads with the specified tag.",
            ),
            ToolInput(
                "chimeric_tag",
                String(optional=True),
                position=4,
                prefix="--chimeric-tag",
                doc="Reads maked with the specified tag will be labeled as Chimeric. Defaults to 'mC' for STAR",
            ),
            ToolInput(
                "exclude_chimeric",
                Boolean(optional=True),
                position=4,
                prefix="--exclude-chimeric",
                doc="Exclude chimeric reads from the read counts",
            ),
            ToolInput(
                "unpaired",
                Boolean(optional=True),
                position=4,
                prefix="--unpaired",
                doc="Allow unpaired reads to be quantified. Required for single-end libraries",
            ),
            ToolInput(
                "rpkm",
                Boolean(optional=True),
                position=4,
                prefix="--rpkm",
                doc="Output gene RPKM values instead of TPMs",
            ),
            ToolInput(
                "coverage",
                Boolean(optional=True),
                position=4,
                prefix="--coverage",
                doc="If this flag is provided, coverage statistics for each transcript will be written to a table. Otherwise, only summary coverage statistics are generated and added to the metrics table",
            ),
            ToolInput(
                "coverage_mask",
                Int(optional=True),
                position=4,
                prefix="--coverage-mask",
                doc="Sets how many bases at both ends of a transcript are masked out when computing per-base exon coverage. Default: 500bp",
            ),
            ToolInput(
                "detection_threshold",
                Int(optional=True),
                position=4,
                prefix="--detection-threshold",
                doc="Number of counts on a gene to consider the gene 'detected'. Additionally, genes below this limit are excluded from 3' bias computation. Default: 5 reads",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "gene_fragments",
                File,
                glob=StringFormatter(
                    "{output_dir}/{sample}.gene_fragments.gct",
                    output_dir=InputSelector("output_dir"),
                    sample=InputSelector("sample"),
                ),
            ),
            ToolOutput(
                "gene_reads",
                File,
                glob=StringFormatter(
                    "{output_dir}/{sample}.gene_reads.gct",
                    output_dir=InputSelector("output_dir"),
                    sample=InputSelector("sample"),
                ),
            ),
            ToolOutput(
                "gene_tpm",
                File,
                glob=StringFormatter(
                    "{output_dir}/{sample}.gene_tpm.gct",
                    output_dir=InputSelector("output_dir"),
                    sample=InputSelector("sample"),
                ),
            ),
            ToolOutput(
                "metrics",
                Tsv,
                glob=StringFormatter(
                    "{output_dir}/{sample}.metrics.tsv",
                    output_dir=InputSelector("output_dir"),
                    sample=InputSelector("sample"),
                ),
            ),
            ToolOutput(
                "coverage",
                Tsv(optional=True),
                glob=StringFormatter(
                    "{output_dir}/{sample}.coverage.tsv",
                    output_dir=InputSelector("output_dir"),
                    sample=InputSelector("sample"),
                ),
            ),
            ToolOutput(
                "exon_reads",
                File,
                glob=StringFormatter(
                    "{output_dir}/{sample}.exon_reads.gct",
                    output_dir=InputSelector("output_dir"),
                    sample=InputSelector("sample"),
                ),
            ),
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 9, 10),
            dateUpdated=datetime(2021, 9, 10),
            documentationUrl="https://github.com/getzlab/rnaseqc",
            documentation="""Usage: rnaseqc [gtf] [bam] [output] \{OPTIONS\}
""",
        )
