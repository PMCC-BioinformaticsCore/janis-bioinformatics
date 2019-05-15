from janis import Step, String, Input, Output, Int, Boolean
from janis.utils.metadata import WorkflowMetadata

from janis_bioinformatics.data_types import Fastq, FastaWithDict
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common.bwamem_samtoolsview import BwaMem_SamToolsView
from janis_bioinformatics.tools.cutadapt.cutadapt_1_18 import CutAdapt_1_18
from janis_bioinformatics.tools.gatk4 import Gatk4SortSam_4_0


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
        bwasam = Step("bwa_sam", BwaMem_SamToolsView())
        sortsam = Step("sortsam", Gatk4SortSam_4_0())

        read_group_header = Input("readGroupHeaderLine", String())
        reference = Input("reference", FastaWithDict())
        fastqs = Input("fastq", Fastq())

        out_bam = Output("out_bwa")
        out = Output("out")

        # S1: Cutadapt
        self.add_edge(fastqs, cutadapt.fastq)
        # Step 1 with defaults
        self.add_edges([
            (Input("adapter", String(optional=True)), cutadapt.adapter),
            (Input("adapter_g", String(optional=True)), cutadapt.adapter_g),
            (Input("removeMiddle5Adapter", String(optional=True)),
             cutadapt.removeMiddle5Adapter),
            (Input("removeMiddle3Adapter", String(optional=True)),
             cutadapt.removeMiddle3Adapter),
            (Input("qualityCutoff", Int(), default=15), cutadapt.qualityCutoff),
            (Input("minReadLength", Int(), default=50), cutadapt.minReadLength),
        ])

        # S2: BWA mem + Samtools View
        self.add_edges([
            (cutadapt.out, bwasam.reads),
            (read_group_header, bwasam.readGroupHeaderLine),
            (reference, bwasam.reference)
        ])

        # S3: SortSam
        self.add_edge(bwasam.out, sortsam.bam)
        self.add_edges([
            (Input("sortOrder", String(), default="coordinate"), sortsam.sortOrder),
            (Input("createIndex", Boolean(), default=True), sortsam.createIndex),
            (Input("validationStringency", String(), default="SILENT"), sortsam.validationStringency),
            (Input("maxRecordsInRam", Int(), default=5000000), sortsam.maxRecordsInRam),
        ])

        # connect to output
        self.add_edge(bwasam.out, out_bam)
        self.add_edge(sortsam.out, out)


if __name__ == "__main__":
    w = AlignSortedBam()

    w.translate("wdl", with_resource_overrides=True)

    # print(build_resources_input(w, "wdl", {CaptureType.KEY: CaptureType.CHROMOSOME}))

    # print(AlignSortedBam().help())

    # import shepherd
    #
    # task = shepherd.from_workflow(w, engine=shepherd.Cromwell(), env="pmac")
    # print(task.outputs)
