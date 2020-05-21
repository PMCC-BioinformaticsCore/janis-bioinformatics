from abc import ABC, abstractmethod

from janis_bioinformatics.tools import BioinformaticsTool


class FacetsBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "Facets"

    def base_command(self):
        return ["LD_LIBRARY_PATH=/opt/conda/lib /snp-pileup"]

    def inputs(self):
        return []

    def doc(self):
        return """\
Algorithm to implement Fraction and Allele specific 
Copy number Estimate from Tumor/normal Sequencing.""".strip()

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the facets classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference facets subclasses, "
            "and the subclass must contain a definition for docker."
        )
