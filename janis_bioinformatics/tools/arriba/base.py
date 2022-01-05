from abc import ABC, abstractmethod

from janis_bioinformatics.tools import BioinformaticsTool


class ArribaBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "Arriba"

    @classmethod
    def base_command(cls):
        return ["", cls.arriba_command()]

    @classmethod
    @abstractmethod
    def arriba_command(cls):
        raise Exception("Unknown error occured")

    def inputs(self):
        return []

    def doc(self):
        return """\
Arriba is a command-line tool for the detection of gene fusions from RNA-Seq \
data. It was developed for the use in a clinical research setting.""".strip()

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the facets classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference facets subclasses, "
            "and the subclass must contain a definition for docker."
        )
