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
from janis_bioinformatics.tools.gatk4 import (
    Gatk4SortSamLatest,
    Gatk4MarkDuplicates_4_1_4,
    Gatk4ReorderSam_4_1_4,
    Gatk4SplitNCigarReads_4_1_4,
    Gatk4HaplotypeCaller_4_1_4,
    Gatk4VariantFiltration_4_1_4,
)
from janis_bioinformatics.tools.oshlack.jaffa.base import Jaffa_2_0
from janis_bioinformatics.tools.oshlack.prepareallsortsinput import (
    PrepareALLSortsInput_0_1_0,
)
from janis_bioinformatics.tools.oshlack.allsorts.versions import AllSorts_0_1_0
from janis_bioinformatics.tools.star import (
    StarAlignReads_2_7_3,
    StarGenerateIndexes_2_7_3,
)
from janis_bioinformatics.tools.subread import FeatureCounts_2_0_1
from janis_bioinformatics.tools.suhrig import Arriba_1_2_0
from janis_bioinformatics.tools.usadellab import TrimmomaticPairedEnd_0_35


class OncopipeWorkflow(BioinformaticsWorkflow):
    def tool_provider(self):
        return "Oncopipe"

    def friendly_name(self):
        return "Oncopipe"

    def id(self) -> str:
        return "oncopipe"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        return WorkflowMetadata(
            institution="Oshlack and Peter MacCallum Cancer Centre",
            dateCreated=datetime(2020, 1, 1),
            contributors=[
                # Original
                "Rebecca Louise Evans",
                "Breon Schmidt",
                "Andrew Lonsdale",
                "Simon Sadedin",
                "Nadia Davidson",
                "Quarkins",
                "Jovana Maksimovic",
                "Alicia Oshlack",
                # Janis rewrite
                "Richard Lupat",
                "Jiaan Yu",
                "Michael Franklin",
            ],
            documentation="""
Clinical pipeline for detecting gene fusions in RNAseq data utilising JAFFA. The pipeline optionally calls a classifier 
for B-Cell Acute Lymphocytic Leukaemia (based on AllSorts). As well as variant calling pipeline using Picard,GATK and VEP.
            
A poster was also presented at ABACBS2018 noting the current status and future plans:

`Oncopipe ABACBS 2018 <https://atlassian.petermac.org.au/bitbucket/projects/OS/repos/oncopipe/browse/Oncopipe_ABACBS_v6.pdf>`_            
            
Original code example:

.. code-block: text

   bpipe run -r \
       -p name=SAMPLE_ID \
       -p out=OUTPUT_PATH \
       -p fastq=FASTQ_GZ_FILES \
       PATH_TO_THIS_DIR/pipeline/onco.pipe
            """,
        )

    def constructor(self):

        self.input("name", Array(String))
        self.input("reads", Array(FastqGzPairedEnd))
        self.input("genome_dir", Directory)
        self.input("jaffa_reference", Directory)
        self.input("reference", FastaWithIndexes)
        self.input("gtf", File)
        self.input("blacklist", File(optional=True))
        self.input("contigs", Array(String(), optional=True))
        self.input("filters", Array(String(), optional=True))
        self.input("platform", String, default="ILLUMINA")
        self.input("sequence_dictionary", File)
        self.input("call_conf", Double, default=20.0)

        self.step(
            "process",
            OncopipeSamplePreparation(
                name=self.name,
                reads=self.reads,
                genome_dir=self.genome_dir,
                reference=self.reference,
                gtf=self.gtf,
                blacklist=self.blacklist,
                contigs=self.contigs,
                filters=self.filters,
                platform=self.platform,
                sequence_dictionary=self.sequence_dictionary,
                call_conf=self.call_conf,
            ),
            scatter=ScatterDescription(
                ["reads", "name"], method=ScatterMethod.dot, labels=self.name,
            ),
        )

        self.capture_outputs_from_step(self.process, output_prefix="")

        self.add_jaffa()

    def add_jaffa(self):
        self.step(
            "jaffa", Jaffa_2_0(reference=self.jaffa_reference, fastqs=self.reads,),
        )

        self.output(
            "out_reference",
            source=self.jaffa.out_reference,
            output_folder="jaffa",
            output_name="jaffa_results.fasta",
        )

        self.output(
            "out_csv",
            source=self.jaffa.out_csv,
            output_folder="jaffa",
            output_name="jaffa_results.csv",
        )
        # Then
        #   // Complete Jaffa
        #   compile_results_jaffa +
        #
        #   // Run Classifier Stage (Counts / Classifier)
        #   run_classifier +
        #
        #   // Consolidate all reports
        #   run_report


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

        self.input("name", String, doc="Sample ID")
        self.input("reads", FastqGzPairedEnd)
        self.input("genome_dir", Directory)
        self.input("reference", FastaWithIndexes)
        self.input("gtf", File)
        self.input("blacklist", File(optional=True))
        self.input("contigs", Array(String(), optional=True))
        self.input("filters", Array(String(), optional=True))
        self.input("platform", String, default="ILLUMINA")
        self.input("sequence_dictionary", File)
        self.input("call_conf", Double, default=20.0)
        self.input("star_sjdbOverhang", Int, default=99)

        self.add_trim_and_align()
        self.add_sort_bam()
        self.add_arriba()
        # self.add_all_sorts()
        # self.add_rna_seq_calling()

    def add_trim_and_align(self):

        self.step(
            "trim",
            TrimmomaticPairedEnd_0_35(
                sampleName=self.name,
                inp=self.reads,
                phred33=True,
                steps=[
                    "ILLUMINACLIP:/usr/local/share/trimmomatic-0.35-6/adapters/TruSeq2-PE.fa:2:30:10",
                    "LEADING:15",
                    "TRAILING:15",
                    "SLIDINGWINDOW:4:15",
                    "MINLEN:35",
                ],
            ),
            doc="Trim reads using Trimmomatic",
        )

        # Merge star alignment stages
        self.step(
            "star_map_1pass_PE",
            StarAlignReads_2_7_3(
                readFilesIn=self.trim.pairedOut,
                genomeDir=self.genome_dir,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                readFilesCommand="zcat",
                outSAMtype=["None"],
            ),
            doc="Map reads using the STAR aligner: 1st pass",
        )

        self.step(
            "star_gen2pass",
            StarGenerateIndexes_2_7_3(
                genomeFastaFiles=self.reference,
                sjdbFileChrStartEnd=self.star_map_1pass_PE.SJ_out_tab,
                sjdbOverhang=self.star_sjdbOverhang,
                sjdbGTFfile=self.gtf,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                outputGenomeDir=self.name,
            ),
            doc="Map reads using the STAR aligner: generate genome",
        )

        self.step(
            "star_map_2pass_PE",
            StarAlignReads_2_7_3(
                readFilesIn=self.trim.pairedOut,
                readFilesCommand="zcat",
                genomeDir=self.star_gen2pass.out,
                outSAMattrRGline=[
                    StringFormatter("ID:{sample}", sample=self.name),
                    StringFormatter("SM:{lane}", lane=self.name),
                    StringFormatter("LB:{library}", library=self.name),
                    StringFormatter("PL:{platform}", platform=self.platform),
                    StringFormatter("PU:1"),
                ],
                sjdbGTFfile=self.gtf,
                quantMode="GeneCounts",
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                outSAMtype=["BAM", "Unsorted"],
                outSAMunmapped="Within",
                outFilterMultimapNmax=1,
                outFilterMismatchNmax=3,
                chimSegmentMin=10,
                chimOutType=["WithinBAM", "SoftClip"],
                chimJunctionOverhangMin=10,
                chimScoreMin=1,
                chimScoreDropMax=30,
                chimScoreJunctionNonGTAG=0,
                chimScoreSeparation=1,
                alignSJstitchMismatchNmax=[5, -1, 5, 5],
                chimSegmentReadGapMax=3,
            ),
        )
        self.output(
            "out_star_gene_counts",
            source=self.star_map_2pass_PE.out_gene_counts.assert_not_null(),
            output_folder=self.name,
            output_name=StringFormatter(
                "{sample_name}_ReadsPerGene.out.tab", sample_name=self.name
            ),
        )

    def add_sort_bam(self):
        self.step(
            "sortsam",
            Gatk4SortSamLatest(
                bam=self.star_map_2pass_PE.out_unsorted_bam.assert_not_null(),
                sortOrder="coordinate",
                createIndex=True,
            ),
        )

        self.output(
            "out_sorted_bam",
            source=self.sortsam.out,
            output_folder=self.name,
            output_name=self.name,
        )

    def add_arriba(self):
        self.step(
            "arriba",
            Arriba_1_2_0(
                aligned_inp=self.star_map_2pass_PE.out_unsorted_bam.assert_not_null(),
                blacklist=self.blacklist,
                fusion_transcript=True,
                peptide_sequence=True,
                reference=self.reference,
                gtf_file=self.gtf,
                contigs=self.contigs,
                filters=self.filters,
            ),
        )

        self.output(
            "out_arriba_fusion",
            source=self.arriba.out,
            output_folder=self.name,
            output_name=StringFormatter("{sample_name}_fusion", sample_name=self.name),
        )
        self.output(
            "out_arriba_fusion_discarded",
            source=self.arriba.out_discarded,
            output_folder=self.name,
            output_name=StringFormatter(
                "{sample_name}_fusion_discarded", sample_name=self.name
            ),
        )

    def add_all_sorts(self):
        self.step(
            "featureCounts",
            FeatureCounts_2_0_1(
                bam=[self.star_map_2pass_PE.out_unsorted_bam.assert_not_null()],
                annotationFile=self.gtf,
                attributeType="gene_name",
            ),
        )

        # A script that transforms featurecounts output to allsorts input
        self.step(
            "prepareAllsortsInput",
            PrepareALLSortsInput_0_1_0(
                inps=[self.featureCounts.out],
                labels=[self.name],
                fusion_caller="featureCounts",
            ),
        )

        self.step(
            "allsorts", AllSorts_0_1_0(samples=self.prepareAllsortsInput.out),
        )

        self.output(
            "out_gene_counts",
            source=self.featureCounts.out,
            output_folder=self.name,
            output_name=StringFormatter(
                "{sample_name}_feature_counts", sample_name=self.name
            ),
        )

        self.output(
            "out_predictions",
            source=self.allsorts.out_predictions,
            output_folder=[self.name, "allsorts"],
            output_name=StringFormatter(
                "{sample_name}_predictions", sample_name=self.name
            ),
        )

        self.output(
            "out_probabilities",
            source=self.allsorts.out_probabilities,
            output_folder=[self.name, "allsorts"],
            output_name=StringFormatter(
                "{sample_name}_probabilities", sample_name=self.name
            ),
        )

        self.output(
            "out_distributions",
            source=self.allsorts.out_distributions,
            output_folder=[self.name, "allsorts"],
            output_name=StringFormatter(
                "{sample_name}_distributions", sample_name=self.name
            ),
        )

        self.output(
            "out_waterfalls",
            source=self.allsorts.out_waterfalls,
            output_folder=[self.name, "allsorts"],
            output_name=StringFormatter(
                "{sample_name}_waterfalls", sample_name=self.name
            ),
        )

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
            Gatk4SplitNCigarReads_4_1_4(
                inp=[self.reorder_bam.out], reference=self.reference,
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
            output_folder=self.name,
            output_name=StringFormatter("{sample_name}_HAP", sample_name=self.name),
        )
        self.output(
            "out_HAP_filter_vcf",
            source=self.filter_variants.out,
            output_folder=self.name,
            output_name=StringFormatter(
                "{sample_name}_HAP.filtered", sample_name=self.name
            ),
        )

    def bind_metadata(self):
        return WorkflowMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 9, 24),
            dateUpdated=datetime(2020, 10, 7),
            documentation="",
        )


__JANIS_ENTRYPOINT = OncopipeWorkflow

if __name__ == "__main__":
    print(OncopipeWorkflow().help())
