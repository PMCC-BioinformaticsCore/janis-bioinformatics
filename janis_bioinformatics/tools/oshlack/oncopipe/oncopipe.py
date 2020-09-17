from datetime import datetime

from janis_unix import Echo

from janis_bioinformatics.data_types import FastqGzPairedEnd, FastaWithIndexes
from janis_core import WorkflowMetadata, String, Array, WorkflowBuilder

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow
from janis_bioinformatics.tools.oshlack.oncopipe.star import OncopipeStarAligner
from janis_bioinformatics.tools.oshlack.oncopipe.variants import OncopipeVariantCaller


class OncopipeWorkflow(BioinformaticsWorkflow):
    def friendly_name(self):
        return "Oncopipe"

    def id(self) -> str:
        return "oncopipe"

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

        self.input("name", String, doc="Sample ID")
        self.input("fastqs", Array(FastqGzPairedEnd), doc="Reads")

        self.input("reference", FastaWithIndexes, doc="Fasta reference")

        self.step(
            "process",
            self.generate_scattered_bit(
                name=self.name, fastq=self.fastqs, reference=self.reference,  # scatter
            ),
            scatter="reference",
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

    @staticmethod
    def generate_scattered_bit(**kwargs):
        wf = WorkflowBuilder("OncopipeProcessForEachSample")

        wf.input("name", String, doc="Sample ID")
        wf.input("fastq", FastqGzPairedEnd)
        wf.input("reference", FastaWithIndexes, doc="Fasta reference")

        wf.step(
            "get_sample_info",
            Echo(),
            doc="Validate and set information about the sample to be processed",
        )

        # The first phase is to perform transcriptome alignment and fusion
        #   detection (modified from JAFFA), for each sample

        # wf.step("run_jaffa", Jaffa(**kkwargs))

        # the second phase is to perform genome alignment (using STAR)

        wf.step(
            "run_start",
            OncopipeStarAligner(
                sampleName=wf.name,
                reads=wf.fastq,
                reference=wf.reference,
                # gtf, sample, lane, library, platform
            ),
        )

        wf.step(
            "run_variants",
            OncopipeVariantCaller(
                bam=wf.run_start.out_bam,
                reference=wf.reference,
                sample_name=wf.sample_name,
                platform="",
            ),
        )

        # The third parallel phase checks the quality of the fastq files

        # wf.step("run_fastqc", OncopipeFastqc(**kkwargs))

        return wf(**kwargs)
