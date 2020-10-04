import docker
import os
from typing import Dict, Union
from abc import ABC

from janis_core.translationdeps.supportedtranslations import SupportedTranslation
from janis_core.translations.cwl import CwlTranslator
from janis_core.translations.wdl import WdlTranslator
from janis_core.utils.metadata import ToolMetadata


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
        evaluation['metadata'] = self.evaluate_metadata()
        evaluation['container'] = self.evaluate_container()
        evaluation['translation'] = self.evaluate_translation()

        return evaluation

    def evaluate_friendly_name(self) -> Union[str, bool]:
        if self.friendly_name() is None:
            return "Missing friendly name"

        return True

    def evaluate_metadata(self) -> Union[str, bool]:
        if isinstance(self.metadata, ToolMetadata):
            required = {
                "contributors": self.metadata.contributors,
                "created date": self.metadata.dateCreated,
                "updated date": self.metadata.dateUpdated,
                "institution": self.metadata.institution,
            }

            missing = []
            for key, field in required.items():
                if field is None or not field:
                    missing.append(key)

            if missing:
                return f"Missing metadata: {', '.join(missing)}"
        # elif isinstance(self.metadata, ...):
        else:
            return "Incorrect metadata class"

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

    def evaluate_translation(self):
        cwl_file_path = f"/tmp/janis/tests/{self.id()}/cwl"
        wdl_file_path = f"/tmp/janis/tests/{self.id()}/wdl"

        self.translate(SupportedTranslation.CWL, to_console=False, to_disk=True, export_path=cwl_file_path)
        self.translate(SupportedTranslation.WDL, to_console=False, to_disk=True, export_path=wdl_file_path)

        # TODO: translate and validate
        CwlTranslator.validate_command_for(cwl_file_path, "", "", "")
        WdlTranslator.validate_command_for(wdl_file_path, "", "", "")

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
