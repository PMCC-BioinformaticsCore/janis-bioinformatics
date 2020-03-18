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

from janis_bioinformatics.data_types import FastaWithDict, Bam, FastqGz
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


class Gatk4FastqToSamBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "FastqToSam"

    def tool(self):
        return "Gatk4FastqToSam"

    def friendly_name(self):
        return "GATK4: Convert a FASTQ file to an unaligned BAM or SAM file."

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 1

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 4

    def inputs(self):
        return [
            ToolInput(
                "fastqR1",
                FastqGz(),
                prefix="--FASTQ",
                prefix_applies_to_all_elements=True,
                doc="Input fastq file (optionally gzipped) for single end data, or first read in paired end data.",
                position=10,
            ),
            ToolInput(
                "fastqR2",
                FastqGz(optional=True),
                prefix="--FASTQ2",
                prefix_applies_to_all_elements=True,
                doc="Input fastq file (optionally gzipped) for single end data, or first read in paired end data.",
                position=10,
            ),
            ToolInput(
                "sampleName",
                String(optional=True),
                prefix="--SAMPLE_NAME",
                prefix_applies_to_all_elements=True,
                doc="Input fastq file (optionally gzipped) for single end data, or first read in paired end data.",
                position=10,
            ),
            ToolInput(
                "reference",
                FastaWithDict(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                position=10,
                doc="Reference sequence file.",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".bam"),
                position=10,
                prefix="--OUTPUT",
                doc="Merged SAM or BAM file to write to.",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [ToolOutput("out", Bam(), glob=InputSelector("outputFilename"))]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=[
                "Michael Franklin (@illusional)",
                "Matthias De Smet(@matthdsm)",
            ],
            dateCreated=date(2020, 2, 26),
            dateUpdated=date(2020, 2, 26),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "merge", "sam"],
            documentationUrl="https://gatk.broadinstitute.org/hc/en-us/articles/360037226792-FastqToSam-Picard-",
            documentation="Converts a FASTQ file to an unaligned BAM or SAM file.",
        )

    additional_args = [
        ToolInput(
            "allowAndIgnoreEmptyLines",
            Boolean(optional=True),
            prefix="--ALLOW_AND_IGNORE_EMPTY_LINES",
            position=11,
            doc="Allow (and ignore) empty lines",
        ),
        ToolInput(
            "argumentsFile",
            Array(File(), optional=True),
            prefix="--arguments_file",
            position=11,
            doc="read one or more arguments files and add them to the command line",
        ),
        ToolInput(
            "comment",
            Array(String(), optional=True),
            prefix="--COMMENT",
            position=11,
            doc="Comment(s) to include in the merged output file's header.",
        ),
        ToolInput(
            "description",
            Array(String(), optional=True),
            prefix="--DESCRIPTION",
            position=11,
            doc="Inserted into the read group header",
        ),
        ToolInput(
            "libraryName",
            Array(String(), optional=True),
            prefix="--LIBRARY_NAME",
            position=11,
            doc="The library name to place into the LB attribute in the read group header",
        ),
        ToolInput(
            "maxQ",
            Int(optional=True),
            prefix="--MAX_Q",
            position=11,
            doc="Maximum quality allowed in the input fastq. An exception will be thrown if a quality is greater than this value.",
        ),
        ToolInput(
            "minQ",
            Int(optional=True),
            prefix="--MIN_Q",
            position=11,
            doc="Minimum quality allowed in the input fastq. An exception will be thrown if a quality is less than this value.",
        ),
        ToolInput(
            "platform",
            String(optional=True),
            prefix="--PLATFORM",
            position=11,
            doc="The platform type (e.g. ILLUMINA, SOLID) to insert into the read group header.",
        ),
        ToolInput(
            "platformModel",
            String(optional=True),
            prefix="--PLATFORM_MODEL",
            position=11,
            doc="Platform model to insert into the group header (free-form text providing further details of the platform/technology used).",
        ),
        ToolInput(
            "platformUnit",
            String(optional=True),
            prefix="--PLATFORM_UNIT",
            position=11,
            doc="The expected orientation of proper read pairs.",
        ),
        ToolInput(
            "predictedInsertSize",
            Int(optional=True),
            prefix="--PREDICTED_INSERT_SIZE",
            position=11,
            doc="Predicted median insert size, to insert into the read group header.",
        ),
        ToolInput(
            "programGroup",
            String(optional=True),
            prefix="--PROGRAM_GROUP",
            position=11,
            doc="Program group to insert into the read group header.",
        ),
        ToolInput(
            "readGroupName",
            String(optional=True),
            prefix="--READ_GROUP_NAME",
            position=11,
            doc="Read group name.",
        ),
        ToolInput(
            "runDate",
            String(optional=True),
            prefix="--RUN_DATE",
            position=11,
            doc="Date the run was produced, to insert into the read group header",
        ),
        ToolInput(
            "sequencingCenter",
            String(optional=True),
            prefix="--SEQUENCING_CENTER",
            position=11,
            doc="The sequencing center from which the data originated.",
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
            "useSequenctialFastqs",
            Boolean(optional=True),
            prefix="--USE_SEQUENTIAL_FASTQS",
            position=11,
            doc="Use sequential fastq files with the suffix _###.fastq or _###.fastq.gz.",
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
