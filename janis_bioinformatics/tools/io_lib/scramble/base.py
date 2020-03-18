from abc import ABC
from typing import Any, Dict

from janis_bioinformatics.data_types import Bam, Cram, FastaFai, FastqGzPair, File
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_core import (
    Boolean,
    CaptureType,
    CpuSelector,
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
    get_value_for_hints_and_ordered_resource_tuple,
)

SCRAMBLE_MEM_TUPLE = [
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

SCRAMBLE_CORES_TUPLE = [
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


class ScrambleBase(BioinformaticsTool, ABC):
    def tool(self):
        return "scramble"

    def friendly_name(self):
        return "scramble"

    def tool_provider(self):
        return "io_lib"

    def base_command(self):
        return ["scramble"]

    def inputs(self):
        return [
            ToolInput("inputFilename", Bam(), position=200),
            ToolInput(
                "reference", FastaFai(), prefix="-r", doc="Reference sequence file."
            ),
            ToolInput("outputFilename", Filename(extension=".bam")),
            *ScrambleBase.additional_inputs,
        ]

    def arguments(self):
        return [
            ToolArgument("bam", prefix="-I", doc="input data format"),
            ToolArgument("cram", prefix="-O", doc="output data format"),
            ToolArgument(
                "-9", doc="compression settings for output cram file (-1=fast,-9=best)"
            ),
            ToolArgument(
                "3.0",
                prefix="-V",
                separate_value_from_prefix=False,
                doc="Cram version to output",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out", Stdout(Cram(), stdoutname=InputSelector("outputFilename"))
            )
        ]

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, SCRAMBLE_MEM_TUPLE)
        if val:
            return val
        return 16

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(
            hints, SCRAMBLE_CORES_TUPLE
        )
        if val:
            return val
        return 4

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Matthias De Smet (@mattdsm)"],
            dateCreated=date(2020, 2, 27),
            dateUpdated=date(2020, 2, 27),
            institution="None",
            doi=None,
            keywords=["bam", "cram", "compression"],
            documentationUrl="https://github.com/jkbonfield/io_lib/",
            documentation="scramble: streaming bam to cram compression",
        )

    additional_inputs = [
        ToolInput(
            "range",
            String(optional=True),
            prefix="-R",
            doc="Specifies the refseq:start-end range",
        ),
        ToolInput(
            "maxBases",
            Int(optional=True),
            prefix="-b",
            default=5000000,
            doc="Max. bases per slice, default 5000000.",
        ),
        ToolInput(
            "maxSequences",
            Int(optional=True),
            prefix="-s",
            default=10000,
            doc="Sequences per slice, default 10000.",
        ),
        ToolInput(
            "maxSlicesPerContainer",
            Int(optional=True),
            prefix="-S",
            default=1,
            doc="Slices per container, default 1.",
        ),
        ToolInput(
            "embedReferenceSeuence",
            Boolean(optional=True),
            prefix="-e",
            doc="Embed reference sequence.",
        ),
        ToolInput(
            "nonReferenceBaseEncoding",
            Boolean(optional=True),
            prefix="-x",
            doc="Non-reference based encoding.",
        ),
        ToolInput(
            "multipleReferencesPerSlice",
            Boolean(optional=True),
            prefix="-M",
            doc="Use multiple references per slice.",
        ),
        ToolInput(
            "generateTags",
            Boolean(optional=True),
            prefix="-m",
            doc="Generate MD and NM tags.",
        ),
        ToolInput(
            "lzmaCompression",
            Boolean(optional=True),
            prefix="-Z",
            doc="Also compress using lzma",
        ),
        ToolInput(
            "discardReadNames",
            Boolean(optional=True),
            prefix="-n",
            doc="Discard read names where possible.",
        ),
        ToolInput(
            "preserveAuxTags",
            Boolean(optional=True),
            prefix="-P",
            doc="Preserve all aux tags (incl RG,NM,MD).",
        ),
        ToolInput(
            "preserveAuxTagSizes",
            Boolean(optional=True),
            prefix="-p",
            doc="Preserve aux tag sizes ('i', 's', 'c').",
        ),
        ToolInput(
            "noAddPG",
            Boolean(optional=True),
            prefix="-q",
            doc="Don't add scramble @PG header line.",
        ),
        ToolInput(
            "decodeStop",
            Int(optional=True),
            prefix="-N",
            doc="Stop decoding after 'integer' sequences.",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            default=CpuSelector(),
            prefix="-t",
            doc="Number of threads. (default = 1)",
        ),
        ToolInput(
            "enableQualityBinning",
            Int(optional=True),
            prefix="-B",
            doc="Enable Illumina 8 quality-binning system (lossy).",
        ),
    ]
