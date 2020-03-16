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


class Gatk4MergeBamAlignmentBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MergeBamAlignment"

    def tool(self):
        return "Gatk4MergeBamAlignment"

    def friendly_name(self):
        return "GATK4: Merge SAM or BAM with unmapped BAM file"

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
                "ubam",
                BamBai(),
                prefix="--UNMAPPED_BAM",
                prefix_applies_to_all_elements=True,
                doc="Original SAM or BAM file of unmapped reads, which must be in queryname order.",
                position=10,
            ),
            ToolInput(
                "bam",
                Array(BamBai()),
                prefix="--ALIGNED_BAM",
                prefix_applies_to_all_elements=True,
                doc="SAM or BAM file(s) with alignment data.",
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
        return [
            ToolOutput(
                "out",
                BamBai(),
                glob=InputSelector("outputFilename"),
                secondaries_present_as={".bai": "^.bai"},
            )
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=[
                "Michael Franklin (@illisional)",
                "Matthias De Smet(@matthdsm)",
            ],
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2020, 2, 26),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "merge", "sam"],
            documentationUrl="https://gatk.broadinstitute.org/hc/en-us/articles/360037225832-MergeBamAlignment-Picard-",
            documentation="Merges SAM/BAM file with an unmapped BAM file",
        )

    additional_args = [
        ToolInput(
            "addMateCigar",
            Boolean(optional=True),
            prefix="--ADD_MATE_CIGAR",
            position=11,
            doc="Adds the mate CIGAR tag (MC)",
        ),
        ToolInput(
            "alignedReadsOnly",
            Boolean(optional=True),
            prefix="--ALIGNED_READS_ONLY",
            position=11,
            doc="Whether to output only aligned reads.",
        ),
        ToolInput(
            "alignerProperPairFlags",
            Boolean(optional=True),
            prefix="--ALIGNER_PROPER_PAIR_FLAGS",
            position=11,
            doc="Use the aligner's idea of what a proper pair is rather than computing in this program.",
        ),
        ToolInput(
            "argumentsFile",
            Array(File(), optional=True),
            prefix="--arguments_file",
            position=11,
            doc="read one or more arguments files and add them to the command line",
        ),
        ToolInput(
            "attributesToRemove",
            Array(String(), optional=True),
            prefix="--ATTRIBUTES_TO_REMOVE",
            position=11,
            doc="Attributes from the alignment record that should be removed when merging.",
        ),
        ToolInput(
            "attributesToRetain",
            Array(String(), optional=True),
            prefix="--ATTRIBUTES_TO_RETAIN",
            position=11,
            doc="Reserved alignment attributes (tags starting with X, Y, or Z) that should be brought over from the alignment data when merging.",
        ),
        ToolInput(
            "attributesToReverse",
            Array(String(), optional=True),
            prefix="--ATTRIBUTES_TO_REVERSE",
            position=11,
            doc="Attributes on negative strand reads that need to be reversed.",
        ),
        ToolInput(
            "attributesToReverseComplement",
            Array(String(), optional=True),
            prefix="--ATTRIBUTES_TO_REVERSE_COMPLEMENT",
            position=11,
            doc="Attributes on negative strand reads that need to be reverse complemented.",
        ),
        ToolInput(
            "clipAdapter",
            Boolean(optional=True),
            prefix="--CLIP_ADAPTERS",
            position=11,
            doc="Whether to clip adapters where identified.",
        ),
        ToolInput(
            "clipOverlappingReads",
            Boolean(optional=True),
            prefix="--CLIP_OVERLAPPING_READS",
            position=11,
            doc="For paired reads, soft clip the 3' end of each read if necessary so that it does not extend past the 5' end of its mate.",
        ),
        ToolInput(
            "expectedOrientations",
            Array(String(), optional=True),
            prefix="--EXPECTED_ORIENTATIONS",
            position=11,
            doc="The expected orientation of proper read pairs.",
        ),
        ToolInput(
            "includeSecondaryAlginments",
            Boolean(optional=True),
            prefix="--INCLUDE_SECONDARY_ALIGNMENTS",
            position=11,
            doc="If false, do not write secondary alignments to output.",
        ),
        ToolInput(
            "isBisulfiteSequencing",
            Boolean(optional=True),
            prefix="--IS_BISULFITE_SEQUENCE",
            position=11,
            doc="Whether the lane is bisulfite sequence (used when calculating the NM tag).",
        ),
        ToolInput(
            "matchingDictionaryTags",
            Array(String(), optional=True),
            prefix="--MATCHING_DICTIONARY_TAGS",
            position=11,
            doc="List of Sequence Records tags that must be equal (if present) in the reference dictionary and in the aligned file.",
        ),
        ToolInput(
            "maxInsertionsOrDeletions",
            Int(optional=True),
            prefix="--MAX_INSERTIONS_OR_DELETIONS",
            position=11,
            doc="The maximum number of insertions or deletions permitted for an alignment to be included.",
        ),
        ToolInput(
            "minUnclippedBases",
            Int(optional=True),
            prefix="--MIN_UNCLIPPED_BASES",
            position=11,
            doc="If UNMAP_CONTAMINANT_READS is set, require this many unclipped bases or else the read will be marked as contaminant.",
        ),
        ToolInput(
            "primaryAlignmentStrategy",
            Int(optional=True),
            prefix="--PRIMARY_ALIGNMENT_STRATEGY",
            position=11,
            doc="Strategy for selecting primary alignment when the aligner has provided more than one alignment for a pair or fragment, and none are marked as primary, more than one is marked as primary, or the primary alignment is filtered out for some reason.",
        ),
        ToolInput(
            "programGroupCommandLine",
            String(optional=True),
            prefix="--PROGRAM_GROUP_COMMAND_LINE",
            position=11,
            doc="The command line of the program group.",
        ),
        ToolInput(
            "programGroupName",
            String(optional=True),
            prefix="--PROGRAM_GROUP_NAME",
            position=11,
            doc="The name of the program group.",
        ),
        ToolInput(
            "programGroupVersion",
            String(optional=True),
            prefix="--PROGRAM_GROUP_VERSION",
            position=11,
            doc="The version of the program group.",
        ),
        ToolInput(
            "programRecordId",
            String(optional=True),
            prefix="--PROGRAM_RECORD_ID",
            position=11,
            doc="The program group ID of the aligner.",
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
            "unmapContaminantReads",
            Boolean(optional=True),
            prefix="--UNMAP_CONTAMINANT_READS",
            position=11,
            doc="Detect reads originating from foreign organisms (e.g. bacterial DNA in a non-bacterial sample),and unmap + label those reads accordingly.",
        ),
        ToolInput(
            "unmappedReadStrategy",
            String(optional=True),
            prefix="--UNMAPPED_READ_STRATEGY",
            position=11,
            doc="How to deal with alignment information in reads that are being unmapped (e.g. due to cross-species contamination.) Currently ignored unless UNMAP_CONTAMINANT_READS = true.",
        ),
        ToolInput(
            "addPgTagToReads",
            Boolean(optional=True),
            prefix="--ADD_PG_TAG_TO_READS",
            position=11,
            doc="Add PG tag to each read in a SAM or BAM",
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
