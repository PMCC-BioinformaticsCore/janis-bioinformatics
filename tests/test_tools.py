import unittest
import janis_bioinformatics
import janis_core as jc
from typing import Dict, Optional, List
from tabulate import tabulate
from .evaluation_helpers import evaluate

print(janis_bioinformatics.tools)


class EvaluateToolDefinitions(unittest.TestCase):
    def evaluate(self, tool: jc.Tool):
        if tool.type() == jc.ToolType.Workflow:
            return self.evaluate_workflow(tool)
        elif tool.type() == jc.ToolType.CommandTool:
            return self.evaluate_command_tool(tool)
        elif tool.type() == jc.ToolType.CodeTool:
            return self.evaluate_code_tool(tool)
        raise Exception("Unrecognised tool type: " + str(tool.type()))

    def evaluate_command_tool(self, tool: jc.CommandTool):
        evaluation = evaluate(tool)
        return self._read_evaluation(evaluation)

    def evaluate_code_tool(self, tool: jc.CodeTool):
        evaluation = evaluate(tool)
        return self._read_evaluation(evaluation)

    def evaluate_workflow(self, wf):
        return True

    @staticmethod
    def _read_evaluation(evaluation: Dict[str, str]):
        errors = []
        for field in evaluation:
            if evaluation[field] is not True:
                errors.append(evaluation[field])

        if not errors:
            return True

        return "; ".join(errors)

    def test_tools(self):
        shed = jc.JanisShed
        shed.hydrate(force=True, modules=[janis_bioinformatics.tools])
        all_tools = shed.get_all_tools()

        failed = {}
        succeeded = set()

        # TODO: revert to full list
        # for tool_versions in all_tools:
        for tool_versions in all_tools[132:134]:
            for versioned_tool in tool_versions:
                evaluation = self.evaluate(versioned_tool)

                if evaluation is True:
                    succeeded.add(versioned_tool.versioned_id())
                else:
                    failed[versioned_tool.versioned_id()] = evaluation

        headers = ["Tool", "Status", "Description"]
        formatted_failed = [(tid, "FAILED", terror) for tid, terror in failed.items()]
        formatted_passed = [(tid, "PASSED", "") for tid in succeeded]
        print(tabulate([*formatted_failed, *formatted_passed], headers=headers))

        if len(failed) > 0:
            self.fail(
                f"There were {len(failed)} tool(s) that did not contain sufficient metadata to include in the janis_* repository. Please check to ensure your tool is in the list below"
            )
