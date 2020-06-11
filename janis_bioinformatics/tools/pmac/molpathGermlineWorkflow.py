from datetime import date

from janis_core import (
    File,
    String,
    Array,
    InputSelector,
    WorkflowMetadata,
    ScatterDescription,
    ScatterMethods,
    InputDocumentation,
    InputQualityType,
)

from janis_bioinformatics.data_types import (
    FastaWithDict,
    VcfTabix,
    FastqGzPair,
    Bed,
    Bam,
    BamBai,
)
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow
from janis_bioinformatics.tools.babrahambioinformatics import FastQC_0_11_5
from janis_bioinformatics.tools.common import (
    BwaAligner,
    MergeAndMarkBams_4_1_3,
    GATKBaseRecalBam_4_1_3,
    SplitMultiAlleleNormaliseVcf,
)
from janis_bioinformatics.tools.gatk4 import Gatk4HaplotypeCaller_4_1_3
from janis_bioinformatics.tools.papenfuss import Gridss_2_6_2
from janis_bioinformatics.tools.pmac import (
    ParseFastqcAdaptors,
    AnnotateDepthOfCoverage_0_1_0,
    PerformanceSummaryTargeted_0_1_0,
    AddBamStatsGermline_0_1_0,
)
from janis_bioinformatics.tools.variantcallers import GatkGermlineVariantCaller_4_1_3


class MolpathGermline_1_0_0(BioinformaticsWorkflow):
    def id(self):
        return "MolpathGermlineWorkflow"

    def friendly_name(self):
        return "Molpath Germline Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v1.0.0", contributors=["Jiaan Yu"])

    def constructor(self):

        # Inputs
        self.input("sample_name", String)
        self.input("fastqs", Array(FastqGzPair))
        self.input("reference", FastaWithDict)
        self.input("region_bed", Bed)
        self.input("region_bed_extended", Bed)
        self.input("region_bed_annotated", Bed)
        self.input("genecoverage_bed", Bed)
        self.input("black_list", Bed(optional=True))
        self.input("snps_dbsnp", VcfTabix)
        self.input("snps_1000gp", VcfTabix)
        self.input("known_indels", VcfTabix)
        self.input("mills_indels", VcfTabix)

        # fastqc
        self.step(
            "fastqc", FastQC_0_11_5(reads=self.fastqs, threads=4), scatter="reads"
        )
        # get the overrepresentative sequence from fastqc
        self.step(
            "getfastqc_adapters",
            ParseFastqcAdaptors(fastqc_datafiles=self.fastqc.datafile,),
            scatter="fastqc_datafiles",
        )
        # align and generate sorted index bam
        self.step(
            "align_and_sort",
            BwaAligner(
                fastq=self.fastqs,
                reference=self.reference,
                sample_name=self.sample_name,
                sortsam_tmpDir=".",
                cutadapt_adapter=self.getfastqc_adapters,
                cutadapt_removeMiddle3Adapter=self.getfastqc_adapters,
            ),
            scatter=["fastq", "cutadapt_adapter", "cutadapt_removeMiddle3Adapter"],
        )
        # merge into one bam and markdups
        self.step(
            "merge_and_mark",
            MergeAndMarkBams_4_1_3(
                bams=self.align_and_sort.out, sampleName=self.sample_name
            ),
        )
        # performance: doc
        self.step(
            "annotate_doc",
            AnnotateDepthOfCoverage_0_1_0(
                bam=self.merge_and_mark.out,
                bed=self.region_bed_annotated,
                reference=self.reference,
                sample_name=self.sample_name,
            ),
        )
        # performance
        self.step(
            "performance_summary",
            PerformanceSummaryTargeted_0_1_0(
                bam=self.merge_and_mark.out,
                bed=self.genecoverage_bed,
                sample_name=self.sample_name,
            ),
        )
        # gridss
        self.step(
            "gridss",
            Gridss_2_6_2(
                bams=self.merge_and_mark.out,
                reference=self.reference,
                blacklist=self.black_list,
                tmpdir=".",
            ),
        )
        # post gridss r script here
        # self.step("gridss_post_r", )
        # gatk bqsr bam
        self.step(
            "bqsr",
            GATKBaseRecalBam_4_1_3(
                bam=self.merge_and_mark.out,
                intervals=self.region_bed_extended,
                reference=self.reference,
                snps_dbsnp=self.snps_dbsnp,
                snps_1000gp=self.snps_1000gp,
                known_indels=self.known_indels,
                mills_indels=self.mills_indels,
            ),
        )
        # haploytype caller
        self.step(
            "haplotype_caller",
            Gatk4HaplotypeCaller_4_1_3(
                inputRead=self.bqsr.out,
                intervals=self.region_bed_extended,
                reference=self.reference,
                dbsnp=self.snps_dbsnp,
                pairHmmImplementation="LOGLESS_CACHING",
            ),
        )
        self.step(
            "splitnormalisevcf",
            SplitMultiAlleleNormaliseVcf(
                compressedVcf=self.haplotype_caller.out, reference=self.reference
            ),
        )
        self.step(
            "addbamstats",
            AddBamStatsGermline_0_1_0(
                bam=self.merge_and_mark.out, vcf=self.splitnormalisevcf.out
            ),
        )
        # output
        self.output("fastq_qc", source=self.fastqc.out, output_folder="QC")

        self.output("markdups_bam", source=self.merge_and_mark.out, output_folder="BAM")

        self.output("doc", source=self.annotate_doc.out, output_folder="PERFORMANCE")
        self.output(
            "summary", source=self.performance_summary.out, output_folder="PERFORMANCE"
        )
        self.output(
            "gene_summary",
            source=self.performance_summary.geneFileOut,
            output_folder="PERFORMANCE",
        )
        self.output(
            "region_summary",
            source=self.performance_summary.regionFileOut,
            output_folder="PERFORMANCE",
        )

        self.output("gridss_vcf", source=self.gridss.out, output_folder="SV")
        self.output("gridss_bam", source=self.gridss.assembly, output_folder="SV")

        self.output("hap_vcf", source=self.haplotype_caller.out, output_folder="VCF")
        self.output("hap_bam", source=self.haplotype_caller.bam, output_folder="VCF")
        self.output("normalise_vcf", source=self.addbamstats.out, output_folder="VCF")
