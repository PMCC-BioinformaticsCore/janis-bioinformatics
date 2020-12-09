import unittest
import sys
from parameterized import parameterized

import janis_bioinformatics

from janis_core.tool.test_suite_runner import ToolTestSuiteRunner
from janis_core.tool import test_helpers

try:
    from nose.plugins.attrib import attr
except ImportError:

    def attr(ob):
        return ob


version = None
for arg in sys.argv:
    if arg.startswith("tool="):
        parts = arg.split("=")
        tool_id = parts[1]

    if arg.startswith("engine="):
        parts = arg.split("=")
        engine = parts[1]

    if arg.startswith("version="):
        parts = arg.split("=")
        version = parts[1]

tool = test_helpers.get_one_tool(tool_id, [janis_bioinformatics.tools], version)
runner = ToolTestSuiteRunner(tool)


class TestOneTool(unittest.TestCase):

    failed_cases = {}
    succeeded_cases = set()

    @parameterized.expand([[tc.name, tc] for tc in tool.tests()])
    @attr("test_suite")
    def test(self, name, test_case):
        failed, succeeded = runner.run_one_test_case(test_case, engine)

        if len(failed) > 0:
            error_msg = "\n".join(failed)
            self.failed_cases[name] = error_msg
            self.fail(error_msg)
        else:
            self.succeeded_cases.add(name)

    @attr("test_suite")
    def test_report(self):
        # Note: This function has to be run LASt! (these tests are run by alphabetical order
        print(f"{tool.versioned_id()} - {engine}")
        test_helpers.print_test_report(
            failed=self.failed_cases,
            succeeded=self.succeeded_cases,
            id_column_header="Test Case",
        )
