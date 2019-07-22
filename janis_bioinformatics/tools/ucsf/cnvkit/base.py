from datetime import datetime
from typing import List

from janis_core import ToolOutput, ToolInput, Filename, File, String

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class CNVKitBase(BioinformaticsTool):
    @staticmethod
    def tool_provider():
        return "UCSF"

    @staticmethod
    def tool() -> str:
        return "CNVKit"

    def friendly_name(self) -> str:
        return "CNVKit"

    @staticmethod
    def base_command():
        return ["cnvkit.py", "batch"]

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "outputDirectory",
                Filename(),
                prefix="--output-dir",
                doc="DIRECTORY Output directory.",
            ),
            ToolInput(
                "reference",
                File(),
                prefix="--reference",
                doc="REFERENCE Copy number reference file (.cnn).",
            ),
            ToolInput(
                "method",
                String(optional=True),
                prefix="--method",
                doc="(-m) {hybrid,amplicon,wgs} Sequencing protocol: hybridization capture ('hybrid'), targeted amplicon sequencing ('amplicon'), or whole genome sequencing ('wgs'). Determines whether and how to use antitarget bins. [Default: hybrid]",
            ),
            ToolInput(
                "maleReference",
                String(optional=True),
                prefix="--male-reference",
                doc="(-y, --haploid-x-reference) Use or assume a male reference (i.e. female samples will have +1 log-CNR of chrX; otherwise male samples would have -1 chrX).",
            ),
            ToolInput(
                "countReads",
                String(optional=True),
                prefix="--count-reads",
                doc=" (-c) Get read depths by counting read midpoints within each bin. (An alternative algorithm).",
            ),
            ToolInput(
                "dropLowCoverage",
                String(optional=True),
                prefix="--drop-low-coverage",
                doc="Drop very-low-coverage bins before segmentation to avoid false-positive deletions in poor-quality tumor samples.",
            ),
            ToolInput(
                "processes",
                String(optional=True),
                prefix="--processes",
                doc="(-p) [PROCESSES] Number of subprocesses used to running each of the BAM files in parallel. Without an argument, use the maximum number of available CPUs. [Default: process each BAM in serial]",
            ),
            ToolInput(
                "rscriptPath",
                String(optional=True),
                prefix="--rscript-path",
                doc="Path to the Rscript excecutable to use for running R code. Use this option to specify a non-default R installation. [Default: Rscript]",
            ),
            # To construct a new copy number reference:
            #   -n [FILES [FILES ...]], --normal [FILES [FILES ...]] Normal samples (.bam) used to construct the pooled, paired, or flat reference. If this option is used but no filenames are given, a "flat" reference will be built. Otherwise, all filenames following this option will be used.
            #   -f FILENAME, --fasta FILENAME Reference genome, FASTA format (e.g. UCSC hg19.fa)
            #   -t FILENAME, --targets FILENAME Target intervals (.bed or .list)
            #   -a FILENAME, --antitargets FILENAME Antitarget intervals (.bed or .list)
            #   --annotate FILENAME   Use gene models from this file to assign names to the target regions. Format: UCSC refFlat.txt or ensFlat.txt file (preferred), or BED, interval list, GFF, or similar.
            #   --short-names         Reduce multi-accession bait labels to be short and consistent.
            #   --target-avg-size TARGET_AVG_SIZE Average size of split target bins (results are approximate).
            #   -g FILENAME, --access FILENAME Regions of accessible sequence on chromosomes (.bed), as output by the 'access' command.
            #   --antitarget-avg-size ANTITARGET_AVG_SIZE Average size of antitarget bins (results are approximate).
            #   --antitarget-min-size ANTITARGET_MIN_SIZE Minimum size of antitarget bins (smaller regions are dropped).
            #   --output-reference FILENAME Output filename/path for the new reference file being created. (If given, ignores the -o/--output-dir option and will write the file to the given path. Otherwise, "reference.cnn" will be created in the current directory or specified output directory.)
            #
            # To reuse an existing reference:
            #
            # Output options:
            #   -d DIRECTORY, --output-dir
            #   --scatter             Create a whole-genome copy ratio profile as a PDF scatter plot.
            #   --diagram             Create an ideogram of copy ratios on chromosomes as a PDF.
        ]

    def outputs(self) -> List[ToolOutput]:
        return []

    def metadata(self):
        self._metadata.dateCreated = datetime(2019, 7, 3)
        self._metadata.dateUpdated = datetime(2019, 7, 3)
        self._metadata.documentationUrl = "https://github.com/etal/cnvkit"
        self._metadata.documentation = """
        A command-line toolkit and Python library for detecting copy number variants 
        and alterations genome-wide from high-throughput sequencing."""

        self._metadata.doi = "10.1371/journal.pcbi.1004873"
        self._metadata.citation = (
            "Talevich, E., Shain, A.H., Botton, T., & Bastian, B.C. (2014). "
            "CNVkit: Genome-wide copy number detection and visualization from targeted "
            "sequencing. PLOS Computational Biology 12(4):e1004873"
        )
