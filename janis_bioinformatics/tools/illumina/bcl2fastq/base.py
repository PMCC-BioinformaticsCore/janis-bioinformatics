from abc import ABC, abstractmethod
from typing import Any, Dict

from janis_bioinformatics.data_types import FastqGz
from janis_bioinformatics.tools.illumina.illuminabase import IlluminaToolBase
from janis_core import (
    Array,
    Boolean,
    CaptureType,
    CpuSelector,
    Directory,
    File,
    Filename,
    Float,
    InputSelector,
    Int,
    Stdout,
    String,
    ToolArgument,
    ToolInput,
    ToolMetadata,
    ToolOutput,
    WildcardSelector,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_unix.data_types import Csv

CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.CHROMOSOME: 8,
            CaptureType.EXOME: 8,
            CaptureType.THIRTYX: 32,
            CaptureType.NINETYX: 40,
            CaptureType.THREEHUNDREDX: 80,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 8,
            CaptureType.CHROMOSOME: 32,
            CaptureType.EXOME: 32,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Bcl2FastqBase(IlluminaToolBase, ABC):
    def tool(self):
        return "bcl2fastq"

    def tool_provider(self):
        return "Illumina"

    def friendly_name(self):
        return "Bcl2Fastq"

    def base_command(self):
        return "bcl2fastq"

    def arguments(self):
        return [
            ToolArgument(".", prefix="--output-dir", doc="path to demultiplexed output")
        ]

    def inputs(self):
        return [
            ToolInput(
                "runFolderDir",
                input_type=Directory(),
                prefix="-R",
                doc="path to runfolder directory",
            ),
            ToolInput(
                "sampleSheet",
                input_type=Csv(),
                prefix="--sample-sheet",
                doc="path to the sample sheet",
            ),
            ToolInput(
                "loadingThreads",
                input_type=Int(),
                prefix="-r",
                default=4,
                doc="number of threads used for loading BCL data",
            ),
            ToolInput(
                "processingThreads",
                input_type=Int(),
                prefix="-p",
                default=4,
                doc="number of threads used for processing demultiplexed data",
            ),
            ToolInput(
                "writingThreads",
                input_type=Int(),
                prefix="-w",
                default=4,
                doc="number of threads used for writing FASTQ data",
            ),
            *Bcl2FastqBase.additional_inputs,
        ]

    def outputs(self):
        return [
            ToolOutput(
                "unalignedReads",
                output_type=Array(FastqGz()),
                glob=WildcardSelector("*/*.fastq.gz"),
            ),
            ToolOutput(
                "stats", output_type=Array(File()), glob=WildcardSelector("Stats/*")
            ),
            ToolOutput(
                "interop", output_type=Array(File()), glob=WildcardSelector("InterOp/*")
            ),
        ]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 4

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Matthias De Smet (@mattdsm)"],
            dateCreated=date(2020, 3, 5),
            dateUpdated=date(2020, 3, 5),
            institution=None,
            doi=None,
            keywords=["illumina", "demultiplex"],
            documentationUrl="https://support.illumina.com/downloads/bcl2fastq-conversion-software-v2-20.html",
            documentation="BCL to FASTQ file converter",
        )

    additional_inputs = [
        ToolInput(
            "minimumTrimmedReadLength",
            input_type=Int(optional=True),
            prefix="--minimum-trimmed-read-length",
            doc="minimum read length after adapter trimming",
        ),
        ToolInput(
            "useBasesMask",
            input_type=String(optional=True),
            prefix="--use-bases-mask",
            doc="specifies how to use each cycle",
        ),
        ToolInput(
            "maskShortAdapterReads",
            input_type=Int(optional=True),
            prefix="--mask-short-adapter-reads",
            doc="smallest number of remaining bases (after masking bases below the minimum trimmed read length) below which whole read is masked",
        ),
        ToolInput(
            "adapterStringency",
            input_type=Float(optional=True),
            prefix="--adapter-stringency",
            doc="adapter stringency",
        ),
        ToolInput(
            "ignoreMissingBcls",
            input_type=Boolean(optional=True),
            prefix="--ignore-missing-bcls",
            doc="assume 'N'/'#' for missing calls",
        ),
        ToolInput(
            "ignoreMissingFilter",
            input_type=Boolean(optional=True),
            prefix="--ignore-missing-filter",
            doc="assume 'true' for missing filters",
        ),
        ToolInput(
            "ignoreMissingPositions",
            input_type=Boolean(optional=True),
            prefix="--ignore-missing-positions",
            doc="assume [0,i] for missing positions, where i is incremented starting from 0",
        ),
        ToolInput(
            "writeFastqReverseComplement",
            input_type=Boolean(optional=True),
            prefix="--write-fastq-reverse-complement",
            doc="generate FASTQs containing reverse complements of actual data",
        ),
        ToolInput(
            "withFailedReads",
            input_type=Boolean(optional=True),
            prefix="--with-failed-reads",
            doc="include non-PF clusters",
        ),
        ToolInput(
            "createFastqForIndexReads",
            input_type=Boolean(optional=True),
            prefix="--create-fastq-for-index-reads",
            doc="create FASTQ files also for index reads",
        ),
        ToolInput(
            "findAdaptersWithSlidingWindow",
            input_type=Boolean(optional=True),
            prefix="--find-adapters-with-sliding-window",
            doc="find adapters with simple sliding window algorithm",
        ),
        ToolInput(
            "noBgzfCompression",
            input_type=Boolean(optional=True),
            prefix="--no-bgzf-compression",
            doc="turn off BGZF compression for FASTQ files",
        ),
        ToolInput(
            "barcodeMismatches",
            input_type=Int(optional=True),
            prefix="--barcode-mismatches",
            doc="number of allowed mismatches per index",
        ),
        ToolInput(
            "noLaneSplitting",
            input_type=Boolean(optional=True),
            prefix=" --no-lane-splitting",
            doc="do not split fastq files by lane",
        ),
    ]
