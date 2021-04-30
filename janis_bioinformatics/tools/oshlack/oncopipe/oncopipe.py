from datetime import datetime

from janis_core import (
    WorkflowMetadata,
    WorkflowBuilder,
    ScatterDescription,
    ScatterMethod,
    Array,
    String,
    Directory,
)

from janis_bioinformatics.data_types import FastqGzPairedEnd
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow
from janis_bioinformatics.tools.oshlack.oncopipe.oncopipeSample import (
    OncopipeSamplePreparation,
)
from janis_bioinformatics.tools.oshlack.jaffa.base import Jaffa_2_0


class OncopipeWorkflow(OncopipeSamplePreparation):
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
            dateUpdated=datetime(2021, 4, 30),
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
        self.add_inputs()
        self.add_process_sample()
        self.add_jaffa()

    def add_inputs(self):
        self.input("sample_name", Array(String))
        self.input("reads", Array(FastqGzPairedEnd))
        self.inputs_for_reference()
        self.inputs_for_intervals()
        self.inputs_for_configuration()

    def inputs_for_reference(self):
        super().inputs_for_reference()
        # Jaffa 2 only supports hg38
        self.input("jaffa_reference", Directory)

    def add_process_sample(self):
        self.step(
            "process",
            OncopipeSamplePreparation(
                sample_name=self.sample_name,
                reads=self.reads,
                genome_dir=self.genome_dir,
                reference=self.reference,
                gtf=self.gtf,
                blacklist=self.blacklist,
                known_fusions=self.known_fusions,
                protein_domains_gff=self.protein_domains_gff,
                cytobands=self.cytobands,
                sequence_dictionary=self.sequence_dictionary,
                intervals=self.intervals,
                trimming_options=self.trimming_options,
                platform=self.platform,
                contigs=self.contigs,
                filters=self.filters,
                call_conf=self.call_conf,
                star_threads=self.star_threads,
            ),
            scatter=ScatterDescription(
                ["reads", "sample_name"],
                method=ScatterMethod.dot,
                labels=self.sample_name,
            ),
        )
        self.capture_outputs_from_step(self.process)

    def add_jaffa(self):
        self.step(
            "jaffa",
            Jaffa_2_0(
                reference=self.jaffa_reference,
                fastqs=self.reads,
            ),
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


if __name__ == "__main__":
    OncopipeWorkflow().translate("wdl", allow_empty_container=True)
