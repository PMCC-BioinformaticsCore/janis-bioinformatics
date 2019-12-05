from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix, VcfTabix

from janis_core import Array, Boolean, String, File



class BioGeographicPhylogenies(BioinformaticsWorkflow):
    def id(self):
        return "BioGeographicPhylogenies"

    def friendly_name(self):
        return "Biogeographic Phylogenic Analysis"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 12, 02)
        self.metadata.dateUpdated = date(2019, 12, 02)

        self.metadata.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = [
            "variants",
            "spatial",
            "evolution",
            "phylogeny",
        ]
        self.metadata.documentation = """
        This workflow analysis the possible migration and population structure pattern of samples of the same organims to gain insight into the disease trajectory.

        It combines clonal deconvolution as well as bayesian phylogentic reconstruction of coalescent trees and migration.
                """.strip()

    def constructor(self):

        self.input("snvs", Array(VcfTabix))
        self.input("seqz", Array(File))



        #select variants


if __name__ == "__main__":

    wf = Strelka2PassWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
