import unittest
import janis_bioinformatics
from parameterized import parameterized

from janis_core.tool.test_suite_runner import ToolTestSuiteRunner
from janis_core.tool import test_helpers as test_helper

all_tools = test_helper.get_all_tools([janis_bioinformatics.tools])
all_versioned_tools = []
# TODO: revert to full list
# for tool_versions in all_tools:
for tool_versions in all_tools[148:152]:
    for versioned_tool in tool_versions:
        all_versioned_tools.append(versioned_tool)


class RunAllToolsTestSuite(unittest.TestCase):
    failed_tools = {}
    succeeded_tools = set()

    @parameterized.expand([
        [t.id(), t] for t in all_versioned_tools
    ])
    def test_one_tool(self, name, tool):
        if not tool.tests():
            error_message = "No test suite provided"
            self.failed_tools[name] = error_message
            self.fail(error_message)
        else:
            runner = ToolTestSuiteRunner(tool)

            for tc in tool.tests():
                with self.subTest(name=str(tc.name)):
                    failed, succeeded = runner.run_one_test_case(tc)

                if len(failed) > 0:
                    self.failed_tools[name] = f"{len(failed)} test case(s) failed"
                    self.fail("; ".join(failed))
                else:
                    self.succeeded_tools.add(name)

    def test_report(self):
        test_helper.print_test_report(failed=self.failed_tools, succeeded=self.succeeded_tools)
