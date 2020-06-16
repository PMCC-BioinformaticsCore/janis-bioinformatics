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
    Int,
)
from janis_unix.data_types import TextFile
from janis_unix.tools import UncompressArchive
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
from janis_bioinformatics.tools.bcftools import BcfToolsSort_1_9
from janis_bioinformatics.tools.common import (
    BwaAligner,
    MergeAndMarkBams_4_1_3,
    GATKBaseRecalBQSRWorkflow_4_1_3,
    SplitMultiAlleleNormaliseVcf,
)
from janis_bioinformatics.tools.gatk4 import Gatk4HaplotypeCaller_4_1_3
from janis_bioinformatics.tools.htslib import BGZip_1_9, TabixLatest
from janis_bioinformatics.tools.papenfuss import Gridss_2_6_2
from janis_bioinformatics.tools.pmac import (
    ParseFastqcAdaptors,
    AnnotateDepthOfCoverage_0_1_0,
    PerformanceSummaryTargeted_0_1_0,
    CombineVariants_0_0_5,
    AddBamStatsGermline_0_1_0,
)
from janis_bioinformatics.tools.variantcallers import (
    GatkSomaticVariantCallerTumorOnlyTargeted,
)
from janis_bioinformatics.tools.vcflib import VcfLength_1_0_1, VcfFilter_1_0_1
from janis_bioinformatics.tools.igvtools import IgvIndexFeature_2_5_3

# from janis_molpath.tools.pathos import NormaliseVcf_1_5_4, Vcf2Tsv_1_5_4
# from janis_molpath.tools.scripts.postgridss import GRIDSSProcessOutput


class MolpathTumorOnly_1_0_0(BioinformaticsWorkflow):
    def id(self):
        return "MolpathTumorOnlyWorkflow"

    def friendly_name(self):
        return "Molpath Tumor Only Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v1.0.0", contributors=["Jiaan Yu"])

    def constructor(self):

        # Inputs
        self.input("sample_name", String)
        self.input("fastqs", Array(FastqGzPair))
        self.input("seqrun", String, doc="SeqRun Name (for Vcf2Tsv)")
        self.input("reference", FastaWithDict)
        self.input("region_bed", Bed)
        self.input("region_bed_extended", Bed)
        self.input("region_bed_annotated", Bed)
        self.input("genecoverage_bed", Bed)
        self.input("genome_file", TextFile)
        self.input("panel_name", String)
        self.input("vcfcols", TextFile)
        self.input("black_list", Bed(optional=True))
        self.input("snps_dbsnp", VcfTabix)
        self.input("snps_1000gp", VcfTabix)
        self.input("known_indels", VcfTabix)
        self.input("mills_indels", VcfTabix)
        self.input("mutalyzer_server", String)
        self.input("pathos_db", String)
        self.input("maxRecordsInRam", Int)
        # tumor only
        self.input("gnomad", VcfTabix)
        self.input("panel_of_normals", VcfTabix(optional=True))

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
                bams=self.align_and_sort.out,
                sampleName=self.sample_name,
                maxRecordsInRam=self.maxRecordsInRam,
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
                genome_file=self.genome_file,
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
        # post gridss r for tumor only + tumor only mode
        # self.step("gridss_post_r", GRIDSSProcessOutput(inp=self.gridss.out))
        # gatk bqsr bam
        self.step(
            "bqsr",
            GATKBaseRecalBQSRWorkflow_4_1_3(
                bam=self.merge_and_mark.out,
                intervals=self.region_bed_extended,
                reference=self.reference,
                snps_dbsnp=self.snps_dbsnp,
                snps_1000gp=self.snps_1000gp,
                known_indels=self.known_indels,
                mills_indels=self.mills_indels,
            ),
        )
        # mutect2
        self.step(
            "mutect2",
            GatkSomaticVariantCallerTumorOnlyTargeted(
                bam=self.bqsr.out,
                intervals=self.region_bed_extended,
                reference=self.reference,
                gnomad=self.gnomad,
                panel_of_normals=self.panel_of_normals,
            ),
        )
        # haplotypecaller to do: take base recal away from the
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
        # combine variants
        self.step(
            "combinevariants",
            CombineVariants_0_0_5(
                vcfs=[self.splitnormalisevcf.out, self.mutect2.out],
                type="germline",
                columns=["AD", "DP", "AF", "GT"],
            ),
        )
        self.step("compressvcf", BGZip_1_9(file=self.combinevariants.out))
        self.step("sortvcf", BcfToolsSort_1_9(vcf=self.compressvcf.out))
        self.step("uncompressvcf", UncompressArchive(file=self.sortvcf.out))
        # addbamstats
        self.step(
            "addbamstats",
            AddBamStatsGermline_0_1_0(
                bam=self.merge_and_mark.out, vcf=self.uncompressvcf.out
            ),
        )
        # Molpath specific processes
        self.step("compressvcf2", BGZip_1_9(file=self.addbamstats.out))
        self.step("tabixvcf", TabixLatest(inp=self.compressvcf2.out))
        self.step(
            "calculate_variant_length",
            VcfLength_1_0_1(vcf=self.tabixvcf.out),
            doc="Add the length column for the output of AddBamStats",
        )

        filter_for_variants = self.input("filter_for_vcfs", str, default="length > 150")
        self.step(
            "filter_variants_1_failed",
            VcfFilter_1_0_1(
                vcf=self.calculate_variant_length.out, info_filter=filter_for_variants
            ),
        )
        self.step(
            "filter_variants_1",
            VcfFilter_1_0_1(
                vcf=self.calculate_variant_length.out,
                info_filter=filter_for_variants,
                invert=True,  # -v param
            ),
        )

        # Jiaan: copy over from the FRCP, can take the block comment out
        # # This one is the in-house molpath step
        # self.step(
        #     "normalise_vcfs",
        #     NormaliseVcf_1_5_4(
        #         pathos_version=self.pathos_db,
        #         mutalyzer=self.mutalyzer_server,  # mutalyzer="https://vmpr-res-mutalyzer1.unix.petermac.org.au",
        #         rdb=self.pathos_db,  # rdb="pa_uat",
        #         inp=self.filter_variants_1.out,
        #     ),
        # )

        # # repeat remove 150bp variants (workaround for normalise_vcf bug)
        # self.step(
        #     "filter_variants_2_failed",
        #     VcfFilter_1_0_1(
        #         vcf=self.normalise_vcfs.out, info_filter=filter_for_variants
        #     ),
        # )
        # self.step(
        #     "filter_variants_2",
        #     VcfFilter_1_0_1(
        #         vcf=self.normalise_vcfs.out,
        #         info_filter=filter_for_variants,
        #         invert=True,  # -v param
        #     ),
        # )

        # self.step(
        #     "convert_to_tsv",
        #     Vcf2Tsv_1_5_4(
        #         pathos_version=self.pathos_db,
        #         inp=self.filter_variants_2.out,
        #         sample=self.sample_name,
        #         columns=self.vcfcols,
        #         seqrun=self.seqrun,
        #     ),
        # )

        # self.step(
        #     "index_with_igvtools", IgvIndexFeature_2_5_3(inp=self.filter_variants_2.out)
        # )

        # output
        self.output("fastq_qc", source=self.fastqc.out, output_folder="QC")

        self.output("markdups_bam", source=self.merge_and_mark.out, output_folder="BAM")

        self.output(
            "doc_out", source=self.annotate_doc.out, output_folder="PERFORMANCE"
        )
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

        self.output(
            "haplotypecaller_vcf",
            source=self.haplotype_caller.out,
            output_folder="VCF",
        )
        self.output(
            "haplotypecaller_bam",
            source=self.haplotype_caller.bam,
            output_folder="VCF",
        )
        self.output(
            "haplotypecaller_norm",
            source=self.splitnormalisevcf.out,
            output_folder="VCF",
        )
        self.output("mutect2_vcf", source=self.mutect2.variants, output_folder="VCF")
        self.output("mutect2_bam", source=self.mutect2.out_bam, output_folder="VCF")
        self.output("mutect2_norm", source=self.mutect2.out, output_folder="VCF")
        self.output("addbamstats_vcf", source=self.addbamstats.out)
        # what more output to save?
        # self.output("final_vcf", source=self.filter_variants_2.out)
        # self.output("tsv", source=self.convert_to_tsv.out)
