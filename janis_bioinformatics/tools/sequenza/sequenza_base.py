from abc import ABC, abstractmethod

from janis_bioinformatics.tools import BioinformaticsTool


class SequenzaBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "Sequenza"

    @classmethod
    @abstractmethod
    def sequenza_command(cls):
        raise Exception(
            "Subclass must implement the sequenza method: expects one of: ["
            "   bam2seqz, seqz_binning"
            "]"
        )

    def base_command(self):
        return ["sequenza-utils", self.sequenza_command()]

    def doc(self):
        return """
  Sequenza Utils is an ensemble of tools capable of perform various tasks, primarily aimed to convert bam/pileup files 
  to a format usable by the sequenza R package""".strip()

    def inputs(self):
        return []

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the sequenza classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference sequenza subclasses, "
            "and the subclass must contain a definition for docker."
        )
