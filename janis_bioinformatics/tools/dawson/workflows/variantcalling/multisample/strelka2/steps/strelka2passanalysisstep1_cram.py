from .strelka2passanalysisstep1 import Strelka2PassWorkflowStep1


class Strelka2PassWorkflowStep1Cram(Strelka2PassWorkflowStep1):
    def id(self):
        return "Strelka2PassWorkflowStep1Cram"

    def friendly_name(self):
        return "Strelka 2Pass analysis step1 (CRAM)"

    # this is a way to get the tool without spaghetti code in bam and cram format
    def getMantaTool(self):
        from janis_bioinformatics.tools.illumina.manta.manta import (
            MantaCram_1_5_0 as Manta,
        )

        return Manta

    def getStrelka2Tool(self):
        from janis_bioinformatics.tools.illumina.strelkasomatic.strelkasomatic import (
            StrelkaSomaticCram_2_9_10 as Strelka,
        )

        return Strelka

    def getStrelka2InputType(self):
        from janis_bioinformatics.data_types import CramCrai

        return CramCrai


if __name__ == "__main__":

    wf = Strelka2PassWorkflowStep1Cram()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
