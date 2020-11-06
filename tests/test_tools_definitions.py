import unittest
from nose.plugins.attrib import attr
from parameterized import parameterized

import janis_bioinformatics
from janis_core.tool.test_definitions import ToolEvaluator
from janis_core.tool import test_helpers

all_tools = test_helpers.get_all_tools([janis_bioinformatics.tools])

all_versioned_tools = []
# TODO: revert to full list
for tool_versions in all_tools:
    for versioned_tool in tool_versions:
        all_versioned_tools.append(versioned_tool)


class TestToolsDefinitions(unittest.TestCase):
    failed = {}
    succeeded = set()

    @parameterized.expand([[t.versioned_id(), t] for t in all_versioned_tools])
    @attr("travis")
    def test(self, name, tool):
        evaluation = ToolEvaluator.evaluate(tool)

        if evaluation is True:
            self.succeeded.add(tool.versioned_id())
        else:
            self.failed[tool.versioned_id()] = evaluation
            raise Exception(evaluation)

    def test_report(self):
        test_helpers.print_test_report(failed=self.failed, succeeded=self.succeeded)

        if len(self.failed) > 0:
            raise Exception(
                f"There were {len(self.failed)} tool(s) that did not contain sufficient metadata to include in the "
                f"janis_* repository. Please check to ensure your tool is in the list below"
            )
