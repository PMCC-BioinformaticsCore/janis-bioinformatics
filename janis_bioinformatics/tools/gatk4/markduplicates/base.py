from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    File,
    Array,
    String,
    Int,
    Boolean,
    InputSelector,
    CaptureType,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
)
from janis_unix import Tsv

from janis_bioinformatics.data_types import BamBai
from ..gatk4toolbase import Gatk4ToolBase

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
            CaptureType.CHROMOSOME: 64,
            CaptureType.EXOME: 64,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4MarkDuplicatesBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MarkDuplicates"

    @staticmethod
    def tool():
        return "Gatk4MarkDuplicates"

    def friendly_name(self):
        return "GATK4: Mark Duplicates"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

    def inputs(self):
        return [
            ToolInput(
                "bam",
                BamBai(),
                prefix="-I",
                position=10,
                doc="One or more input SAM or BAM files to analyze. Must be coordinate sorted.",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".bam"),
                position=10,
                prefix="-O",
                doc="File to write duplication metrics to",
            ),
            ToolInput(
                "metricsFilename",
                Filename(extension=".metrics.txt"),
                position=10,
                prefix="-M",
                doc="The output file to write marked records to.",
            ),
            *super(Gatk4MarkDuplicatesBase, self).inputs(),
            *self.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput("out", BamBai(), glob=InputSelector("outputFilename")),
            ToolOutput("metrics", Tsv(), glob=InputSelector("metricsFilename")),
        ]

    def metadata(self):
        from datetime import date

        return ToolMetadata(
            creator="Michael Franklin",
            maintainer="Michael Franklin",
            maintainerEmail="michael.franklin@petermac.org",
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 1, 24),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "mark", "duplicates"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/current/picard_sam_markduplicates_MarkDuplicates.php",
            documentation="""MarkDuplicates (Picard): Identifies duplicate reads.

This tool locates and tags duplicate reads in a BAM or SAM file, where duplicate reads are 
defined as originating from a single fragment of DNA. Duplicates can arise during sample 
preparation e.g. library construction using PCR. See also EstimateLibraryComplexity for 
additional notes on PCR duplication artifacts. Duplicate reads can also result from a single 
amplification cluster, incorrectly detected as multiple clusters by the optical sensor of the 
sequencing instrument. These duplication artifacts are referred to as optical duplicates.

The MarkDuplicates tool works by comparing sequences in the 5 prime positions of both reads 
and read-pairs in a SAM/BAM file. An BARCODE_TAG option is available to facilitate duplicate
marking using molecular barcodes. After duplicate reads are collected, the tool differentiates 
the primary and duplicate reads using an algorithm that ranks reads by the sums of their 
base-quality scores (default method).

The tool's main output is a new SAM or BAM file, in which duplicates have been identified 
in the SAM flags field for each read. Duplicates are marked with the hexadecimal value of 0x0400, 
which corresponds to a decimal value of 1024. If you are not familiar with this type of annotation, 
please see the following blog post for additional information.

Although the bitwise flag annotation indicates whether a read was marked as a duplicate, 
it does not identify the type of duplicate. To do this, a new tag called the duplicate type (DT) 
tag was recently added as an optional output in the 'optional field' section of a SAM/BAM file. 
Invoking the TAGGING_POLICY option, you can instruct the program to mark all the duplicates (All), 
only the optical duplicates (OpticalOnly), or no duplicates (DontTag). The records within the 
output of a SAM/BAM file will have values for the 'DT' tag (depending on the invoked TAGGING_POLICY), 
as either library/PCR-generated duplicates (LB), or sequencing-platform artifact duplicates (SQ). 
This tool uses the READ_NAME_REGEX and the OPTICAL_DUPLICATE_PIXEL_DISTANCE options as the 
primary methods to identify and differentiate duplicate types. Set READ_NAME_REGEX to null to 
skip optical duplicate detection, e.g. for RNA-seq or other data where duplicate sets are 
extremely large and estimating library complexity is not an aim. Note that without optical 
duplicate counts, library size estimation will be inaccurate.

MarkDuplicates also produces a metrics file indicating the numbers 
of duplicates for both single- and paired-end reads.

The program can take either coordinate-sorted or query-sorted inputs, however the behavior 
is slightly different. When the input is coordinate-sorted, unmapped mates of mapped records 
and supplementary/secondary alignments are not marked as duplicates. However, when the input 
is query-sorted (actually query-grouped), then unmapped mates and secondary/supplementary 
reads are not excluded from the duplication test and can be marked as duplicate reads.

If desired, duplicates can be removed using the REMOVE_DUPLICATE and REMOVE_SEQUENCING_DUPLICATES options.""".strip(),
        )

    additional_args = [
        ToolInput(
            "argumentsFile",
            Array(File(), optional=True),
            prefix="--arguments_file",
            position=10,
            doc="read one or more arguments files and add them to the command line",
        ),
        ToolInput(
            "assumeSortOrder",
            String(optional=True),
            prefix="-ASO",
            doc="If not null, assume that the input file has this order even if the header says otherwise. "
            "Exclusion: This argument cannot be used at the same time as ASSUME_SORTED. "
            "The --ASSUME_SORT_ORDER argument is an enumerated type (SortOrder), which can have one of "
            "the following values: [unsorted, queryname, coordinate, duplicate, unknown]",
        ),
        ToolInput(
            "barcodeTag",
            String(optional=True),
            prefix="--BARCODE_TAG",
            doc="Barcode SAM tag (ex. BC for 10X Genomics)",
        ),
        ToolInput(
            "comment",
            Array(String(), optional=True),
            prefix="-CO",
            doc="Comment(s) to include in the output file's header.",
        ),
        ToolInput(
            "compressionLevel",
            Int(optional=True),
            prefix="--COMPRESSION_LEVEL",
            position=11,
            doc="Compression level for all compressed files created (e.g. BAM and GELI).",
        ),
        ToolInput(
            "createIndex",
            Boolean(optional=True),
            prefix="--CREATE_INDEX",
            position=11,
            doc="Whether to create a BAM index when writing a coordinate-sorted BAM file.",
        ),
        ToolInput(
            "createMd5File",
            Boolean(optional=True),
            prefix="--CREATE_MD5_FILE",
            position=11,
            doc="Whether to create an MD5 digest for any BAM or FASTQ files created.",
        ),
        ToolInput(
            "maxRecordsInRam",
            Int(optional=True),
            prefix="--MAX_RECORDS_IN_RAM",
            position=11,
            doc="When writing SAM files that need to be sorted, this will specify the number of "
            "records stored in RAM before spilling to disk. Increasing this number reduces "
            "the number of file handles needed to sort a SAM file, and increases the amount of RAM needed.",
        ),
        ToolInput(
            "quiet",
            Boolean(optional=True),
            prefix="--QUIET",
            position=11,
            doc="Whether to suppress job-summary info on System.err.",
        ),
        ToolInput(
            "tmpDir",
            String(optional=True),
            prefix="--TMP_DIR",
            position=11,
            default="tmp/",
            doc="Undocumented option",
        ),
        ToolInput(
            "useJdkDeflater",
            Boolean(optional=True),
            prefix="--use_jdk_deflater",
            position=11,
            doc="Whether to use the JdkDeflater (as opposed to IntelDeflater)",
        ),
        ToolInput(
            "useJdkInflater",
            Boolean(optional=True),
            prefix="--use_jdk_inflater",
            position=11,
            doc="Whether to use the JdkInflater (as opposed to IntelInflater)",
        ),
        ToolInput(
            "validationStringency",
            String(optional=True),
            prefix="--VALIDATION_STRINGENCY",
            position=11,
            doc="Validation stringency for all SAM files read by this program. Setting stringency to SILENT "
            "can improve performance when processing a BAM file in which variable-length data "
            "(read, qualities, tags) do not otherwise need to be decoded."
            "The --VALIDATION_STRINGENCY argument is an enumerated type (ValidationStringency), "
            "which can have one of the following values: [STRICT, LENIENT, SILENT]",
        ),
        ToolInput(
            "verbosity",
            String(optional=True),
            prefix="--verbosity",
            position=11,
            doc="The --verbosity argument is an enumerated type (LogLevel), which can have "
            "one of the following values: [ERROR, WARNING, INFO, DEBUG]",
        ),
    ]
