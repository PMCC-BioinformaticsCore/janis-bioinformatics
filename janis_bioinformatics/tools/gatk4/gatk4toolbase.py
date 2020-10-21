from abc import ABC, abstractmethod

from janis_core.operators.logical import If, IsDefined
from janis_core.operators.standard import JoinOperator, FirstOperator

from janis_bioinformatics.data_types import Bed

from .. import BioinformaticsTool
from janis_core import (
    ToolInput,
    Boolean,
    ToolArgument,
    StringFormatter,
    MemorySelector,
    String,
    Array,
    InputSelector,
    Int,
)


class Gatk4ToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
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
            ToolInput("javaOptions", Array(String, optional=True)),
            ToolInput(
                "compression_level",
                Int(optional=True),
                doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2.",
            )
            # ToolInput("pg-tag", Boolean(optional=True), prefix="--add-output-sam-program-record",
            #           doc="If true, adds a PG tag to created SAM/BAM/CRAM files.")
        ]

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
                StringFormatter(
                    "-Xmx{memory}G {compression} {otherargs}",
                    memory=MemorySelector() * 3 / 4,
                    compression=If(
                        IsDefined(InputSelector("compression_level")),
                        "-Dsamjdk.compress_level=" + InputSelector("compression_level"),
                        "",
                    ),
                    otherargs=JoinOperator(
                        FirstOperator([InputSelector("javaOptions"), []]), " "
                    ),
                ),
                prefix="--java-options",
                position=-1,
            )
        ]
