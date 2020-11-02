import unittest
from parameterized import parameterized

import janis_bioinformatics

from janis_core.tool.test_suite_runner import ToolTestSuiteRunner
from janis_core.tool import test_helpers as test_helper

all_engines = ToolTestSuiteRunner.get_available_engines()
all_tools = test_helper.get_all_tools([janis_bioinformatics.tools])

all_versioned_tools = []
# TODO: revert to full list
for tool_versions in all_tools:
    for versioned_tool in tool_versions:
        all_versioned_tools.append(versioned_tool)


class RunAllToolsTestSuite(unittest.TestCase):
    failed_tools = {}
    succeeded_tools = set()

    @parameterized.expand([
        [f"{tool.versioned_id()} - {engine}", engine, tool] for tool in all_versioned_tools for engine in all_engines
    ])
    def test(self, name, engine, tool):
        if not tool.tests():
            error_message = "No test suite provided"
            self.failed_tools[name] = error_message
            self.fail(error_message)
        else:
            runner = ToolTestSuiteRunner(tool)

            n_test_case_failed = 0
            error_messages = []
            for tc in tool.tests():
                error_msg = None
                try:
                    failed, succeeded = runner.run_one_test_case(tc, engine)

                    # the len(failed) here is the number of expected output that fails per test case
                    if len(failed) > 0:
                        error_msg = ";".join(failed)

                except Exception as e:
                    error_msg = str(e)

                except SystemExit as e:
                    error_msg = f"Workflow execution failed (exit code: {e.code})"

                finally:
                    if error_msg is not None:
                        n_test_case_failed += 1
                        error_messages.append(f"{tc.name}: {error_msg}")

            if n_test_case_failed > 0:
                self.failed_tools[name] = f"{n_test_case_failed} test case(s) failed"
                self.fail("\n".join(error_messages))
            else:
                self.succeeded_tools.add(name)

    def test_report(self):
        test_helper.print_test_report(failed=self.failed_tools, succeeded=self.succeeded_tools)

        if (len(self.failed_tools) > 0):
            raise Exception(
                f"There were {len(self.failed_tools)} tool(s) did not pass their unit tests"
            )