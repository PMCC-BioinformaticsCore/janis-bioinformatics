import subprocess
from janis_core import File
from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)
import operator


class Bam(File):
    def __init__(self, optional=False):
        super().__init__(optional, extension=".bam")

    @staticmethod
    def name():
        return "BAM"

    def doc(self):
        return "A binary version of a SAM file, http://software.broadinstitute.org/software/igv/bam"

    @classmethod
    def flagstat(cls, file_path: str):
        command = ["samtools", "flagstat", file_path]
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        if result.stderr:
            raise Exception(result.stderr)

        return result.stdout

    @classmethod
    def equal(cls, file_path_1: str, file_path_2: str):
        flagstat1 = cls.flagstat(file_path_1)
        flagstat2 = cls.flagstat(file_path_2)

        return flagstat1 == flagstat2

    @classmethod
    def basic_test(cls, tag, bam_size, value, flagstat=""):
        output = [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.eq,
                expected_value=bam_size,
            ),
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.Value,
                operator=Bam.equal,
                expected_value=value,
            ),
        ]

        if flagstat == "":
            return output

        return output + [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=Bam.flagstat,
                operator=operator.eq,
                expected_file=flagstat,
            ),
        ]


class BamBai(Bam):
    @staticmethod
    def name():
        return "IndexedBam"

    @staticmethod
    def secondary_files():
        return [".bai"]

    def doc(self):
        return "A Bam and bai as the secondary"

    @classmethod
    def basic_test(cls, tag, bam_size, bai_size, value, flagstat=""):
        return Bam.basic_test(tag, bam_size, value, flagstat) + [
            TTestExpectedOutput(
                tag=tag,
                suffix_secondary_file=".bai",
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.gt,
                expected_value=bai_size,
            ),
        ]
