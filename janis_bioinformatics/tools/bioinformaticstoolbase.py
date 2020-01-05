from abc import ABC

from janis_core import CommandTool, Workflow

BIOINFORMATICS_MODULE = "bioinformatics"


class BioinformaticsTool(CommandTool, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsWorkflow(Workflow, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE
