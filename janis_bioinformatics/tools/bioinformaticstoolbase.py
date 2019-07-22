from abc import ABC

from janis_core import CommandTool, Workflow

BIOINFORMATICS_MODULE = "bioinformatics"


class BioinformaticsTool(CommandTool, ABC):
    @staticmethod
    def tool_module():
        return BIOINFORMATICS_MODULE


class BioinformaticsWorkflow(Workflow, ABC):
    @staticmethod
    def tool_module():
        return BIOINFORMATICS_MODULE
