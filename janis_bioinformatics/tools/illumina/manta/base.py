from abc import ABC, abstractmethod
from typing import List

from janis_bioinformatics.data_types import FastaWithDict, VcfTabix, BamBai, Bam
from janis_bioinformatics.tools import BioinformaticsTool

from janis import ToolOutput, ToolInput, ToolArgument, Boolean, String, File, Directory, Stdout, Filename, \
    InputSelector, Int
from janis.unix.data_types.tsv import Tsv
from janis.utils.metadata import ToolMetadata


class MantaBase(BioinformaticsTool, ABC):

    @staticmethod
    def tool_provider():
        return "illumina"

    @staticmethod
    def tool():
        return "manta-germline"

    @staticmethod
    def base_command():
        return None

    def inputs(self) -> List[ToolInput]:
        return [*self.config_inputs, *self.running_inputs]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("python", File(), glob=InputSelector("runDir", suffix="/runWorkflow.py")),
            ToolOutput("pickle", File(), glob=InputSelector("runDir", suffix="/runWorkflow.py.config.pickle")),

            ToolOutput("candidateSV", VcfTabix(),
                       glob=InputSelector("runDir", suffix="/results/variants/candidateSV.vcf.gz")),
            ToolOutput("candidateSmallIndels", VcfTabix(),
                       glob=InputSelector("runDir", suffix="/results/variants/candidateSmallIndels.vcf.gz")),
            ToolOutput("diploidSV", VcfTabix(),
                       glob=InputSelector("runDir", suffix="/results/variants/diploidSV.vcf.gz")),

            ToolOutput("alignmentStatsSummary", VcfTabix(),
                       glob=InputSelector("runDir", suffix="/results/stats/alignmentStatsSummary.txt")),
            ToolOutput("svCandidateGenerationStats", Tsv(),
                       glob=InputSelector("runDir", suffix="/results/stats/svCandidateGenerationStats.tsv")),
            ToolOutput("svLocusGraphStats", VcfTabix(),
                       glob=InputSelector("runDir", suffix="/results/stats/svLocusGraphStats.tsv")),

        ]

    def arguments(self) -> List[ToolArgument]:
        return [
            ToolArgument("configManta.py", position=0, shell_quote=False),
            ToolArgument(InputSelector("runDir", prefix="&& ", suffix="/runWorkflow.py"), position=2, shell_quote=False)
        ]

    @staticmethod
    def requirements():
        from cwlgen import ShellCommandRequirement
        return [ShellCommandRequirement()]

    @staticmethod
    @abstractmethod
    def docker():
        raise Exception("Strelka version must override docker command")

    def friendly_name(self):
        return "Manta"

    def metadata(self):
        from datetime import date
        return ToolMetadata(
            creator="Michael Franklin",
            maintainer="Michael Franklin",
            maintainer_email="michael.franklin@petermac.org",
            date_created=date(2019, 2, 12),
            date_updated=date(2019, 2, 19),
            institution="Illumina",
            doi=" doi:10.1093/bioinformatics/btv710",
            citation="Chen, X. et al. (2016) Manta: rapid detection of structural variants and indels for germline and "
                     "cancer sequencing applications. Bioinformatics, 32, 1220-1222. doi:10.1093/bioinformatics/btv710",
            keywords=["illumina", "manta", "variant caller"],
            documentation_url="https://github.com/Illumina/manta",
            documentation="""
Manta calls structural variants (SVs) and indels from mapped paired-end sequencing reads. 
It is optimized for analysis of germline variation in small sets of individuals and somatic 
variation in tumor/normal sample pairs. Manta discovers, assembles and scores large-scale SVs, 
medium-sized indels and large insertions within a single efficient workflow. The method is 
designed for rapid analysis on standard compute hardware: NA12878 at 50x genomic coverage is 
analyzed in less than 20 minutes on a 20 core server, and most WGS tumor/normal analyses 
can be completed within 2 hours. Manta combines paired and split-read evidence during SV 
discovery and scoring to improve accuracy, but does not require split-reads or successful 
breakpoint assemblies to report a variant in cases where there is strong evidence otherwise. 

It provides scoring models for germline variants in small sets of diploid samples and somatic 
variants in matched tumor/normal sample pairs. There is experimental support for analysis of 
unmatched tumor samples as well. Manta accepts input read mappings from BAM or CRAM files and 
reports all SV and indel inferences in VCF 4.1 format. See the user guide for a full description 
of capabilities and limitations.""".strip()
        )

    config_inputs = [
        ToolInput("config", File(optional=True), prefix="--config", position=1, shell_quote=False,
                  doc="provide a configuration file to override defaults in global config file "
                      "(/opt/conda/share/manta-1.2.1-0/bin/configManta.py.ini)"),
        ToolInput("bam", BamBai(), prefix="--bam", position=1, shell_quote=False,
                  doc="FILE Normal sample BAM or CRAM file. May be specified more than once, multiple inputs "
                      "will be treated as each BAM file representing a different sample. [optional] (no default)"),
        ToolInput("runDir", Filename(), prefix="--runDir", position=1, shell_quote=False,
                  doc="Run script and run output will be written to this directory [required] "
                      "(default: MantaWorkflow)"),
        ToolInput("reference", FastaWithDict(), prefix="--referenceFasta", position=1,
                  shell_quote=False, doc="samtools-indexed reference fasta file [required]"),

        ToolInput("tumorBam", Bam(optional=True), prefix="--tumorBam", position=1, shell_quote=False,
                  doc="Tumor sample BAM or CRAM file. Only up to one tumor bam file accepted. [optional=null]"),
        ToolInput("exome", Boolean(optional=True), prefix="--exome", position=1, shell_quote=False,
                  doc="Set options for WES input: turn off depth filters"),
        ToolInput("rna", Bam(optional=True), prefix="--rna", position=1, shell_quote=False,
                  doc="Set options for RNA-Seq input. Must specify exactly one bam input file"),
        ToolInput("unstrandedRNA", File(optional=True), prefix="--unstrandedRNA", position=1, shell_quote=False,
                  doc="Set if RNA-Seq input is unstranded: Allows splice-junctions on either strand"),
        ToolInput("outputContig", File(optional=True), prefix="--outputContig", position=1, shell_quote=False,
                  doc="Output assembled contig sequences in VCF file"),
    ]

    running_inputs = [
        ToolInput("mode", String(default="local", optional=True), prefix="--mode", position=3, shell_quote=False,
                  doc="(-m) select run mode (local|sge)"),
        ToolInput("jobs", Int(optional=True), prefix="--jobs", position=3, shell_quote=False,
                  doc="(-j) number of jobs, must be an integer or 'unlimited' "
                      "(default: Estimate total cores on this node for local mode, 128 for sge mode)"),
        ToolInput("quiet", Boolean(optional=True, default=True), prefix="--quiet", position=3, shell_quote=False,
                  doc="Don't write any log output to stderr "
                      "(but still write to workspace/pyflow.data/logs/pyflow_log.txt)"),
        ToolInput("queue", String(optional=True), prefix="--queue", position=3, shell_quote=False,
                  doc="(-q) specify scheduler queue name"),

        ToolInput("memgb", Int(optional=True), prefix="--memGb", position=3, shell_quote=False,
                  doc="(-g) gigabytes of memory available to run workflow -- only meaningful in local mode, "
                      "must be an integer (default: Estimate the total memory for this node for local  mode, "
                      "'unlimited' for sge mode)"),
        # ToolInput("dryRun", Boolean(optional=True), prefix="--dryRun", position=3, shell_quote=False,
        #           doc="(-d) dryRun workflow code without actually running command - tasks"),
        ToolInput("maxTaskRuntime", String(optional=True), prefix="--maxTaskRuntime", position=3, shell_quote=False,
                  doc="(format: hh:mm:ss) Specify scheduler max runtime per task, argument is "
                      "provided to the 'h_rt' resource limit if using SGE (no default)"),
    ]
