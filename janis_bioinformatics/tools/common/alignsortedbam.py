from janis_bioinformatics.data_types import Bam, BamBai, Fastq, Sam, FastaWithDict
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bwa import BwaMemLatest, BwaMem_0_7_15
from janis_bioinformatics.tools.cutadapt.cutadapt_1_18 import CutAdapt_1_18
from janis_bioinformatics.tools.gatk4 import Gatk4SortSamLatest, Gatk4SortSam_4_0
from janis_bioinformatics.tools.samtools import SamToolsViewLatest, SamToolsView_1_7
from janis import Step, String, Input, Directory, Output
from janis.utils.metadata import WorkflowMetadata


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
        self.add_default_value(cutadapt.adapter, "AGATCGGAAGAGCGGTTCAGCAGGAATGCCGAG")
        self.add_default_value(cutadapt.adapter_g, "ACACTCTTTCCCTACACGACGCTCTTCCGATCT")
        self.add_default_value(cutadapt.removeMiddle5Adapter, "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT")
        self.add_default_value(cutadapt.removeMiddle3Adapter, "CTCGGCATTCCTGCTGAACCGCTCTTCCGATCT")
        self.add_default_value(cutadapt.qualityCutoff, 15)
        self.add_default_value(cutadapt.minReadLength, 50)

        # S2: BWA mem
        self.add_edges([
            (cutadapt.out, bwa.reads),
            (s1_inp_header, bwa.readGroupHeaderLine),
            (reference, bwa.reference)
        ])
        self.add_default_value(bwa.threads, 1)

        # fully connect step 2
        self.add_edge(bwa.out, samtools.sam)

        # fully connect step 3
        self.add_edges([
            (samtools.out, sortsam.bam),
        ])
        self.add_default_value(sortsam.sortOrder, "coordinate")
        self.add_default_value(sortsam.createIndex, True)
        self.add_default_value(sortsam.validationStringency, "SILENT")
        self.add_default_value(sortsam.maxRecordsInRam, 5000000)

        # connect to output
        self.add_edge(bwa.out, out_bwa)
        self.add_edge(samtools.out, out_samtools)
        # self.add_edge(sortsam.out, out_sortsam)
        self.add_edge(sortsam.out, out)


if __name__ == "__main__":
    w = AlignSortedBam()
    w.dump_translation("wdl")
    # print(AlignSortedBam().help())

    # import shepherd
    #
    # task = shepherd.from_workflow(w, engine=shepherd.Cromwell(), env="pmac")
    # print(task.outputs)
