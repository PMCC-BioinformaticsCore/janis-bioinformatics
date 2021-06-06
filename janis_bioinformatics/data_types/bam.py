import subprocess
from janis_core import File
from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)
import operator
from typing import Optional, List


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
    def basic_test(
        cls,
        tag: str,
        min_bam_size: int,
        flagstat: Optional[str] = None,
        md5: Optional[str] = None,
    ) -> List[TTestExpectedOutput]:
        outcome = [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.ge,
                expected_value=min_bam_size,
            )
        ]
        if flagstat is not None:
            outcome += [
                TTestExpectedOutput(
                    tag=tag,
                    preprocessor=Bam.flagstat,
                    operator=operator.eq,
                    expected_file=flagstat,
                )
            ]
        if md5 is not None:
            outcome += [
                TTestExpectedOutput(
                    tag=tag,
                    preprocessor=TTestPreprocessor.FileMd5,
                    operator=operator.eq,
                    expected_value=md5,
                ),
            ]
        return outcome


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
    def basic_test(
        cls,
        tag: str,
        min_bam_size: int,
        min_bai_size: int,
        flagstat: Optional[str] = None,
        bam_md5: Optional[str] = None,
        bai_md5: Optional[str] = None,
    ) -> List[TTestExpectedOutput]:
        outcome = super().basic_test(tag, min_bam_size, flagstat, bam_md5) + [
            TTestExpectedOutput(
                tag=tag,
                suffix_secondary_file=".bai",
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.ge,
                expected_value=min_bai_size,
            ),
        ]
        if bai_md5 is not None:
            outcome += [
                TTestExpectedOutput(
                    tag=tag,
                    suffix_secondary_file=".bai",
                    preprocessor=TTestPreprocessor.FileMd5,
                    operator=operator.eq,
                    expected_value=bai_md5,
                ),
            ]
        return outcome
