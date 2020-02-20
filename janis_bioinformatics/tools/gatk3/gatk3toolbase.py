from abc import ABC, abstractmethod

from .. import BioinformaticsTool

class GATK3ToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "broad institute"
    
    @classmethod
    def base_command(cls):
        # Check to emplement the gatk3 java options
        return ["java", "-Xmx8g", "-jar", "GenomeAnalysisTK.jar", "-T",
        cls.gatk_command()]

    @classmethod
    @abstractmethod
    def gatk_command(cls):
        raise Exception("Subclass must override 'gatk_command' method")

    def inputs(self):
        return []

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the Gatk classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference Gatkbase subclasses, "
            "and the subclass must contain a definition for docker."
        )

    def arguments(self):
        return []
