import os
import operator
from abc import ABC

from janis_core import (
    ToolInput,
    Filename,
    File,
    Int,
    String,
    Boolean,
    ToolOutput,
    Array,
    InputSelector,
    WildcardSelector,
    Stdout,
)
from janis_unix import TextFile
from janis_bioinformatics.data_types.bam import BamBai
from janis_bioinformatics.tools.samtools.samtoolstoolbase import SamToolsToolBase
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata
from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)


class SamToolsMpileupBase(SamToolsToolBase, ABC):
    def tool(self):
        return "SamToolsMpileup"

    @classmethod
    def samtools_command(cls):
        return "mpileup"

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput("bam", BamBai(), position=10),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(TextFile))]

    def friendly_name(self):
        return "SamTools: Mpileup"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 5, 19),
            dateUpdated=date(2020, 5, 19),
            institution="Samtools",
            doi=None,
            citation=None,
            keywords=["samtools", "mpileup"],
            documentationUrl="http://www.htslib.org/doc/samtools-mpileup.html",
            documentation="""Generate text pileup output for one or multiple BAM files. Each input file produces a separate group of pileup columns in the output.

Samtools mpileup can still produce VCF and BCF output (with -g or -u), but this feature is deprecated and will be removed in a future release. Please use bcftools mpileup for this instead. (Documentation on the deprecated options has been removed from this manual page, but older versions are available online at <http://www.htslib.org/doc/>.)

Note that there are two orthogonal ways to specify locations in the input file; via -r region and -l file. The former uses (and requires) an index to do random access while the latter streams through the file contents filtering out the specified regions, requiring no index. The two may be used in conjunction. For example a BED file containing locations of genes in chromosome 20 could be specified using -r 20 -l chr20.bed, meaning that the index is used to find chromosome 20 and then it is filtered for the regions listed in the bed file.""".strip(),
        )

    additional_inputs = [
        ToolInput(
            "illuminaEncoding",
            Boolean(optional=True),
            prefix="--illumina1.3+",
            doc="Assume the quality is in the Illumina 1.3+ encoding.",
        ),
        ToolInput(
            "countOrphans",
            Boolean(optional=True),
            prefix="--count-orphans",
            doc="do not discard anomalous read pairs",
        ),
        # Not sure this would load the
        # ToolInput("bamList", File(optional=True), prefix="--bam-list", doc="list of input BAM filenames, one per line")
        ToolInput(
            "noBAQ",
            Boolean(optional=True),
            prefix="--no-BAQ",
            doc="disable BAQ (per-Base Alignment Quality)",
        ),
        ToolInput(
            "adjustMQ",
            Int(optional=True),
            prefix="--adjust-MQ",
            doc="adjust mapping quality; recommended:50, disable:0 [0]",
        ),
        ToolInput(
            "maxDepth",
            Int(optional=True),
            prefix="--max-depth",
            doc="max per-file depth; avoids excessive memory usage [8000]",
        ),
        ToolInput(
            "redoBAQ",
            Boolean(optional=True),
            prefix="--redo-BAQ",
            doc="recalculate BAQ on the fly, ignore existing BQs",
        ),
        ToolInput(
            "fastaRef",
            File(optional=True),
            prefix="--fasta-ref",
            doc=" skip unlisted positions (chr pos) or regions (BED)",
        ),
        ToolInput(
            "excludeRG",
            File(optional=True),
            prefix="--exclude-RG",
            doc="exclude read groups listed in FILE",
        ),
        ToolInput(
            "positions",
            File(optional=True),
            prefix="--positions",
            doc="skip unlisted positions (chr pos) or regions (BED)",
        ),
        ToolInput(
            "minBQ",
            Int(optional=True),
            prefix="--min-BQ",
            doc="Minimum base quality for a base to be considered [13]",
        ),
        ToolInput(
            "minMQ",
            Int(optional=True),
            prefix="--min-MQ",
            doc="skip alignments with mapQ smaller than INT [0]",
        ),
        ToolInput(
            "region",
            String(optional=True),
            prefix="--region",
            doc="region in which pileup is generated",
        ),
        ToolInput(
            "ignoreRG",
            Boolean(optional=True),
            prefix="--ignore-RG",
            doc="ignore RG tags (one BAM = one sample)",
        ),
        ToolInput(
            "inclFlags",
            String(optional=True),
            prefix="--incl-flags",
            doc="required flags: skip reads with mask bits unset []",
        ),
        ToolInput(
            "exclFlags",
            String(optional=True),
            prefix="--excl-flags",
            doc="filter flags: skip reads with mask bits set [UNMAP,SECONDARY,QCFAIL,DUP]",
        ),
        ToolInput(
            "ignoreOverlaps",
            Boolean(optional=True),
            prefix="--ignore-overlaps",
            doc="disable read-pair overlap detection",
        ),
        ToolInput(
            "outputBP",
            Boolean(optional=True),
            prefix="--output-BP",
            doc="output base positions on reads",
        ),
        ToolInput(
            "outputMQ",
            Boolean(optional=True),
            prefix="--output-MQ",
            doc="output mapping quality",
        ),
        ToolInput(
            "outputQNAME",
            Boolean(optional=True),
            prefix="--output-QNAME",
            doc="output read names",
        ),
        ToolInput(
            "allPositions",
            Boolean(optional=True),
            prefix="-a",
            doc="output all positions (including zero depth)",
        ),
        ToolInput(
            "absolutelyAllPositions",
            Boolean(optional=True),
            doc="output absolutely all positions, including unused ref. sequences",
        ),
        ToolInput(
            "reference",
            File(optional=True),
            prefix="--reference",
            doc="Reference sequence FASTA FILE [null]",
        ),
    ]

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "bam": os.path.join(
                        BioinformaticsTool.test_data_path(), "small.bam"
                    ),
                },
                output=[
                    TTestExpectedOutput(
                        tag="out",
                        preprocessor=TTestPreprocessor.FileMd5,
                        operator=operator.eq,
                        expected_value="6b6f2401df9965b5250f4752dde03f2a",
                    ),
                    TTestExpectedOutput(
                        tag="out",
                        preprocessor=TTestPreprocessor.FileContent,
                        operator=operator.contains,
                        expected_value="17:43044045-43125733\t5\tN\t15\tCCCCCCCCCCCCCCC\tJDDAJDEDCDJD>gB\n",
                    ),
                    TTestExpectedOutput(
                        tag="out",
                        preprocessor=TTestPreprocessor.LineCount,
                        operator=operator.eq,
                        expected_value=81689,
                    ),
                ],
            )
        ]
