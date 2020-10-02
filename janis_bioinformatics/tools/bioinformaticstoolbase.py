from typing import Dict, Union
from abc import ABC
import docker

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

    def evaluate(self) -> Dict[str, str]:
        evaluation = {}

        evaluation['friendly_name'] = self.evaluate_friendly_name()
        evaluation['container'] = self.evaluate_container()

        return evaluation

    def evaluate_friendly_name(self) -> Union[str, bool]:
        if self.friendly_name() is None:
            return "Missing friendly name"

        return True

    def evaluate_container(self) -> Union[str, bool]:
        """
        Evaluate if the image specified for this tool exists in the remote registry
        """
        client = docker.from_env()
        try:
            client.images.get_registry_data(self.container())
        except docker.errors.NotFound as e:
            return f"image {self.container()} not found"
        except Exception as e:
            return f"image {self.container()}: {str(e)}"

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
