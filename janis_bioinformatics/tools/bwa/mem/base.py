import os
from abc import ABC
from typing import Any, Dict

from janis_core import (
    Array,
    ToolInput,
    Int,
    Float,
    Boolean,
    String,
    ToolOutput,
    Filename,
    InputSelector,
    CaptureType,
    CpuSelector,
    Stdout,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
)
from janis_core.tool.test_classes import TTestCase

from janis_bioinformatics.data_types import Sam, FastaBwa, FastqGz, FastqGzPair, Bam
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

BWA_MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 8,
            CaptureType.EXOME: 12,
            CaptureType.CHROMOSOME: 12,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 20,
            CaptureType.THREEHUNDREDX: 24,
        },
    )
]

BWA_CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 16,
            CaptureType.EXOME: 20,
            CaptureType.CHROMOSOME: 24,
            CaptureType.THIRTYX: 30,
            CaptureType.NINETYX: 32,
            CaptureType.THREEHUNDREDX: 32,
        },
    )
]


class BwaMemBase(BioinformaticsTool, ABC):
    def tool(self):
        return "bwamem"

    def friendly_name(self):
        return "BWA-MEM"

    def tool_provider(self):
        return "BWA"

    def base_command(self):
        return ["bwa", "mem"]

    def inputs(self):
        return [
            ToolInput("reference", FastaBwa(), position=9),
            ToolInput("reads", Array(FastqGz()), position=10, doc=None),
            ToolInput("mates", FastqGzPair(optional=True), position=11, doc=None),
            ToolInput("outputFilename", Filename(extension=".sam")),
            *BwaMemBase.additional_inputs,
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Sam()))]

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, BWA_MEM_TUPLE)
        if val:
            return val
        return 16

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, BWA_CORES_TUPLE)
        if val:
            return val
        return 16

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 7, 23),
            institution="Sanger Institute",
            doi=None,
            citation="The BWA-MEM algorithm has not been published yet.",
            keywords=["bwa", "mem", "align"],
            documentationUrl="http://bio-bwa.sourceforge.net/bwa.shtml#3",
            documentation="""bwa - Burrows-Wheeler Alignment Tool
BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human 
genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for 
Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. 
BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is 
the latest, is generally recommended for high-quality queries as it is faster and more accurate. 
BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.

Align 70bp-1Mbp query sequences with the BWA-MEM algorithm. Briefly, the algorithm works by seeding alignments 
with maximal exact matches (MEMs) and then extending seeds with the affine-gap Smith-Waterman algorithm (SW).

If mates.fq file is absent and option -p is not set, this command regards input reads are single-end. If 'mates.fq' 
is present, this command assumes the i-th read in reads.fq and the i-th read in mates.fq constitute a read pair. 
If -p is used, the command assumes the 2i-th and the (2i+1)-th read in reads.fq constitute a read pair (such input 
file is said to be interleaved). In this case, mates.fq is ignored. In the paired-end mode, the mem command will 
infer the read orientation and the insert size distribution from a batch of reads.

The BWA-MEM algorithm performs local alignment. It may produce multiple primary alignments for different part of a 
query sequence. This is a crucial feature for long sequences. However, some tools such as Picard’s markDuplicates 
does not work with split alignments. One may consider to use option -M to flag shorter split hits as secondary.
""".strip(),
        )

    additional_inputs = [
        ToolInput(
            "threads",
            Int(optional=True),
            default=CpuSelector(),
            prefix="-t",
            doc="Number of threads. (default = 1)",
        ),
        ToolInput(
            "minimumSeedLength",
            Int(optional=True),
            prefix="-k",
            doc="Matches shorter than INT will be missed. The alignment speed is usually "
            "insensitive to this value unless it significantly deviates 20. (Default: 19)",
        ),
        ToolInput(
            "bandwidth",
            Int(optional=True),
            prefix="-w",
            doc="Essentially, gaps longer than ${bandWidth} will not be found. Note that the maximum gap length "
            "is also affected by the scoring matrix and the hit length, not solely determined by this option."
            " (Default: 100)",
        ),
        ToolInput(
            "offDiagonalXDropoff",
            Int(optional=True),
            prefix="-d",
            doc="(Z-dropoff): Stop extension when the difference between the best and the current extension "
            "score is above |i-j|*A+INT, where i and j are the current positions of the query and reference, "
            "respectively, and A is the matching score. Z-dropoff is similar to BLAST’s X-dropoff except "
            "that it doesn’t penalize gaps in one of the sequences in the alignment. Z-dropoff not only "
            "avoids unnecessary extension, but also reduces poor alignments inside a long good alignment. "
            "(Default: 100)",
        ),
        ToolInput(
            "reseedTrigger",
            Float(optional=True),
            prefix="-r",
            doc="Trigger re-seeding for a MEM longer than minSeedLen*FLOAT. This is a key heuristic parameter "
            "for tuning the performance. Larger value yields fewer seeds, which leads to faster alignment "
            "speed but lower accuracy. (Default: 1.5)",
        ),
        ToolInput(
            "occurenceDiscard",
            Int(optional=True),
            prefix="-c",
            doc="Discard a MEM if it has more than INT occurence in the genome. "
            "This is an insensitive parameter. (Default: 10000)",
        ),
        ToolInput(
            "performSW",
            Boolean(optional=True),
            prefix="-P",
            doc="In the paired-end mode, perform SW to rescue missing hits only but "
            "do not try to find hits that fit a proper pair.",
        ),
        ToolInput(
            "matchingScore",
            Int(optional=True),
            prefix="-A",
            doc="Matching score. (Default: 1)",
        ),
        ToolInput(
            "mismatchPenalty",
            Int(optional=True),
            prefix="-B",
            doc="Mismatch penalty. The sequence error rate is approximately: {.75 * exp[-log(4) * B/A]}. "
            "(Default: 4)",
        ),
        ToolInput(
            "openGapPenalty",
            Int(optional=True),
            prefix="-O",
            doc="Gap open penalty. (Default: 6)",
        ),
        ToolInput(
            "gapExtensionPenalty",
            Int(optional=True),
            prefix="-E",
            doc="Gap extension penalty. A gap of length k costs O + k*E "
            "(i.e. -O is for opening a zero-length gap). (Default: 1)",
        ),
        ToolInput(
            "clippingPenalty",
            Int(optional=True),
            prefix="-L",
            doc="Clipping penalty. When performing SW extension, BWA-MEM keeps track of the best score "
            "reaching the end of query. If this score is larger than the best SW score minus the "
            "clipping penalty, clipping will not be applied. Note that in this case, the SAM AS tag "
            "reports the best SW score; clipping penalty is not deducted. (Default: 5)",
        ),
        ToolInput(
            "unpairedReadPenalty",
            Int(optional=True),
            prefix="-U",
            doc="Penalty for an unpaired read pair. BWA-MEM scores an unpaired read pair as "
            "scoreRead1+scoreRead2-INT and scores a paired as scoreRead1+scoreRead2-insertPenalty. "
            "It compares these two scores to determine whether we should force pairing. (Default: 9)",
        ),
        ToolInput(
            "assumeInterleavedFirstInput",
            Boolean(optional=True),
            prefix="-p",
            doc="Assume the first input query file is interleaved paired-end FASTA/Q. ",
        ),
        ToolInput(
            "readGroupHeaderLine",
            String(optional=True),
            prefix="-R",
            doc="Complete read group header line. ’\\t’ can be used in STR and will be converted to a TAB i"
            "n the output SAM. The read group ID will be attached to every read in the output. "
            "An example is ’@RG\\tID:foo\\tSM:bar’. (Default=null)",
        ),
        ToolInput(
            "outputAlignmentThreshold",
            Int(optional=True),
            prefix="-T",
            doc="Don’t output alignment with score lower than INT. Only affects output. (Default: 30)",
        ),
        ToolInput(
            "outputAllElements",
            Boolean(optional=True),
            prefix="-a",
            doc="Output all found alignments for single-end or unpaired paired-end reads. "
            "These alignments will be flagged as secondary alignments.",
        ),
        ToolInput(
            "appendComments",
            Boolean(optional=True),
            prefix="-C",
            doc="Append append FASTA/Q comment to SAM output. This option can be used to transfer "
            "read meta information (e.g. barcode) to the SAM output. Note that the FASTA/Q comment "
            "(the string after a space in the header line) must conform the SAM spec (e.g. BC:Z:CGTAC). "
            "Malformated comments lead to incorrect SAM output.",
        ),
        ToolInput(
            "hardClipping",
            Boolean(optional=True),
            prefix="-H",
            doc="Use hard clipping ’H’ in the SAM output. This option may dramatically reduce "
            "the redundancy of output when mapping long contig or BAC sequences.",
        ),
        ToolInput(
            "markShorterSplits",
            Boolean(optional=True),
            prefix="-M",
            doc="Mark shorter split hits as secondary (for Picard compatibility).",
        ),
        ToolInput(
            "verboseLevel",
            Int(optional=True),
            prefix="-v",
            doc="Control the verbose level of the output. "
            "This option has not been fully supported throughout BWA. Ideally, a value: "
            "0 for disabling all the output to stderr; "
            "1 for outputting errors only; "
            "2 for warnings and errors; "
            "3 for all normal messages; "
            "4 or higher for debugging. When this option takes value 4, the output is not SAM. (Default: 3)",
        ),
    ]

    def tests(self):
        remote_dir = "https://swift.rc.nectar.org.au/v1/AUTH_4df6e734a509497692be237549bbe9af/janis-test-data/bioinformatics/wgsgermline_data"
        return [
            TTestCase(
                name="basic",
                input={
                    "reads": [
                        f"{remote_dir}/NA12878-BRCA1_R1.fastq.gz",
                        f"{remote_dir}/NA12878-BRCA1_R2.fastq.gz",
                    ],
                    "reference": f"{remote_dir}/Homo_sapiens_assembly38.chr17.fasta",
                    "markShorterSplits": True,
                    "readGroupHeaderLine": "@RG\tID:NA12878-BRCA1\tSM:NA12878-BRCA1\tLB:NA12878-BRCA1\tPL:ILLUMINA",
                    "threads": 16,
                },
                output=Bam.basic_test(
                    "out",
                    8628527,
                    f"{remote_dir}/NA12878-BRCA1.bwamem.flagstat",
                ),
            ),
            TTestCase(
                name="minimal",
                input={
                    "reads": [
                        f"{remote_dir}/NA12878-BRCA1_R1.fastq.gz",
                        f"{remote_dir}/NA12878-BRCA1_R2.fastq.gz",
                    ],
                    "reference": f"{remote_dir}/Homo_sapiens_assembly38.chr17.fasta",
                    "markShorterSplits": True,
                    "readGroupHeaderLine": "@RG\tID:NA12878-BRCA1\tSM:NA12878-BRCA1\tLB:NA12878-BRCA1\tPL:ILLUMINA",
                    "threads": 16,
                },
                output=self.minimal_test(),
            ),
        ]
