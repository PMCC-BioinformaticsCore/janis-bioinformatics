from .mutect2jointsomaticworkflow import Mutect2JointSomaticWorkflow


class Mutect2JointSomaticWorkflowCram(Mutect2JointSomaticWorkflow):
    def id(self):
        return "Mutect2JointSomaticWorkflowCram"

    def friendly_name(self):
        return "Mutect2 joint somatic variant calling workflow (CRAM)"

    # this is a way to get the tool without spaghetti code in bam and cram format
    def getMutect2Tool(self):
        from janis_bioinformatics.tools.gatk4.mutect2.versions import (
            GatkMutect2Cram_4_1_8 as Mutect2,
        )

        return Mutect2

    def getPileUpTool(self):
        from janis_bioinformatics.tools.gatk4.getpileupsummaries.versions import (
            Gatk4GetPileUpSummariesCram_4_1_8 as Pileup,
        )

        return Pileup

    def getMutect2InputType(self):
        from janis_bioinformatics.data_types import CramCrai

        return CramCrai


if __name__ == "__main__":

    wf = Mutect2JointSomaticWorkflowCram()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
