from datetime import datetime

from janis_core import (
    WorkflowMetadata,
    String,
    Array,
    WorkflowBuilder,
    StringFormatter,
    Directory,
    File,
    Double,
    Int,
    ScatterDescription,
    ScatterMethod,
)

from janis_bioinformatics.data_types import FastqGzPairedEnd, FastaWithIndexes, Fasta
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow

from janis_bioinformatics.tools.usadellab import TrimmomaticPairedEnd_0_35
from janis_bioinformatics.tools.star import (
    StarAlignReads_2_7_7,
)
from janis_bioinformatics.tools.arriba import (
    ArribaWorkflow_2_1_0,
    ArribaDrawFusions_2_1_0,
)
from janis_bioinformatics.tools.gatk4 import (
    Gatk4SortSam_4_1_4,
    Gatk4MarkDuplicates_4_1_4,
    Gatk4ReorderSam_4_1_4,
    Gatk4SplitNCigarReads_4_1_8_1,
    Gatk4HaplotypeCaller_4_1_4,
    Gatk4VariantFiltration_4_1_4,
)

# from janis_bioinformatics.tools.subread import FeatureCounts_2_0_1


class OncopipeSamplePreparation(BioinformaticsWorkflow):
    def tool_provider(self):
        return "Oncopipe"

    def friendly_name(self):
        return "Oncopipe: sample preparation"

    def id(self) -> str:
        return "OncopipeSamplePreparation"

    def version(self):
        return "v0.1.0"

    def constructor(self):

        self.input("sample_name", String, doc="Sample ID")
        self.input("reads", FastqGzPairedEnd)
        self.input("genome_dir", Directory)
        self.input("reference", FastaWithIndexes)
        self.input("gtf", File)
        self.input("blacklist", File)
        self.input("known_fusions", File)
        self.input("protein_domains_gff", File)
        self.input("cytobands", File)
        self.input("sequence_dictionary", File)

        # optional inputs
        self.input(
            "trimming_options",
            Array(String),
            default=[
                "ILLUMINACLIP:/usr/local/share/trimmomatic-0.35-6/adapters/TruSeq2-PE.fa:2:30:10",
                "LEADING:15",
                "TRAILING:15",
                "SLIDINGWINDOW:4:15",
                "MINLEN:35",
            ],
        )
        self.input("platform", String, default="ILLUMINA")
        self.input("contigs", Array(String(), optional=True))
        self.input("filters", Array(String(), optional=True))
        self.input("call_conf", Double, default=20.0)
        self.input("star_threads", Int(optional=True), 8)

        self.add_trim_and_align()
        self.add_sort_bam()
        self.add_arriba()
        self.add_rna_seq_calling()
        # Allsort is not ready
        # self.add_all_sorts()

    def add_trim_and_align(self):

        self.step(
            "trim",
            TrimmomaticPairedEnd_0_35(
                sampleName=self.sample_name,
                inp=self.reads,
                phred33=True,
                steps=self.trimming_options,
            ),
            doc="Trim reads using Trimmomatic",
        )

        # star alignment steps
        self.step(
            "star_alignment",
            StarAlignReads_2_7_7(
                genomeDir=self.genome_dir,
                genomeLoad="NoSharedMemory",
                twopassMode="Basic",
                readFilesIn=self.trim.pairedOut,
                readFilesCommand="zcat",
                quantMode="GeneCounts",
                outSAMattrRGline=[
                    StringFormatter("ID:{sample}", sample=self.sample_name),
                    StringFormatter("SM:{lane}", lane=self.sample_name),
                    StringFormatter("LB:{library}", library=self.sample_name),
                    StringFormatter("PL:{platform}", platform=self.platform),
                    StringFormatter("PU:1"),
                ],
                outSAMtype=["BAM", "Unsorted"],
                chimOutType=["WithinBAM"],
                runThreadN=self.star_threads,
                limitOutSJcollapsed=3000000,
            ),
            doc="Map reads using the STAR aligner",
        )

        self.output(
            "out_star_gene_counts",
            source=self.star_alignment.out_gene_counts.assert_not_null(),
            output_folder=self.sample_name,
            output_name=StringFormatter(
                "{sample_name}_ReadsPerGene.out.tab", sample_name=self.sample_name
            ),
        )

    def add_sort_bam(self):
        self.step(
            "sortsam",
            Gatk4SortSam_4_1_4(
                bam=self.star_alignment.out_unsorted_bam.assert_not_null(),
                sortOrder="coordinate",
                createIndex=True,
            ),
        )

        self.output(
            "out_sorted_bam",
            source=self.sortsam.out,
            output_folder=self.sample_name,
            output_name=self.sample_name,
        )

    def add_arriba(self):
        self.step(
            "arriba",
            ArribaWorkflow_2_1_0(
                starGenomeDir=self.genome_dir,
                gtf_file=self.gtf,
                reference=self.reference,
                blacklist=self.blacklist,
                known_fusions=self.known_fusions,
                protein_domains_gff=self.protein_domains_gff,
                threads=self.star_threads,
                reads=self.trim.pairedOut,
            ),
        )
        self.step(
            "fusion_plot",
            ArribaDrawFusions_2_1_0(
                fusions=self.arriba.out,
                alignments=self.sortsam.out,
                annotation=self.gtf,
                cytobands=self.cytobands,
                proteinDomains=self.protein_domains_gff,
            ),
        )

        self.output(
            "out_arriba_fusion",
            source=self.arriba.out,
            output_folder=self.sample_name,
            output_name=StringFormatter(
                "{sample_name}_fusion", sample_name=self.sample_name
            ),
        )
        self.output(
            "out_arriba_fusion_discarded",
            source=self.arriba.out_discarded,
            output_folder=self.sample_name,
            output_name=StringFormatter(
                "{sample_name}_fusion_discarded", sample_name=self.sample_name
            ),
        )
        self.output(
            "out_fusion_plot",
            source=self.fusion_plot.out,
            output_folder=self.sample_name,
            output_name=StringFormatter(
                "{sample_name}_fusions", sample_name=self.sample_name
            ),
        )

    # Allsort is not ready
    # def add_all_sorts(self):
    #     self.step(
    #         "featureCounts",
    #         FeatureCounts_2_0_1(
    #             bam=[self.star_alignment.out_unsorted_bam.assert_not_null()],
    #             annotationFile=self.gtf,
    #             attributeType="gene_name",
    #         ),
    #     )

    #     # A script that transforms featurecounts output to allsorts input
    #     self.step(
    #         "prepareAllsortsInput",
    #         PrepareALLSortsInput_0_1_0(
    #             inps=[self.featureCounts.out],
    #             labels=[self.sample_name],
    #             fusion_caller="featureCounts",
    #         ),
    #     )

    #     self.step(
    #         "allsorts",
    #         AllSorts_0_1_0(samples=self.prepareAllsortsInput.out),
    #     )

    #     self.output(
    #         "out_gene_counts",
    #         source=self.featureCounts.out,
    #         output_folder=self.sample_name,
    #         output_name=StringFormatter(
    #             "{sample_name}_feature_counts", sample_name=self.sample_name
    #         ),
    #     )

    #     self.output(
    #         "out_predictions",
    #         source=self.allsorts.out_predictions,
    #         output_folder=[self.sample_name, "allsorts"],
    #         output_name=StringFormatter(
    #             "{sample_name}_predictions", sample_name=self.sample_name
    #         ),
    #     )

    #     self.output(
    #         "out_probabilities",
    #         source=self.allsorts.out_probabilities,
    #         output_folder=[self.sample_name, "allsorts"],
    #         output_name=StringFormatter(
    #             "{sample_name}_probabilities", sample_name=self.sample_name
    #         ),
    #     )

    #     self.output(
    #         "out_distributions",
    #         source=self.allsorts.out_distributions,
    #         output_folder=[self.sample_name, "allsorts"],
    #         output_name=StringFormatter(
    #             "{sample_name}_distributions", sample_name=self.sample_name
    #         ),
    #     )

    #     self.output(
    #         "out_waterfalls",
    #         source=self.allsorts.out_waterfalls,
    #         output_folder=[self.sample_name, "allsorts"],
    #         output_name=StringFormatter(
    #             "{sample_name}_waterfalls", sample_name=self.sample_name
    #         ),
    #     )

    def add_rna_seq_calling(self):
        self.step(
            "mark_duplicates",
            Gatk4MarkDuplicates_4_1_4(
                bam=[self.sortsam.out], validationStringency="SILENT", createIndex=True
            ),
            doc="Mark duplicates and create index",
        )

        self.step(
            "reorder_bam",
            Gatk4ReorderSam_4_1_4(
                reference=self.reference,
                inp=self.mark_duplicates.out,
                sequence_dictionary=self.sequence_dictionary,
                create_index=True,
            ),
        )

        # this tool may break in some samples
        # Fixed in the pull request in https://github.com/broadinstitute/gatk/pull/6909 update version tbc
        self.step(
            "splitncigar",
            Gatk4SplitNCigarReads_4_1_8_1(
                inp=[self.reorder_bam.out],
                reference=self.reference,
            ),
            doc="split'n'trim and reassign mapping qualities",
        )

        self.step(
            "rnaseq_call_variants",
            Gatk4HaplotypeCaller_4_1_4(
                inputRead=self.splitncigar.out,
                reference=self.reference,
                dontUseSoftClippedBases=True,
                standardMinConfidenceThresholdForCalling=self.call_conf,
            ),
        )

        self.step(
            "filter_variants",
            Gatk4VariantFiltration_4_1_4(
                reference=self.reference,
                variant=self.rnaseq_call_variants.out,
                clusterWindowSize=35,
                clusterSize=3,
                filterName=["FS", "QD"],
                filterExpression=["FS > 30.0", "QD < 2.0"],
            ),
        )

        self.output(
            "out_HAP_vcf",
            source=self.rnaseq_call_variants.out,
            output_folder=self.sample_name,
            output_name=StringFormatter(
                "{sample_name}_HAP", sample_name=self.sample_name
            ),
        )
        self.output(
            "out_HAP_filter_vcf",
            source=self.filter_variants.out,
            output_folder=self.sample_name,
            output_name=StringFormatter(
                "{sample_name}_HAP.filtered", sample_name=self.sample_name
            ),
        )

    def bind_metadata(self):
        return WorkflowMetadata(
            contributors=["Michael Franklin", "Jiaan Yu"],
            dateCreated=datetime(2020, 9, 24),
            dateUpdated=datetime(2021, 4, 22),
            documentation="",
        )


if __name__ == "__main__":
    OncopipeSamplePreparation().translate("wdl", allow_empty_container=True)
