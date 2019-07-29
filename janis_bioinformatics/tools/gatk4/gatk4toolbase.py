from abc import ABC, abstractmethod

from janis_bioinformatics.data_types import Bed

from .. import BioinformaticsTool
from janis_core import ToolInput, Boolean


class Gatk4ToolBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "GATK4"

    @classmethod
    def base_command(cls):
        return ["gatk", cls.gatk_command()]

    @classmethod
    @abstractmethod
    def gatk_command(cls):
        raise Exception("Subclass must override 'gatk_command' method")

    def inputs(self):
        return [
            # ToolInput("pg-tag", Boolean(optional=True), prefix="--add-output-sam-program-record",
            #           doc="If true, adds a PG tag to created SAM/BAM/CRAM files.")
        ]

    @staticmethod
    @abstractmethod
    def container():
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the Gatk classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference Gatkbase subclasses, "
            "and the subclass must contain a definition for docker."
        )

    def arguments(self):
        return []
