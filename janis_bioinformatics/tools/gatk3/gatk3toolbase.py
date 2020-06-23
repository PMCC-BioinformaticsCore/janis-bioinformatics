from abc import ABC, abstractmethod

from janis_core import ToolArgument, StringFormatter, MemorySelector

from .. import BioinformaticsTool


class GATK3ToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "broad institute"

    @classmethod
    def base_command(cls):
        # Just java, rest is in arguments
        return [
            "java",
        ]

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
        return [
            ToolArgument(
                "-jar /usr/GenomeAnalysisTK.jar", position=-3, shell_quote=False
            ),
            ToolArgument(
                StringFormatter("-Xmx{memory}G", memory=MemorySelector() * 3 / 4,),
                position=-2,
                shell_quote=False,
            ),
            ToolArgument(f"-T {self.gatk_command()}", position=-1, shell_quote=False),
        ]
