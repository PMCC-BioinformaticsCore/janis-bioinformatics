from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import FastaWithDict

from janis_core import Array, Boolean, String


class BwaAlignWithPostProcessing(BioinformaticsWorkflow):
    def id(self):
        return "BwaAlignWithPostProcessing"

    def friendly_name(self):
        return "BWA MEM: alt aware alignment with postprocessing"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        # self.metadata.dateCreated = date(2019, 11, 05)
        # self.metadata.dateUpdated = date(2019, 11, 05)

        self.metadata.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = ["alignment", "bwa", "GRCh38"]
        self.metadata.documentation = """
        This workflow will use the alt aware approach of BWA MEM and apply the posprocessing step afterwards
                """.strip()

    def constructor(self):

        self.input("R1FastqFiles", FastqGzPair)
        self.input("reference", FastaWithDict)


if __name__ == "__main__":

    wf = BwaAlignWithPostProcessing()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
