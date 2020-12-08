from abc import ABC
from typing import List, Dict, Any

from janis_core import get_value_for_hints_and_ordered_resource_tuple, ToolArgument
from janis_core import (
    ToolOutput,
    ToolInput,
    Boolean,
    Int,
    String,
    File,
    Array,
    Float,
    Stdout,
    CaptureType,
)
from janis_bioinformatics.data_types import Vcf, CompressedVcf
from ..bcftoolstoolbase import BcfToolsToolBase
from janis_core import ToolMetadata


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
            CaptureType.THIRTYX: 32,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class BcfToolsViewBase(BcfToolsToolBase, ABC):
    def bind_metadata(self):
        from datetime import date

        self.metadata.contributors = ["Michael Franklin"]
        self.metadata.dateCreated = date(2019, 1, 24)
        self.metadata.dateUpdated = date(2019, 1, 24)
        self.metadata.doi = "http://www.ncbi.nlm.nih.gov/pubmed/19505943"
        self.metadata.citation = (
            "Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R, "
            "and 1000 Genome Project Data Processing Subgroup, The Sequence alignment/map (SAM) "
            "format and SAMtools, Bioinformatics (2009) 25(16) 2078-9"
        )
        self.metadata.documentationUrl = (
            "https://samtools.github.io/bcftools/bcftools.html#view"
        )
        self.metadata.documentation = """________________________________\n 
        View, subset and filter VCF or BCF files by position and filtering expression
        Convert between VCF and BCF. Former bcftools subset."""

    def tool(self):
        return "bcftoolsview"

    def friendly_name(self):
        return "BCFTools: View"

    def base_command(self):
        return ["bcftools", "view"]

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

    def inputs(self) -> List[ToolInput]:
        return [ToolInput("file", CompressedVcf(), position=2), *self.additional_inputs]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Stdout(CompressedVcf()))]

    def arguments(self):
        return [
            # Ensures the output is compressed
            ToolArgument(
                "z",
                prefix="--output-type",
                position=1,
                doc="(-O) [<b|u|z|v>] b: compressed BCF, u: uncompressed BCF, "
                "z: compressed VCF, v: uncompressed VCF [v]",
            )
        ]

    additional_inputs = [
        ToolInput(
            "dropGenotypes",
            Boolean(optional=True),
            prefix="--drop-genotypes",
            position=1,
            doc="(-G) drop individual genotype information (after subsetting if -s option set)",
        ),
        ToolInput(
            "headerOnly",
            Boolean(optional=True),
            prefix="--header-only",
            position=1,
            doc="(-h) print the header only",
        ),
        ToolInput(
            "noHeader",
            Boolean(optional=True),
            prefix="--no-header",
            position=1,
            doc="(-H) suppress the header in VCF output",
        ),
        ToolInput(
            "compressionLevel",
            Int(optional=True),
            prefix="--compression-level",
            position=1,
            doc="(-l) compression level: 0 uncompressed, 1 best speed, 9 best compression [-1]",
        ),
        ToolInput(
            "noVersion",
            Boolean(optional=True),
            prefix="--no-version",
            position=1,
            doc="do not append version and command line to the header",
        ),
        # Captured by stdout
        # ToolInput(
        #     "outputFilename",
        #     File(optional=True),
        #     prefix="--output-file",
        #     position=1,
        #     doc="(-o) output file name [stdout]",
        # ),
        ToolInput(
            "regions",
            String(optional=True),
            prefix="--regions",
            position=1,
            doc="(-r) restrict to comma-separated list of regions",
        ),
        ToolInput(
            "regionsFile",
            File(optional=True),
            prefix="--regions-file",
            position=1,
            doc="(-R) restrict to regions listed in a file",
        ),
        ToolInput(
            "targets",
            String(optional=True),
            prefix="--targets",
            position=1,
            doc="(-t) similar to -r but streams rather than index-jumps. Exclude regions with '^' prefix",
        ),
        ToolInput(
            "targetsFile",
            File(optional=True),
            prefix="--targets-file",
            position=1,
            doc="(-T) similar to -R but streams rather than index-jumps. Exclude regions with '^' prefix",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            prefix="--threads",
            position=1,
            doc="number of extra output compression threads [0]",
        ),
        ToolInput(
            "trimAltAlleles",
            Boolean(optional=True),
            prefix="--trim-alt-alleles",
            position=1,
            doc="(-a) trim alternate alleles not seen in the subset",
        ),
        ToolInput(
            "noUpdate",
            Boolean(optional=True),
            prefix="--no-update",
            position=1,
            doc="(-I) do not (re)calculate INFO fields for the subset (currently INFO/AC and INFO/AN)",
        ),
        ToolInput(
            "samples",
            Array(String(), optional=True),
            prefix="--samples",
            position=1,
            doc="(-s) comma separated list of samples to include (or exclude with '^' prefix)",
        ),
        ToolInput(
            "samplesFile",
            File(optional=True),
            prefix="--samples-file",
            position=1,
            doc="(-S) file of samples to include (or exclude with '^' prefix)",
        ),
        ToolInput(
            "forceSamples",
            Boolean(optional=True),
            prefix="--force-samples",
            position=1,
            doc="only warn about unknown subset samples",
        ),
        ToolInput(
            "minAc",
            Int(optional=True),
            prefix="--min-ac",
            position=1,
            doc="(-c) minimum count for non-reference (nref), 1st alternate (alt1), least frequent (minor), "
            "most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]",
        ),
        ToolInput(
            "maxAc",
            Int(optional=True),
            prefix="--max-ac",
            position=1,
            doc="(-C) maximum count for non-reference (nref), 1st alternate (alt1), least frequent (minor), "
            "most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]",
        ),
        ToolInput(
            "applyFilters",
            Array(String(), optional=True),
            prefix="--apply-filters",
            position=1,
            doc="(-f) require at least one of the listed FILTER strings (e.g. 'PASS,.'')",
        ),
        ToolInput(
            "genotype",
            String(optional=True),
            prefix="--genotype",
            position=1,
            doc="(-g) [<hom|het|miss>] require one or more hom/het/missing genotype or, if prefixed with '^', "
            "exclude sites with hom/het/missing genotypes",
        ),
        ToolInput(
            "include",
            String(optional=True),
            prefix="--include",
            position=1,
            doc="(-i) select sites for which the expression is true (see man page for details)",
        ),
        ToolInput(
            "exclude",
            String(optional=True),
            prefix="--exclude",
            position=1,
            doc="(-e) exclude sites for which the expression is true (see man page for details)",
        ),
        ToolInput(
            "known",
            Boolean(optional=True),
            prefix="--known",
            position=1,
            doc="(-k) select known sites only (ID is not/is '.')",
        ),
        ToolInput(
            "novel",
            Boolean(optional=True),
            prefix="--novel",
            position=1,
            doc="(-n) select novel sites only (ID is not/is '.')",
        ),
        ToolInput(
            "minAlleles",
            Int(optional=True),
            prefix="--min-alleles",
            position=1,
            doc="(-m) minimum number of alleles listed in REF and ALT (e.g. -m2 -M2 for biallelic sites)",
        ),
        ToolInput(
            "maxAlleles",
            Int(optional=True),
            prefix="--max-alleles",
            position=1,
            doc="(-M) maximum number of alleles listed in REF and ALT (e.g. -m2 -M2 for biallelic sites)",
        ),
        ToolInput(
            "phased",
            Boolean(optional=True),
            prefix="--phased",
            position=1,
            doc="(-p) select sites where all samples are phased",
        ),
        ToolInput(
            "excludePhased",
            Boolean(optional=True),
            prefix="--exclude-phased",
            position=1,
            doc="(-P) exclude sites where all samples are phased",
        ),
        ToolInput(
            "minAf",
            Float(optional=True),
            prefix="--min-af",
            position=1,
            doc="(-q) minimum frequency for non-reference (nref), 1st alternate (alt1), least frequent (minor), "
            "most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]",
        ),
        ToolInput(
            "maxAf",
            Float(optional=True),
            prefix="--max-af",
            position=1,
            doc="(-Q) maximum frequency for non-reference (nref), 1st alternate (alt1), least frequent (minor), "
            "most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]",
        ),
        ToolInput(
            "uncalled",
            Boolean(optional=True),
            prefix="--uncalled",
            position=1,
            doc="(-u) select sites without a called genotype",
        ),
        ToolInput(
            "excludeUncalled",
            Boolean(optional=True),
            prefix="--exclude-uncalled",
            position=1,
            doc="(-U) exclude sites without a called genotype",
        ),
        ToolInput(
            "types",
            Array(String(), optional=True),
            prefix="--types",
            position=1,
            doc="(-v) select comma-separated list of variant types: snps,indels,mnps,other [null]",
        ),
        ToolInput(
            "excludeTypes",
            Array(String(), optional=True),
            prefix="--exclude-types",
            position=1,
            doc="(-V) exclude comma-separated list of variant types: snps,indels,mnps,other [null]",
        ),
        ToolInput(
            "private",
            Boolean(optional=True),
            prefix="--private",
            position=1,
            doc="(-x) select sites where the non-reference alleles are exclusive (private) to the subset samples",
        ),
        ToolInput(
            "excludePrivate",
            Boolean(optional=True),
            prefix="--exclude-private",
            position=1,
            doc="(-X) exclude sites where the non-reference alleles are exclusive (private) to the subset samples",
        ),
    ]
