import operator
import os
import sys
from abc import ABC

from janis_core import (
    CommandTool,
    Workflow,
    PythonTool,
    CommandToolBuilder,
    WorkflowBuilder,
    Array,
)
from janis_core.tool.test_classes import TTestExpectedOutput, TTestPreprocessor

BIOINFORMATICS_MODULE = "bioinformatics"


class BioinformaticsTool(CommandTool, ABC):
    def tool_module(self):
        return BIOINFORMATICS_MODULE

    def minimal_test(self):
        outcome = []
        for i in self.outputs():
            array_index = 0 if i.output_type.is_base_type(Array) else None
            outcome += [
                TTestExpectedOutput(
                    tag=i.tag,
                    array_index=array_index,
                    preprocessor=TTestPreprocessor.FileSize,
                    operator=operator.gt,
                    expected_value=0,
                )
            ]
            if i.secondaries_present_as is not None:
                for suffix in i.secondaries_present_as.keys():
                    outcome += [
                        TTestExpectedOutput(
                            tag=i.tag,
                            array_index=array_index,
                            suffix_secondary_file=suffix,
                            preprocessor=TTestPreprocessor.FileSize,
                            operator=operator.gt,
                            expected_value=0,
                        )
                    ]
            # if i.output_type.is_base_type(Array):
            #     outcome += [
            #         TTestExpectedOutput(
            #             tag=i.tag,
            #             #array_index=0,
            #             preprocessor=TTestPreprocessor.FileSize,
            #             operator=operator.gt,
            #             expected_value=0,
            #         )
            #     ]
            #     if i.secondaries_present_as is not None:
            #         for suffix in i.secondaries_present_as.keys():
            #             print(suffix)
            #             outcome += [
            #                 TTestExpectedOutput(
            #                     tag=i.tag,
            #                     #array_index=0,
            #                     suffix_secondary_file=suffix,
            #                     preprocessor=TTestPreprocessor.FileSize,
            #                     operator=operator.gt,
            #                     expected_value=0,
            #                 )
            #             ]
            # else:
            #     outcome += [
            #         TTestExpectedOutput(
            #             tag=i.tag,
            #             preprocessor=TTestPreprocessor.FileSize,
            #             operator=operator.gt,
            #             expected_value=0,
            #         )
            #     ]
            #     if i.secondaries_present_as is not None:
            #         for suffix in i.secondaries_present_as.keys():
            #             print(suffix)
            #             outcome += [
            #                 TTestExpectedOutput(
            #                     tag=i.tag,
            #                     suffix_secondary_file=suffix,
            #                     preprocessor=TTestPreprocessor.FileSize,
            #                     operator=operator.gt,
            #                     expected_value=0,
            #                 )
            #             ]
        return outcome


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
