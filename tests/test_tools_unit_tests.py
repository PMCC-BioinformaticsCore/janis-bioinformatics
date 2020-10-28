import unittest
from parameterized import parameterized

import janis_bioinformatics

from janis_core.tool.test_suite_runner import ToolTestSuiteRunner
from janis_core.tool import test_helpers as test_helper

all_tools = test_helper.get_all_tools([janis_bioinformatics.tools])

all_versioned_tools = []
# TODO: revert to full list
# for tool_versions in all_tools:
# for tool_versions in all_tools[150:152]:
# for tool_versions in all_tools[47:53]:
for tool_versions in all_tools[50:51]: # view
# for tool_versions in all_tools[51:52]: # index
# for tool_versions in all_tools[52:53]: # faidx
# for tool_versions in all_tools[47:48]: # flagstat
# for tool_versions in all_tools[48:49]: # mpileup
    for versioned_tool in tool_versions:
        all_versioned_tools.append(versioned_tool)


class RunAllToolsTestSuite(unittest.TestCase):
    failed_tools = {}
    succeeded_tools = set()

    @parameterized.expand([
        [t.versioned_id(), t] for t in all_versioned_tools
    ])
    def test_one_tool(self, name, tool):
        if not tool.tests():
            error_message = "No test suite provided"
            self.failed_tools[name] = error_message
            self.fail(error_message)
        else:
            runner = ToolTestSuiteRunner(tool)
            fail_count_by_engine = {}

            for tc in tool.tests():
                test_results = runner.run_one_test_case(tc)

                for engine in test_results:
                    failed, succeeded = test_results[engine]

                    if engine not in fail_count_by_engine:
                        fail_count_by_engine[engine] = 0

                    if len(failed) > 0:
                        fail_count_by_engine[engine] += 1

            error_messages = []
            for engine in fail_count_by_engine:
                fail_count = fail_count_by_engine[engine]
                name_on_report = f"{name} - {engine}"
                if fail_count > 0:
                    self.failed_tools[name_on_report] = f"{fail_count} test case(s) failed"
                    error_messages.append(f"{engine}: {'; ' .join(failed)}")
                else:
                    self.succeeded_tools.add(name_on_report)

            if error_messages:
                self.fail("| ".join(error_messages))

    def test_report(self):
        test_helper.print_test_report(failed=self.failed_tools, succeeded=self.succeeded_tools)

