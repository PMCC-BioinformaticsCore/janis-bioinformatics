import os
import unittest
import subprocess
from abc import ABC, abstractmethod

from janis_core import (
    CommandTool,
    Workflow,
    PythonTool,
    CommandToolBuilder,
    WorkflowBuilder,
)

BIOINFORMATICS_MODULE = "bioinformatics"


class BioinformaticsUnitTestClass(unittest.TestCase, ABC):
    input_params = {}

    @classmethod
    @abstractmethod
    def tool_full_path(cls):
        pass

    @classmethod
    def setUpClass(cls):
        curr_dir = os.getcwd()
        output_dir = os.path.join(curr_dir, "tests_output", "junytest")

        input_list = []
        for key, val in cls.input_params.items():
            input_list.append(key)
            input_list.append(val)

        subprocess.run(
            [
                "janis", "run", "--engine", "cwltool", "-o",
                os.path.join(output_dir, "cwl"),
                cls.tool_full_path(),
            ] + input_list
        )


class BioinformaticsTool(CommandTool, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE

    class UnitTestClass(BioinformaticsUnitTestClass):
        pass


class BioinformaticsWorkflow(Workflow, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE


class BioinformaticsPythonTool(PythonTool, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE

    class UnitTestClass(BioinformaticsUnitTestClass):
        pass


class BioinformaticsToolBuilder(CommandToolBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module=BIOINFORMATICS_MODULE)


class BioinformaticsWorkflowBuilder(WorkflowBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module=BIOINFORMATICS_MODULE)


