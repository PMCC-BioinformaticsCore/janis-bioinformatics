from janis import Step, String, Input, Output, Int, Boolean
from janis.utils.metadata import WorkflowMetadata

from janis_bioinformatics.data_types import Bam, BamBai, Fastq, Sam, FastaWithDict
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bwa import BwaMem_0_7_15
from janis_bioinformatics.tools.cutadapt.cutadapt_1_18 import CutAdapt_1_18
from janis_bioinformatics.tools.gatk4 import Gatk4SortSam_4_0
from janis_bioinformatics.tools.samtools import SamToolsView_1_7


class AlignSortedBam(BioinformaticsWorkflow):

    def __init__(self):
        super(AlignSortedBam, self).__init__("alignsortedbam", friendly_name="Align sorted BAM")

        if not self._metadata:
            self._metadata = WorkflowMetadata()

        self._metadata.documentation = "Align sorted bam with this subworkflow consisting of BWA Mem + SamTools + Gatk4SortSam"
        self._metadata.creator = "Michael Franklin"
        self._metadata.dateCreated = "2018-12-24"
        self._metadata.version = "1.0.0"

        cutadapt = Step("cutadapt", CutAdapt_1_18())
        bwa = Step("bwa", BwaMem_0_7_15())
        samtools = Step("samtools", SamToolsView_1_7())
        sortsam = Step("sortsam", Gatk4SortSam_4_0())

        s1_inp_header = Input("read_group_header_line", String())
        reference = Input("reference", FastaWithDict())
        fastqs = Input("fastq", Fastq())

        out_bwa = Output("out_bwa", Sam())
        out_samtools = Output("out_samtools", Bam())
        out = Output("out", BamBai())

        # Fully connect step 1
        self.add_edges([
            (fastqs, cutadapt.fastq)
        ])
        # Step 1 with defaults
        self.add_edges([
            (Input("adapter", String(), default="AGATCGGAAGAGCGGTTCAGCAGGAATGCCGAG"), cutadapt.adapter),
            (Input("adapter_g", String(), default="ACACTCTTTCCCTACACGACGCTCTTCCGATCT"), cutadapt.adapter_g),
            (Input("removeMiddle5Adapter", String(), default="AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"),
             cutadapt.removeMiddle5Adapter),
            (Input("removeMiddle3Adapter", String(), default="CTCGGCATTCCTGCTGAACCGCTCTTCCGATCT"),
             cutadapt.removeMiddle3Adapter),
            (Input("qualityCutoff", Int(), default=15), cutadapt.qualityCutoff),
            (Input("minReadLength", Int(), default=50), cutadapt.minReadLength),
        ])

        # S2: BWA mem
        self.add_edges([
            (cutadapt.out, bwa.reads),
            (s1_inp_header, bwa.readGroupHeaderLine),
            (reference, bwa.reference)
        ])

        # fully connect step 2
        self.add_edge(bwa.out, samtools.sam)

        # fully connect step 3
        self.add_edge(samtools.out, sortsam.bam)
        self.add_edges([
            (Input("sortOrder", String(), default="coordinate"), sortsam.sortOrder),
            (Input("createIndex", Boolean(), default=True), sortsam.createIndex),
            (Input("validationStringency", String(), default="SILENT"), sortsam.validationStringency),
            (Input("maxRecordsInRam", Int(), default=5000000), sortsam.maxRecordsInRam),
        ])

        # connect to output
        self.add_edge(bwa.out, out_bwa)
        self.add_edge(samtools.out, out_samtools)
        # self.add_edge(sortsam.out, out_sortsam)
        self.add_edge(sortsam.out, out)


if __name__ == "__main__":
    w = AlignSortedBam()

    w.dump_translation("cwl", with_resource_overrides=True)

    # print(build_resources_input(w, "wdl", {CaptureType.KEY: CaptureType.CHROMOSOME}))

    # print(AlignSortedBam().help())

    # import shepherd
    #
    # task = shepherd.from_workflow(w, engine=shepherd.Cromwell(), env="pmac")
    # print(task.outputs)
