import unittest
import sys
from parameterized import parameterized
from nose.plugins.attrib import attr

import janis_bioinformatics

from janis_core.tool.test_suite_runner import ToolTestSuiteRunner
from janis_core.tool import test_helpers as test_helper

for arg in sys.argv:
    if arg.startswith("tool="):
        parts = arg.split("=")
        tool_id = parts[1]
        break

print(tool_id)

tool = test_helper.get_one_tool(tool_id, [janis_bioinformatics.tools])
runner = ToolTestSuiteRunner(tool)


class TestOneTool(unittest.TestCase):

    @parameterized.expand([
        [tc.name, tc] for tc in tool.tests()
    ])
    @attr("test_suite")
    def test_tool(self, name, test_case):
        failed, succeeded = runner.run_one_test_case(test_case)

        if len(failed) > 0:
            self.fail("; ".join(failed))
