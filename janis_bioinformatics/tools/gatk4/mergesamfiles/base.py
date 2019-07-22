from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    String,
    ToolOutput,
    Array,
    File,
    Int,
    Boolean,
    InputSelector,
    CaptureType,
)
from janis_core import get_value_for_hints_and_ordered_resource_tuple
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import FastaWithDict, BamBai
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
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 16,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 32,
            CaptureType.THREEHUNDREDX: 32,
        },
    )
]


class Gatk4MergeSamFilesBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MergeSamFiles"

    @staticmethod
    def tool():
        return "Gatk4MergeSamFiles"

    def friendly_name(self):
        return "GATK4: Merge SAM Files"

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
                "bams",
                Array(BamBai()),
                prefix="-I",
                doc="The SAM/BAM file to sort.",
                position=10,
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".bam"),
                position=10,
                prefix="-O",
                doc="SAM/BAM file to write merged result to",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [ToolOutput("out", BamBai(), glob=InputSelector("outputFilename"))]

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
            keywords=["gatk", "gatk4", "broad", "merge", "sam"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/4.beta.3/org_broadinstitute_hellbender_tools_picard_sam_MergeSamFiles.php",
            documentation="Merges multiple SAM/BAM files into one file",
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
            "assumeSorted",
            Boolean(optional=True),
            prefix="-AS",
            doc="If true, assume that the input files are in the same sort order as the requested "
            "output sort order, even if their headers say otherwise.",
        ),
        ToolInput(
            "comment",
            Array(String(), optional=True),
            prefix="-CO",
            doc="Comment(s) to include in the merged output file's header.",
        ),
        ToolInput(
            "mergeSequenceDictionaries",
            Boolean(optional=True),
            prefix="-MSD",
            doc="Merge the sequence dictionaries",
        ),
        ToolInput(
            "sortOrder",
            String(optional=True),
            prefix="-SO",
            position=10,
            doc="The --SORT_ORDER argument is an enumerated type (SortOrder), which can have one of "
            "the following values: [unsorted, queryname, coordinate, duplicate, unknown]",
        ),
        ToolInput(
            "useThreading",
            Boolean(optional=True),
            prefix="--USE_THREADING",
            doc="Option to create a background thread to encode, compress and write to disk the output file. "
            "The threaded version uses about 20% more CPU and decreases runtime by "
            "~20% when writing out a compressed BAM file.",
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
            "reference",
            FastaWithDict(optional=True),
            prefix="--reference",
            position=11,
            doc="Reference sequence file.",
        ),
        ToolInput(
            "tmpDir",
            String(optional=True),
            prefix="--TMP_DIR",
            position=11,
            default="/tmp/",
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
