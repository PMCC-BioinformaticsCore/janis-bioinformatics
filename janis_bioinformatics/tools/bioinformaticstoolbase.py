import os
import sys
from abc import ABC

from janis_core import (
    CommandTool,
    Workflow,
    PythonTool,
    CommandToolBuilder,
    WorkflowBuilder,
)

from janis_core.tool.tool import ToolWithTestSuite

BIOINFORMATICS_MODULE = "bioinformatics"


class BioinformaticsTool(CommandTool, ToolWithTestSuite, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsWorkflow(Workflow, ToolWithTestSuite, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsPythonTool(PythonTool, ToolWithTestSuite, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsToolBuilder(CommandToolBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module=BIOINFORMATICS_MODULE)


class BioinformaticsWorkflowBuilder(WorkflowBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module=BIOINFORMATICS_MODULE)


