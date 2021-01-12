from .strelka2passanalysisstep2 import Strelka2PassWorkflowStep2


class Strelka2PassWorkflowStep2Cram(Strelka2PassWorkflowStep2):
    def id(self):
        return "Strelka2PassWorkflowStep2Cram"

    def friendly_name(self):
        return "Strelka 2Pass analysis step 2 (CRAM)"

    def getStrelka2Tool(self):
        from janis_bioinformatics.tools.illumina.strelkasomatic.strelkasomatic import (
            StrelkaSomaticCram_2_9_10 as Strelka,
        )

        return Strelka

    def getStrelka2InputType(self):
        from janis_bioinformatics.data_types import CramCrai

        return CramCrai


if __name__ == "__main__":

    wf = Strelka2PassWorkflowStep2Cram()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
