from abc import ABC
from typing import Dict, Any
from janis_core import get_value_for_hints_and_ordered_resource_tuple
from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    Array,
    String,
    InputSelector,
    File,
    Boolean,
    Int,
    CaptureType,
)
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import Vcf
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


class Gatk4GatherVcfsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "GatherVcfs"

    @staticmethod
    def tool():
        return "Gatk4GatherVcfs"

    def friendly_name(self):
        return "GATK4: Gather VCFs"

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

    def inputs(self):
        return [
            ToolInput(
                "vcfs",
                Array(Vcf()),
                prefix="--INPUT",
                doc="[default: []] (-I) Input VCF file(s).",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf", suffix=".gathered"),
                prefix="--OUTPUT",
                doc="[default: null] (-O) Output VCF file.",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [ToolOutput("out", Vcf(), glob=InputSelector("outputFilename"))]

    def metadata(self):
        from datetime import date

        return ToolMetadata(
            creator="Michael Franklin",
            maintainer="Michael Franklin",
            maintainerEmail="michael.franklin@petermac.org",
            dateCreated=date(2018, 5, 1),
            dateUpdated=date(2019, 5, 1),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=[
                "gatk",
                "gatk4",
                "broad",
                "gather",
                "vcfs",
                "variant manipulation",
            ],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.12.0/picard_vcf_GatherVcfs.php",
            documentation="""GatherVcfs (Picard)
            
Gathers multiple VCF files from a scatter operation into a single VCF file. 
Input files must be supplied in genomic order and must not have events at overlapping positions.
""".strip(),
        )

    additional_args = [
        ToolInput(
            "argumentsFile",
            Array(File(), optional=True),
            prefix="--arguments_file",
            doc="[default: []] read one or more arguments files and add them to the command line",
        ),
        ToolInput(
            "compressionLevel",
            Int(optional=True),
            prefix="--COMPRESSION_LEVEL",
            doc="[default: 5] Compression level for all compressed files created (e.g. BAM and VCF).",
        ),
        ToolInput(
            "createIndex",
            Boolean(optional=True),
            prefix="--CREATE_INDEX",
            doc="[default: TRUE] Whether to create a BAM index when writing a coordinate-sorted BAM file.",
        ),
        ToolInput(
            "createMd5File",
            Boolean(optional=True),
            prefix="--CREATE_MD5_FILE",
            doc="[default: FALSE] Whether to create an MD5 digest for any BAM or FASTQ files created.",
        ),
        ToolInput(
            "ga4ghClientSecrets",
            File(optional=True),
            prefix="--GA4GH_CLIENT_SECRETS",
            doc="[default: client_secrets.json] Google Genomics API client_secrets.json file path.",
        ),
        ToolInput(
            "maxRecordsInRam",
            Int(optional=True),
            prefix="--MAX_RECORDS_IN_RAM",
            doc="[default: 500000] When writing files that need to be sorted, this will specify the number of "
            "records stored in RAM before spilling to disk. Increasing this number reduces the number of "
            "file handles needed to sort the file, and increases the amount of RAM needed.",
        ),
        ToolInput(
            "quiet",
            Boolean(optional=True),
            prefix="--QUIET",
            doc="[default: FALSE] Whether to suppress job-summary info on System.err.",
        ),
        ToolInput(
            "referenceSequence",
            File(optional=True),
            prefix="--REFERENCE_SEQUENCE",
            doc="[default: null] Reference sequence file.",
        ),
        ToolInput(
            "tmpDir",
            String(optional=True),
            default="/tmp",
            prefix="--TMP_DIR",
            doc="[default: []] One or more directories with space available to be "
            "used by this program for temporary storage of working files",
        ),
        ToolInput(
            "useJdkDeflater",
            Boolean(optional=True),
            prefix="--USE_JDK_DEFLATER",
            doc="[default: FALSE] (-use_jdk_deflater) Use the JDK Deflater instead "
            "of the Intel Deflater for writing compressed output",
        ),
        ToolInput(
            "useJdkInflater",
            Boolean(optional=True),
            prefix="--USE_JDK_INFLATER",
            doc="[default: FALSE] (-use_jdk_inflater) Use the JDK Inflater instead "
            "of the Intel Inflater for reading compressed input",
        ),
        ToolInput(
            "validationStringency",
            String(optional=True),
            prefix="--VALIDATION_STRINGENCY",
            doc="[default: STRICT] Validation stringency for all SAM files read by this program. Setting "
            "stringency to SILENT can improve performance when processing a BAM file in which "
            "variable-length data (read, qualities, tags) do not otherwise need to be decoded.",
        ),
        ToolInput(
            "verbosity",
            Boolean(optional=True),
            prefix="--VERBOSITY",
            doc="[default: INFO] Control verbosity of logging.",
        ),
    ]
