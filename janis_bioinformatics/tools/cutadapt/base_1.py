from datetime import datetime
from typing import List

from janis_core import CaptureType
from janis_core import (
    ToolOutput,
    ToolInput,
    Boolean,
    String,
    Float,
    Int,
    Filename,
    ToolMetadata,
    WildcardSelector,
)
from janis_core import get_value_for_hints_and_ordered_resource_tuple

from janis_bioinformatics.data_types import Fastq
from janis_bioinformatics.tools import BioinformaticsTool

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.EXOME: 4,
            CaptureType.CHROMOSOME: 8,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 16,
            CaptureType.THREEHUNDREDX: 24,
        },
    )
]

CPU_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 2,
            CaptureType.EXOME: 4,
            CaptureType.CHROMOSOME: 5,
            CaptureType.THIRTYX: 8,
            CaptureType.NINETYX: 12,
            CaptureType.THREEHUNDREDX: 16,
        },
    )
]


class CutAdaptBase_1(BioinformaticsTool):
    def friendly_name(self) -> str:
        return "Cutadapt"

    @staticmethod
    def tool_provider():
        return "cutadapt"

    @staticmethod
    def tool() -> str:
        return "cutadapt"

    @staticmethod
    def base_command():
        return "cutadapt"

    def inputs(self) -> List[ToolInput]:
        import uuid

        fastq_uuid = str(uuid.uuid1())
        return [
            ToolInput("fastq", Fastq(), position=5),
            ToolInput(
                "adapter",
                String(optional=True),
                prefix="-a",
                doc="Sequence of an adapter ligated to the 3' end (paired data: of the first read). "
                "The adapter and subsequent bases are trimmed. If a '$' character is appended ('anchoring'), "
                "the adapter is only found if it is a suffix of the read.",
            ),
            ToolInput(
                "outputFilename",
                Filename(suffix="-R1", extension=".fastq.gz", guid=fastq_uuid),
                prefix="-o",
                doc="Write trimmed reads to FILE. FASTQ or FASTA format is chosen depending on input. "
                "The summary report is sent to standard output. Use '{name}' in FILE to demultiplex "
                "reads into multiple files. Default: write to standard output",
            ),
            ToolInput(
                "secondReadFile",
                Filename(suffix="-R2", extension=".fastq.gz", guid=fastq_uuid),
                prefix="-p",
                doc="Write second read in a pair to FILE.",
            ),
            *self.additional_args,
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Fastq(), glob=WildcardSelector("*.fastq.gz"))]

    def memory(self, hints):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 4

    def cpus(self, hints):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CPU_TUPLE)
        if val:
            return val
        return 5

    additional_args = [
        ToolInput(
            "debug",
            Boolean(optional=True),
            prefix="--debug",
            doc="Print debugging information.",
        ),
        ToolInput(
            "noIndels",
            Boolean(optional=True),
            prefix="--no-indels",
            doc="Allow only mismatches in alignments. Default: allow both mismatches and indels",
        ),
        ToolInput(
            "matchReadWildcards",
            Boolean(optional=True),
            prefix="--match-read-wildcards",
            doc="Interpret IUPAC wildcards in reads. Default: False",
        ),
        ToolInput(
            "trimN",
            Boolean(optional=True),
            prefix="--trim-n",
            doc="Trim N's on ends of reads.",
        ),
        ToolInput(
            "discardCasava",
            Boolean(optional=True),
            prefix="--discard-casava",
            doc="Discard reads that did not pass CASAVA filtering (header has :Y:).",
        ),
        ToolInput(
            "quiet",
            Boolean(optional=True),
            prefix="--quiet",
            doc="Print only error messages.",
        ),
        ToolInput(
            "stripF3",
            Boolean(optional=True),
            prefix="--strip-f3",
            doc="Strip the _F3 suffix of read names",
        ),
        ToolInput(
            "noZeroCap",
            Boolean(optional=True),
            prefix="--no-zero-cap",
            doc="Disable zero capping",
        ),
        ToolInput(
            "interleaved",
            Boolean(optional=True),
            prefix="--interleaved",
            doc="Read and write interleaved paired-end reads.",
        ),
        ToolInput(
            "discardTrimmed",
            Boolean(optional=True),
            prefix="--discard-trimmed",
            doc="Discard reads that contain an adapter. "
            "Also use -O to avoid discarding too many randomly matching reads!",
        ),
        ToolInput(
            "discardUntrimmed",
            Boolean(optional=True),
            prefix="--discard-untrimmed",
            doc="Discard reads that do not contain an adapter.",
        ),
        ToolInput(
            "maq",
            Boolean(optional=True),
            prefix="--maq",
            doc="MAQ- and BWA-compatible colorspace output. This enables -c, -d, -t, --strip-f3 and -y '/1'.",
        ),
        ToolInput(
            "pairFilter",
            String(optional=True),
            prefix="--pair-filter=",
            doc="(any|both|first) Which of the reads in a paired-end read have to match the filtering "
            "criterion in order for the pair to be filtered. Default: any",
        ),
        ToolInput(
            "nextseqTrim",
            String(optional=True),
            prefix="--nextseq-trim=",
            doc="NextSeq-specific quality trimming (each read). Trims also dark cycles appearing as "
            "high-quality G bases.",
        ),
        ToolInput(
            "action",
            String(optional=True),
            prefix="--action=",
            doc="What to do with found adapters. trim: remove; mask: replace with 'N' characters; "
            "none: leave unchanged (useful with --discard-untrimmed). Default: trim",
        ),
        ToolInput(
            "qualityBase",
            String(optional=True),
            prefix="--quality-base=",
            doc="Assume that quality values in FASTQ are encoded as ascii(quality + N). "
            "This needs to be set to 64 for some old Illumina FASTQ files. Default: 33",
        ),
        ToolInput(
            "lengthTag",
            String(optional=True),
            prefix="--length-tag=",
            doc="Search for TAG followed by a decimal number in the description field of the read. "
            "Replace the decimal number with the correct length of the trimmed read. "
            "For example, use --length-tag 'length=' to correct fields like 'length=123'.",
        ),
        ToolInput(
            "stripSuffix",
            String(optional=True),
            prefix="--strip-suffix=",
            doc="Remove this suffix from read names if present. Can be given multiple times.",
        ),
        ToolInput(
            "maxN",
            Int(optional=True),
            prefix="--max-n=",
            doc="Discard reads with more than COUNT 'N' bases. If COUNT is a number between 0 and 1, "
            "it is interpreted as a fraction of the read length.",
        ),
        ToolInput(
            "report",
            String(optional=True),
            prefix="--report=",
            doc="Which type of report to print. Default: full",
        ),
        ToolInput(
            "infoFile",
            String(optional=True),
            prefix="--info-file=",
            doc="Write information about each read and its adapter matches into FILE. "
            "See the documentation for the file format.",
        ),
        ToolInput(
            "wildcardFile",
            String(optional=True),
            prefix="--wildcard-file=",
            doc="When the adapter has N wildcard bases, write adapter bases matching wildcard positions to FILE. "
            "(Inaccurate with indels.)",
        ),
        ToolInput(
            "tooShortOutput",
            String(optional=True),
            prefix="--too-short-output=",
            doc="Write reads that are too short (according to length specified by -m) to FILE. "
            "Default: discard reads",
        ),
        ToolInput(
            "tooLongOutput",
            String(optional=True),
            prefix="--too-long-output=",
            doc="Write reads that are too long (according to length specified by -M) to FILE. "
            "Default: discard reads",
        ),
        ToolInput(
            "untrimmedOutput",
            String(optional=True),
            prefix="--untrimmed-output=",
            doc="Write reads that do not contain any adapter to FILE. "
            "Default: output to same file as trimmed reads",
        ),
        ToolInput(
            "untrimmedPairedOutput",
            String(optional=True),
            prefix="--untrimmed-paired-output=",
            doc="Write second read in a pair to this FILE when no adapter was found. Use with --untrimmed-output."
            " Default: output to same file as trimmed reads",
        ),
        ToolInput(
            "tooShortPairedOutput",
            String(optional=True),
            prefix="--too-short-paired-output=",
            doc="Write second read in a pair to this file if pair is too short. Use also --too-short-output.",
        ),
        ToolInput(
            "tooLongPairedOutput",
            String(optional=True),
            prefix="--too-long-paired-output=",
            doc="Write second read in a pair to this file if pair is too long. Use also --too-long-output.",
        ),
        ToolInput(
            "inputFileFormat",
            String(optional=True),
            prefix="-f",
            doc="Input file format; can be either 'fasta', 'fastq' or 'sra-fastq'. "
            "Ignored when reading csfasta/qual files. Default: auto-detect from file name extension.",
        ),
        ToolInput(
            "cores",
            Int(optional=True),
            prefix="-j",
            default=0,
            doc="Number of CPU cores to use. Use 0 to auto-detect. Default: 1",
        ),
        ToolInput(
            "adapter_g",
            String(optional=True),
            prefix="-g",
            doc="Sequence of an adapter ligated to the 5' end (paired data: of the first read). "
            "The adapter and any preceding bases are trimmed. Partial matches at the 5' end are allowed. "
            "If a '^' character is prepended ('anchoring'), the adapter is only found if it is a "
            "prefix of the read.",
        ),
        ToolInput(
            "adapter_both",
            String(optional=True),
            prefix="-b",
            doc="Sequence of an adapter that may be ligated to the 5' or 3' end (paired data: of the first read)."
            " Both types of matches as described under -a und -g are allowed. If the first base of the read "
            "is part of the match, the behavior is as with -g, otherwise as with -a. This option is mostly "
            "for rescuing failed library preparations "
            "- do not use if you know which end your adapter was ligated to!",
        ),
        ToolInput(
            "maximumErrorRate",
            Float(optional=True),
            prefix="-e",
            doc="Maximum allowed error rate as value between 0 and 1 (no. of errors divided by length of "
            "matching region). Default: 0.1 (=10%)",
        ),
        ToolInput(
            "removeNAdapters",
            Int(optional=True),
            prefix="-n",
            doc="Remove up to COUNT adapters from each read. Default: 1",
        ),
        ToolInput(
            "overlapRequirement",
            Int(optional=True),
            prefix="-O",
            doc="Require MINLENGTH overlap between read and adapter for an adapter to be found. Default: 3",
        ),
        ToolInput(
            "removeNBases",
            Int(optional=True),
            prefix="-u",
            doc="Remove bases from each read (first read only if paired). If LENGTH is positive, remove bases "
            "from the beginning. If LENGTH is negative, remove bases from the end. Can be used twice if "
            "LENGTHs have different signs. This is applied *before* adapter trimming.",
        ),
        ToolInput(
            "qualityCutoff",
            Int(optional=True),
            prefix="-q",
            doc="--quality-cutoff=[5'CUTOFF,]3'CUTOFF Trim low-quality bases from 5' and/or 3' ends of each "
            "read before adapter removal. Applied to both reads if data is paired. If one value is given, "
            "only the 3' end is trimmed. If two comma-separated cutoffs are given, the 5' end is trimmed "
            "with the first cutoff, the 3' end with the second.",
        ),
        ToolInput(
            "shortenReadsToLength",
            Int(optional=True),
            prefix="-l",
            doc="Shorten reads to LENGTH. Positive values remove bases at the end while negative ones remove "
            "bases at the beginning. This and the following modifications are applied after adapter trimming.",
        ),
        ToolInput(
            "readNamesPrefix",
            String(optional=True),
            prefix="-x",
            doc="Add this prefix to read names. Use {name} to insert the name of the matching adapter.",
        ),
        ToolInput(
            "readNamesSuffix",
            String(optional=True),
            prefix="-y",
            doc="Add this suffix to read names; can also include {name}",
        ),
        ToolInput(
            "minReadLength",
            Int(optional=True),
            prefix="-m",
            doc="--minimum-length=LEN[:LEN2] Discard reads shorter than LEN. Default: 0",
        ),
        ToolInput(
            "maxReadsLength",
            Int(optional=True),
            prefix="-M",
            doc="--maximum-length=LEN[:LEN2] Discard reads longer than LEN. Default: no limit",
        ),
        ToolInput(
            "middleReadMatchFile",
            String(optional=True),
            prefix="-r",
            doc="When the adapter matches in the middle of a read, write the rest (after the adapter) to FILE.",
        ),
        ToolInput(
            "removeMiddle3Adapter",
            String(optional=True),
            prefix="-A",
            doc="3' adapter to be removed from second read in a pair.",
        ),
        ToolInput(
            "removeMiddle5Adapter",
            String(optional=True),
            prefix="-G",
            doc="5' adapter to be removed from second read in a pair.",
        ),
        ToolInput(
            "removeMiddleBothAdapter",
            String(optional=True),
            prefix="-B",
            doc="5'/3 adapter to be removed from second read in a pair.",
        ),
        ToolInput(
            "removeNBasesFromSecondRead",
            Int(optional=True),
            prefix="-U",
            doc="Remove LENGTH bases from second read in a pair.",
        ),
        ToolInput(
            "noMatchAdapterWildcards",
            Boolean(optional=True),
            prefix="-N",
            doc="Do not interpret IUPAC wildcards in adapters.",
        ),
        ToolInput(
            "colorspace",
            Boolean(optional=True),
            prefix="-c",
            doc="Enable colorspace mode",
        ),
        ToolInput(
            "doubleEncode",
            Boolean(optional=True),
            prefix="-d",
            doc="Double-encode colors (map 0,1,2,3,4 to A,C,G,T,N).",
        ),
        ToolInput(
            "trimPrimer",
            Boolean(optional=True),
            prefix="-t",
            doc="Trim primer base and the first color",
        ),
        ToolInput(
            "zeroCap",
            Boolean(optional=True),
            prefix="-z",
            doc="Change negative quality values to zero. Enabled by default in colorspace mode "
            "since many tools have problems with negative qualities",
        ),
    ]

    def metadata(self):
        return ToolMetadata(
            creator=None,
            maintainer="Michael Franklin",
            maintainerEmail="michael.franklin@petermac.org",
            dateCreated=datetime(2019, 3, 21),
            dateUpdated=datetime(2019, 3, 29),
            institution=None,
            doi="DOI:10.14806/ej.17.1.200",
            citation="Martin, Marcel. “Cutadapt Removes Adapter Sequences from High-Throughput Sequencing Reads.” "
            "EMBnet.journal, vol. 17, no. 1, EMBnet Stichting, May 2011, p. 10. "
            "Crossref, doi:10.14806/ej.17.1.200.",
            keywords=["cutadapt", "trim"],
            documentationUrl="https://cutadapt.readthedocs.io/en/stable/",
            documentation="""
Cutadapt finds and removes adapter sequences, primers, poly-A tails and other types of unwanted sequence 
from your high-throughput sequencing reads.

Cleaning your data in this way is often required: Reads from small-RNA sequencing 
contain the 3’ sequencing adapter because the read is longer than the molecule that is sequenced. 
Amplicon reads start with a primer sequence. Poly-A tails are useful for pulling out RNA from your sample, 
but often you don’t want them to be in your reads.
Cutadapt helps with these trimming tasks by finding the adapter or primer sequences in an error-tolerant way. 
It can also modify and filter reads in various ways. Adapter sequences can contain IUPAC wildcard characters. 
Also, paired-end reads and even colorspace data is supported. If you want, you can also just demultiplex your 
input data, without removing adapter sequences at all.

Cutadapt comes with an extensive suite of automated tests and is available under the terms of the MIT license.
If you use Cutadapt, please cite DOI:10.14806/ej.17.1.200 .""",
        )
