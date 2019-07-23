from abc import ABC
from datetime import datetime
from typing import Dict, Any

from janis import get_value_for_hints_and_ordered_resource_tuple
from janis_core import (
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    InputSelector,
    Filename,
    ToolMetadata,
    CpuSelector,
    ToolArgument,
    CaptureType,
    StringFormatter,
)
from janis_unix import Tsv

from janis_bioinformatics.data_types import (
    BamBai,
    Bed,
    FastaWithDict,
    VcfTabix,
    BedTabix,
)
from janis_bioinformatics.tools.illumina.illuminabase import IlluminaToolBase

CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 16,
            CaptureType.THIRTYX: 32,
            CaptureType.NINETYX: 40,
            CaptureType.THREEHUNDREDX: 40,
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


class StrelkaSomaticBase(IlluminaToolBase, ABC):


    @staticmethod
    def tool() -> str:
        return "strelka_somatic"

    def friendly_name(self) -> str:
        return "Strelka (Somatic)"

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

    @staticmethod
    def base_command():
        return

    def arguments(self):
        return [
            ToolArgument("configureStrelkaSomaticWorkflow.py", position=0),
            ToolArgument(
                StringFormatter(";") + InputSelector("rundir") + "/runWorkflow.py",
                position=2,
                shell_quote=False,
            ),
            ToolArgument(
                CpuSelector(None),
                prefix="--jobs",
                position=3,
                shell_quote=False,
                doc=" (-j JOBS)  number of jobs, must be an integer or 'unlimited' "
                "(default: Estimate total cores on this node for local mode, 128 for sge mode)",
            ),
        ]

    def inputs(self):
        return [
            # ToolInput(tag="version", input_type=Boolean(), prefix="--version", separate_value_from_prefix=True,
            #           doc="show program's version number and exit"),
            # ToolInput(tag="help", input_type=Boolean(), prefix="--help", separate_value_from_prefix=True,
            #           doc="(-h) show this help message and exit"),
            # ToolInput(tag="allhelp", input_type=Boolean(), prefix="--allHelp", separate_value_from_prefix=True,
            #           doc="show all extended/hidden options"),
            ToolInput(
                tag="normalBam",
                input_type=BamBai(),
                prefix="--normalBam=",
                separate_value_from_prefix=False,
                position=1,
                doc="Normal sample BAM or CRAM file. (no default)",
            ),
            ToolInput(
                tag="tumorBam",
                input_type=BamBai(),
                prefix="--tumourBam=",
                separate_value_from_prefix=False,
                position=1,
                doc="(--tumorBam)  Tumor sample BAM or CRAM file. [required] (no default)",
            ),
            ToolInput(
                tag="reference",
                input_type=FastaWithDict(),
                prefix="--referenceFasta=",
                position=1,
                separate_value_from_prefix=False,
                doc=" samtools-indexed reference fasta file [required]",
            ),
            ToolInput(
                tag="rundir",
                input_type=Filename(),
                prefix="--runDir=",
                separate_value_from_prefix=False,
                position=1,
                doc="Name of directory to be created where all workflow scripts and output will be written. "
                "Each analysis requires a separate directory. (default: StrelkaSomaticWorkflow)",
            ),
            ToolInput(
                tag="region",
                input_type=Bed(optional=True),
                prefix="--region=",
                separate_value_from_prefix=False,
                position=1,
                doc="Limit the analysis to one or more genome region(s) for debugging purposes. If this argument "
                "is provided multiple times the union of all specified regions will be analyzed. All regions "
                "must be non-overlapping to get a meaningful result. Examples: '--region chr20' "
                "(whole chromosome), '--region chr2:100-2000 --region chr3:2500-3000' (two regions)'. "
                "If this option is specified (one or more times) together with the 'callRegions' BED file,"
                "then all region arguments will be intersected with the callRegions BED track.",
            ),
            ToolInput(
                tag="config",
                input_type=File(optional=True),
                prefix="--config=",
                separate_value_from_prefix=False,
                position=1,
                doc="provide a configuration file to override defaults in global config file "
                "(/opt/strelka/bin/configureStrelkaSomaticWorkflow.py.ini)",
            ),
            ToolInput(
                tag="outputcallableregions",
                input_type=Bed(optional=True),
                prefix="--outputCallableRegions",
                position=1,
                separate_value_from_prefix=True,
                doc=" Output a bed file describing somatic callable regions of the genome",
            ),
            ToolInput(
                tag="indelCandidates",
                input_type=VcfTabix(optional=True),
                prefix="--indelCandidates=",
                position=1,
                separate_value_from_prefix=False,
                doc="Specify a VCF of candidate indel alleles. These alleles are always evaluated "
                "but only reported in the output when they are inferred to exist in the sample. "
                "The VCF must be tabix indexed. All indel alleles must be left-shifted/normalized, "
                "any unnormalized alleles will be ignored. This option may be specified more than once, "
                "multiple input VCFs will be merged. (default: None)",
            ),
            ToolInput(
                tag="forcedgt",
                input_type=File(optional=True),
                prefix="--forcedGT=",
                separate_value_from_prefix=False,
                position=1,
                doc="Specify a VCF of candidate alleles. These alleles are always evaluated and reported even "
                "if they are unlikely to exist in the sample. The VCF must be tabix indexed. All indel "
                "alleles must be left- shifted/normalized, any unnormalized allele will trigger a runtime "
                "error. This option may be specified more than once, multiple input VCFs will be merged. "
                "Note that for any SNVs provided in the VCF, the SNV site will be reported (and for gVCF, "
                "excluded from block compression), but the specific SNV alleles are ignored. (default: None)",
            ),
            ToolInput(
                tag="targeted",
                input_type=Boolean(optional=True),
                prefix="--targeted",
                separate_value_from_prefix=True,
                position=1,
                doc="(--exome)  Set options for exome or other targeted input: "
                "note in particular that this flag turns off high-depth filters",
            ),
            ToolInput(
                tag="callRegions",
                input_type=BedTabix(optional=True),
                prefix="--callRegions=",
                separate_value_from_prefix=False,
                position=1,
                doc="Optionally provide a bgzip-compressed/tabix-indexed BED file containing the set of "
                "regions to call. No VCF output will be provided outside of these regions. "
                "The full genome will still be used to estimate statistics from the input "
                "(such as expected depth per chromosome). Only one BED file may be specified. "
                "(default: call the entire genome)",
            ),
            ToolInput(
                tag="noisevcf",
                input_type=File(optional=True),
                prefix="--noiseVcf=",
                separate_value_from_prefix=False,
                position=1,
                doc="Noise vcf file (submit argument multiple times for more than one file)",
            ),
            ToolInput(
                tag="scansizemb",
                input_type=Int(optional=True),
                prefix="--scanSizeMb=",
                separate_value_from_prefix=False,
                position=1,
                doc="Maximum sequence region size (in megabases) scanned by each "
                "task during genome variant calling. (default: 12)",
            ),
            ToolInput(
                tag="callmemmb",
                input_type=Int(optional=True),
                prefix="--callMemMb=",
                position=1,
                separate_value_from_prefix=False,
                doc="Set variant calling task memory limit (in megabytes). It is not recommended to change the "
                "default in most cases, but this might be required for a sample of unusual depth.",
            ),
            ToolInput(
                tag="retaintempfiles",
                input_type=Boolean(optional=True),
                default=False,
                position=1,
                prefix="--retainTempFiles",
                separate_value_from_prefix=True,
                doc="Keep all temporary files (for workflow debugging)",
            ),
            ToolInput(
                tag="disableevs",
                input_type=Boolean(optional=True),
                prefix="--disableEVS",
                position=1,
                separate_value_from_prefix=True,
                doc="Disable empirical variant scoring (EVS).",
            ),
            ToolInput(
                tag="reportevsfeatures",
                input_type=Boolean(optional=True),
                prefix="--reportEVSFeatures",
                position=1,
                separate_value_from_prefix=True,
                doc=" Report all empirical variant scoring features in VCF output.",
            ),
            ToolInput(
                tag="snvscoringmodelfile",
                input_type=File(optional=True),
                prefix="--snvScoringModelFile=",
                position=1,
                separate_value_from_prefix=False,
                doc=" Provide a custom empirical scoring model file for SNVs "
                "(default: /opt/strelka/share/config/somaticSNVScoringM odels.json)",
            ),
            ToolInput(
                tag="indelscoringmodelfile",
                input_type=File(optional=True),
                prefix="--indelScoringModelFile=",
                position=1,
                separate_value_from_prefix=False,
                doc=" Provide a custom empirical scoring model file for indels "
                "(default: /opt/strelka/share/config/somaticInde lScoringModels.json)",
            ),
            ToolInput(
                "mode",
                String(optional=True),
                default="local",
                prefix="--mode",
                position=3,
                shell_quote=False,
                doc="(-m MODE)  select run mode (local|sge)",
            ),
            ToolInput(
                "queue",
                String(optional=True),
                prefix="--queue",
                position=3,
                shell_quote=False,
                doc="(-q QUEUE) specify scheduler queue name",
            ),
            ToolInput(
                "memGb",
                String(optional=True),
                prefix="--memGb",
                position=3,
                shell_quote=False,
                doc=" (-g MEMGB) gigabytes of memory available to run workflow "
                "-- only meaningful in local mode, must be an integer (default: Estimate the total "
                "memory for this node for local mode, 'unlimited' for sge mode)",
            ),
            ToolInput(
                "quiet",
                Boolean(optional=True),
                prefix="--quiet",
                position=3,
                shell_quote=False,
                doc="Don't write any log output to stderr "
                "(but still write to workspace/pyflow.data/logs/pyflow_log.txt)",
            ),
            # ToolInput("mailTo", String(optional=True), prefix="--mailTo", position=3, shell_quote=False,
            #           doc="(-e) send email notification of job completion status to this address "
            #               "(may be provided multiple times for more than one email address)"),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "configPickle",
                File(),
                glob=InputSelector("rundir") + "/runWorkflow.py.config.pickle",
            ),
            ToolOutput(
                "script", File(), glob=InputSelector("rundir") + "/runWorkflow.py"
            ),
            ToolOutput(
                "stats",
                Tsv(),
                glob=InputSelector("rundir") + "/results/stats/runStats.tsv",
                doc="A tab-delimited report of various internal statistics from the variant calling process: "
                "Runtime information accumulated for each genome segment, excluding auxiliary steps such "
                "as BAM indexing and vcf merging. Indel candidacy statistics",
            ),
            ToolOutput(
                "indels",
                VcfTabix(),
                glob=InputSelector("rundir")
                + "/results/variants/somatic.indels.vcf.gz",
                doc="",
            ),
            ToolOutput(
                "snvs",
                VcfTabix(),
                glob=InputSelector("rundir") + "/results/variants/somatic.snvs.vcf.gz",
                doc="",
            ),
        ]

    def metadata(self):
        return ToolMetadata(
            dateCreated=datetime(2019, 5, 27, 15, 7, 45),
            dateUpdated=datetime(2019, 5, 27, 15, 7, 45),
            documentation="""Usage: configureStrelkaSomaticWorkflow.py [options]
Version: 2.9.10
This script configures Strelka somatic small variant calling.
You must specify an alignment file (BAM or CRAM) for each sample of a matched tumor-normal pair.
Configuration will produce a workflow run script which can execute the workflow on a single node or through
sge and resume any interrupted execution.""",
        )
