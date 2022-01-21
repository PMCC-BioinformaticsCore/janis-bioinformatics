from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    String,
    File,
    Filename,
    Array,
    Int,
    Float,
    ToolOutput,
    InputSelector,
    get_value_for_hints_and_ordered_resource_tuple,
    CaptureType,
)
from janis_bioinformatics.data_types import Bam
from janis_bioinformatics.tools.htseq.htseqtoolbase import HTSeqToolBase

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
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class HTSeqCountBase(HTSeqToolBase, ABC):
    def tool(self):
        return "HTSeqCount"

    def friendly_name(self):
        return "HTSeq-Count"

    def base_command(self):
        return ["htseq-count"]

    def inputs(self):
        return [
            ToolInput("bams", Array(Bam), position=3),
            ToolInput("gff_file", File, position=4),
            ToolInput(
                "outputFilename",
                Filename(suffix=".htseq-count", extension=".txt"),
                prefix=">",
                doc="",
                position=5,
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("outputFilename"))]

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

    def bind_metadata(self):
        from datetime import date

        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.dateCreated = date(2022, 1, 17)
        self.metadata.dateUpdated = date(2022, 1, 17)
        self.metadata.doi = (
            "https://htseq.readthedocs.io/en/release_0.11.1/overview.html"
        )
        self.metadata.citation = (
            "G Putri, S Anders, PT Pyl, JE Pimanda, F Zanini"
            "Analysing high-throughput sequencing data with HTSeq 2.0"
            "arXiv:2112.00939 (2021)"
        )
        self.metadata.documentationUrl = (
            "https://htseq.readthedocs.io/en/release_0.11.1/count.html#count"
        )

    additional_args = [
        ToolInput(
            "format",
            String(optional=True),
            prefix="--format=",
            separate_value_from_prefix=False,
            position=1,
            doc="Format of the input data. Possible values are sam (for text \
SAM files) and bam (for binary BAM files). Default is sam.",
        ),
        ToolInput(
            "order",
            String(optional=True),
            prefix="--order=",
            separate_value_from_prefix=False,
            position=1,
            doc="For paired-end data, the alignment have to be sorted either \
by read name or by alignment position. If your data is not sorted, use the \
samtools sort function of samtools to sort it. Use this option, with name or \
pos for <order> to indicate how the input data has been sorted. The default is name.\
If name is indicated, htseq-count expects all the alignments for the reads of \
a given read pair to appear in adjacent records in the input data. For pos, \
this is not expected; rather, read alignments whose mate alignment have not \
yet been seen are kept in a buffer in memory until the mate is found. While, \
strictly speaking, the latter will also work with unsorted data, sorting \
ensures that most alignment mates appear close to each other in the data \
and hence the buffer is much less likely to overflow.",
        ),
        ToolInput(
            "max_reads_in_buffer",
            Int(optional=True),
            prefix="--max-reads-in-buffer=",
            separate_value_from_prefix=False,
            position=1,
            doc="When <alignment_file> is paired end sorted by position, \
allow only so many reads to stay in memory until the mates are found (raising \
this number will use more memory). Has no effect for single end or paired end \
sorted by name. (default: 30000000)",
        ),
        ToolInput(
            "stranded",
            String(optional=True),
            prefix="--stranded=",
            separate_value_from_prefix=False,
            position=1,
            doc="whether the data is from a strand-specific assay (default: \
yes)\
For stranded=no, a read is considered overlapping with a feature regardless \
of whether it is mapped to the same or the opposite strand as the feature. \
For stranded=yes and single-end reads, the read has to be mapped to the same \
strand as the feature. For paired-end reads, the first read has to be on the \
same strand and the second read on the opposite strand. For stranded=reverse, \
these rules are reversed.",
        ),
        ToolInput(
            "minaqual",
            Int(optional=True),
            prefix="-a",
            position=1,
            doc="skip all reads with alignment quality lower than the given \
minimum value (default: 10 — Note: the default used to be 0 until \
version 0.5.4.)",
        ),
        ToolInput(
            "type",
            String(optional=True),
            prefix="--type=",
            separate_value_from_prefix=False,
            position=1,
            doc="feature type (3rd column in GFF file) to be used, all \
features of other type are ignored (default, suitable for RNA-Seq analysis \
using an Ensembl GTF file: exon)",
        ),
        ToolInput(
            "id",
            String(optional=True),
            prefix="--idattr=",
            separate_value_from_prefix=False,
            position=1,
            doc="GFF attribute to be used as feature ID. Several GFF lines \
with the same feature ID will be considered as parts of the same feature. The \
feature ID is used to identity the counts in the output table. The default, \
suitable for RNA-Seq analysis using an Ensembl GTF file, is gene_id.",
        ),
        ToolInput(
            "additional_attr",
            String(optional=True),
            prefix="--additional-attr=",
            separate_value_from_prefix=False,
            position=1,
            doc="Additional feature attributes, which will be printed as an \
additional column after the primary attribute column but before the counts \
column(s). The default is none, a suitable value to get gene names using an \
Ensembl GTF file is gene_name. To use more than one additional attribute, \
repeat the option in the command line more than once, with a single attribute \
each time, e.g. --additional-attr=gene_name --additional_attr=exon_number.",
        ),
        ToolInput(
            "mode",
            String(optional=True),
            prefix="--mode=",
            separate_value_from_prefix=False,
            position=1,
            doc="Mode to handle reads overlapping more than one feature. \
Possible values for <mode> are union, intersection-strict and \
intersection-nonempty (default: union)",
        ),
        ToolInput(
            "nonunique",
            String(optional=True),
            prefix="--nonunique=",
            separate_value_from_prefix=False,
            position=1,
            doc="Mode to handle reads that align to or are assigned to more \
than one feature in the overlap <mode> of choice (see -m option). <nonunique \
mode> are none and all (default: none)",
        ),
        ToolInput(
            "secondary_alignments",
            String(optional=True),
            prefix="--secondary-alignments=",
            separate_value_from_prefix=False,
            position=1,
            doc="Mode to handle secondary alignments (SAM flag 0x100). <mode> \
can be score and ignore (default: score)",
        ),
        ToolInput(
            "supplementary_alignments",
            String(optional=True),
            prefix="--supplementary-alignments=",
            separate_value_from_prefix=False,
            position=1,
            doc="Mode to handle supplementary/chimeric alignments (SAM flag \
0x800). <mode> can be score and ignore (default: score)",
        ),
        ToolInput(
            "samout",
            String(optional=True),
            prefix="--samout=",
            separate_value_from_prefix=False,
            position=1,
            doc="write out all SAM alignment records into an output SAM file \
called <samout>, annotating each line with its assignment to a feature or a \
special counter (as an optional field with tag ‘XF’)",
        ),
    ]
