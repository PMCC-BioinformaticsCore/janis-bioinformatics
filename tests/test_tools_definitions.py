import unittest
import janis_bioinformatics

from janis_core.tool.test_definitions import ToolEvaluator
from janis_core.tool import test_helpers


class TestToolsDefinitions(unittest.TestCase):
    def test_all_tools(self):
        all_tools = test_helpers.get_all_tools([janis_bioinformatics.tools])

        failed = {}
        succeeded = set()
        # TODO: revert to full list
        # for tool_versions in all_tools:
        for tool_versions in all_tools[132:134]:
            for versioned_tool in tool_versions:
                evaluation = ToolEvaluator.evaluate(versioned_tool)

                if evaluation is True:
                    succeeded.add(versioned_tool.versioned_id())
                else:
                    failed[versioned_tool.versioned_id()] = evaluation

        test_helpers.print_test_report(failed, succeeded)

        if len(failed) > 0:
            raise Exception(
                f"There were {len(failed)} tool(s) that did not contain sufficient metadata to include in the "
                f"janis_* repository. Please check to ensure your tool is in the list below"
            )


# from janis_assistant.test_tools_framework.test_definitions import EvaluateToolDefinitions
#
#
# class TestTools(unittest.TestCase):
#     def test_tools(self):
#         try:
#             EvaluateToolDefinitions().run_test([janis_bioinformatics.tools])
#         except Exception as e:
#             self.fail(e)
