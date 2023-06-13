from .strelka2passworkflow import Strelka2PassWorkflow


class Strelka2PassWorkflowCram(Strelka2PassWorkflow):
    def id(self):
        return "Strelka2PassWorkflowCram"

    def friendly_name(self):
        return "Strelka 2Pass analysis (CRAM)"

    # this is a way to get the tool without spaghetti code in bam and cram format
    def getStep1Tool(self):
        from .steps.strelka2passanalysisstep1_cram import (
            Strelka2PassWorkflowStep1Cram as Strelka2PassWorkflowStep1,
        )

        return Strelka2PassWorkflowStep1

    def getStep2Tool(self):
        from .steps.strelka2passanalysisstep2_cram import (
            Strelka2PassWorkflowStep2Cram as Strelka2PassWorkflowStep2,
        )

        return Strelka2PassWorkflowStep2

    def getStrelka2InputType(self):
        from janis_bioinformatics.data_types import CramCrai

        return CramCrai


if __name__ == "__main__":

    wf = Strelka2PassWorkflowCram()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
