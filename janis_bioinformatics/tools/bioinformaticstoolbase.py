from abc import ABC

from janis_core import (
    CommandTool,
    Workflow,
    PythonTool,
    CommandToolBuilder,
    WorkflowBuilder,
)

BIOINFORMATICS_MODULE = "bioinformatics"


class BioinformaticsTool(CommandTool, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE

    def evaluate(self):
        evaluation = {}

        evaluation['friendly_name'] = self.evaluate_friendly_name()

        return evaluation

    def evaluate_friendly_name(self):
        if self.friendly_name() is None:
            return False

        return True


class BioinformaticsWorkflow(Workflow, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsPythonTool(PythonTool, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsToolBuilder(CommandToolBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module=BIOINFORMATICS_MODULE)


class BioinformaticsWorkflowBuilder(WorkflowBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module=BIOINFORMATICS_MODULE)
