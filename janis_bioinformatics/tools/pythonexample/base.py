import unittest
from abc import ABC
from pathlib import Path
from typing import Dict, Optional, List, Any

from janis_core import TOutput, File
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool, BioinformaticsUnitTestClass
from janis_core import ToolMetadata, Logger, PythonTool


class InsertLineBase(BioinformaticsPythonTool):
    @staticmethod
    def code_block(in_file: File, line_to_insert: str, insert_after_line: int) -> Dict[str, Any]:
        from shutil import copyfile

        # dst = copyfile(in_file, "./out.file")
        dst = "./out.file"

        with open(in_file, "r") as fin, open(dst, "w") as fout:
            count = 0
            for line in fin:
                count += 1
                fout.write(line)

                if count == insert_after_line:
                    fout.write(line_to_insert)

        line_count = count + 1

        return {
            "out_file": dst,
            "line_count": line_count
        }

    def friendly_name(self) -> Optional[str]:
        return "Insert line to a text file"

    def outputs(self) -> List[TOutput]:
        return [
            TOutput("out_file", File),
            TOutput("line_count", int)
        ]

    def id(self) -> str:
        return "InsertLine"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated="2020-07-30",
            institution="Melbourne Bioinformatics"
        )

    class UnitTestClass(BioinformaticsUnitTestClass):

        @classmethod
        def tool_full_path(cls):
            return Path(__file__).absolute()

        input_params = {
            "--in-file": "/Users/jkesumadewi/projects/janis-bioinformatics/myworkdir/input.txt",
            "--line-to-insert": "abc",
            "--insert-after-line": "1"
        }

        def test_good(self):
            print("good")

        def test_bad(self):
            print("bad")
            assert True is False

        def test_error(self):
            raise Exception("bla bla")


if __name__ == "__main__":
    InsertLineBase().translate("cwl")
