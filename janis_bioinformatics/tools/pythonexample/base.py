import os
import operator
from pathlib import Path
from typing import Dict, Optional, List, Any

from janis_core import TOutput, File, Array, Int
from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsPythonTool,
)
from janis_core import ToolMetadata, Logger, PythonTool
from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)


class FileDiffOperator:
    @classmethod
    def new_lines(cls, output_diff, expected_new_lines):
        new_lines = []
        for diff_line in output_diff:
            prefix = diff_line[0:3]
            if prefix in ["+++", "---", "@@ "]:
                continue

            if diff_line.startswith("+"):
                diff_line = diff_line.strip()
                diff_line = diff_line[1:]

                new_lines.append(diff_line)

        return new_lines == expected_new_lines


class InsertLineBase(BioinformaticsPythonTool):
    @staticmethod
    def code_block(
        in_file: File, line_to_insert: str, insert_after_line: int
    ) -> Dict[str, Any]:
        from shutil import copyfile

        # dst = copyfile(in_file, "./out.file")
        dst = "./output.txt"

        with open(in_file, "r") as fin, open(dst, "w") as fout:
            count = 0
            for line in fin:
                count += 1
                fout.write(line)

                if count == insert_after_line:
                    fout.write(line_to_insert + "\n")

        line_count = count + 1
        misc_files = [dst, dst]

        return {"out_file": dst, "line_count": line_count, "misc_files": misc_files}

    def friendly_name(self) -> Optional[str]:
        return "Insert line to a text file"

    def outputs(self) -> List[TOutput]:
        return [
            TOutput("out_file", File),
            TOutput("line_count", int),
            TOutput("misc_files", Array(File)),
        ]

    def id(self) -> str:
        return "InsertLine"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated="2020-07-30",
            institution="Melbourne Bioinformatics",
        )

    def tests(self):
        return [
            TTestCase(
                name="insert-one-line",
                input={
                    "in_file": os.path.join(self.test_data_path(), "input.txt"),
                    "line_to_insert": "abc",
                    "insert_after_line": 1,
                },
                output=[
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileMd5,
                        operator=operator.eq,
                        expected_value="85d7c20f3e0c7af4510ca5d1f4997b9f",
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileDiff,
                        file_diff_source=os.path.join(
                            self.test_data_path(), "expected_output_1.txt"
                        ),
                        operator=operator.eq,
                        expected_value=[],
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileContent,
                        operator=operator.eq,
                        expected_value="test\nabc\nsame\nsame\nlast line\n",
                    ),
                ],
            ),
            TTestCase(
                name="append-one-line",
                input={
                    "in_file": os.path.join(self.test_data_path(), "input.txt"),
                    "line_to_insert": "my new line",
                    "insert_after_line": 4,
                },
                output=[
                    TTestExpectedOutput(
                        tag="line_count",
                        preprocessor=TTestPreprocessor.Value,
                        operator=operator.eq,
                        expected_value="5",
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileDiff,
                        file_diff_source=os.path.join(
                            self.test_data_path(), "input.txt"
                        ),
                        operator=FileDiffOperator.new_lines,
                        expected_value=["my new line"],
                    ),
                    TTestExpectedOutput(
                        tag="misc_files",
                        array_index=1,
                        preprocessor=TTestPreprocessor.FileContent,
                        operator=operator.eq,
                        expected_value="test\nsame\nsame\nlast line\nmy new line\n",
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileMd5,
                        operator=operator.eq,
                        expected_value="d680893100be1181c8a7071618ff4524",
                    ),
                ],
            ),
        ]

    # TODO: delete
    @classmethod
    def tool_full_path(cls):
        return Path(__file__).absolute()


if __name__ == "__main__":
    InsertLineBase().translate("cwl")
