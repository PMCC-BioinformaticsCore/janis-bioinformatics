import operator
import os.path
import zipfile
from typing import Any, Dict, List, Optional

from janis_core import File, Array, Logger
from janis_core.tool.test_classes import TTestExpectedOutput, TTestPreprocessor


class Fastq(File):
    def __init__(self, optional=False):
        super().__init__(
            optional=optional, extension=".fastq", alternate_extensions={".fq"}
        )

    @staticmethod
    def name():
        return "Fastq"

    def doc(self):
        return (
            "FASTQ files are text files containing sequence data with quality score, there are different types"
            "with no standard: https://www.drive5.com/usearch/manual/fastq_files.html"
        )


class FastqGz(File):
    def __init__(self, optional=False):
        super().__init__(
            optional=optional, extension=".fastq.gz", alternate_extensions={".fq.gz"}
        )

    @staticmethod
    def name():
        return "FastqGz"

    def doc(self):
        return (
            "FastqGz files are compressed sequence data with quality score, there are different types"
            "with no standard: https://en.wikipedia.org/wiki/FASTQ_format"
        )

    @classmethod
    def basic_test(cls, tag: str, min_size: int) -> List[TTestExpectedOutput]:
        return [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.ge,
                expected_value=min_size,
            ),
        ]


class FastqGzPairedEnd(Array):
    def __init__(self, optional=False):
        super().__init__(FastqGz, optional=optional)

    @staticmethod
    def name():
        return "FastqGzPair"

    def id(self):
        if self.optional:
            return f"Optional<{self.name()}>"
        return self.name()

    def doc(self):
        return "Paired end FastqGz files"

    def validate_value(self, meta: Any, allow_null_if_not_optional: bool):
        super_is_valid = super().validate_value(meta, allow_null_if_not_optional)
        if not super_is_valid or meta is None:
            return super_is_valid

        return len(meta) == 2

    def invalid_value_hint(self, meta):
        prev = super().invalid_value_hint(meta)
        hints = []
        if prev:
            hints.append(prev)

        if meta is not None and len(meta) != 2:
            hints.append(f"There must be exactly 2 (found {len(meta)}) fastq files")
        return ", ".join(hints)

    @classmethod
    def ge(cls, file_paths: str, expected_sizes: List[int]):
        """

        :param file_paths: a string containing all file paths, separated by |
        :type file_paths: str
        :param expected_sizes: expected minimum sizes of all files
        :type expected_sizes: List[int]
        :return: a boolean value indicating if all files are bigger than or equal to their expected minimum sizes
        """
        files = file_paths.split("|")
        if len(files) != len(expected_sizes):
            return "Number of expected values don't match number of outputs"
        for file in files:
            unzipped = zipfile.ZipFile(file)
            if "R1" in unzipped.namelist()[0]:
                if os.path.getsize(file) < expected_sizes[0]:
                    return False
            else:
                if os.path.getsize(file) < expected_sizes[1]:
                    return False
        return True

    @classmethod
    def basic_test(
        cls,
        tag: str,
        min_total_size: int,
        min_first_size: Optional[int] = None,
        min_second_size: Optional[int] = None,
    ) -> List[TTestExpectedOutput]:
        outcome = [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.ListSize,
                operator=operator.eq,
                expected_value=2,
            ),
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.ListOfFilesTotalSize,
                operator=operator.ge,
                expected_value=min_total_size,
            ),
        ]

        # An example of how FastqGzPairedEnd.ge is used; can be removed if deemed unnecessary
        if min_first_size is not None and min_second_size is not None:
            outcome += [
                TTestExpectedOutput(
                    tag=tag,
                    preprocessor=TTestPreprocessor.Value,
                    operator=FastqGzPairedEnd.ge,
                    expected_value=[min_first_size, min_second_size],
                )
            ]
        return outcome


class FastqPairedEnd(Array):
    def __init__(self, optional=False):
        super().__init__(Fastq(optional=False), optional=optional)

    def id(self):
        if self.optional:
            return f"Optional<{self.name()}>"
        return self.name()

    @staticmethod
    def name():
        return "FastqPair"

    def doc(self):
        return "Paired end Fastq files "

    def validate_value(self, meta: Any, allow_null_if_not_optional: bool):
        if not super().validate_value(meta, allow_null_if_not_optional):
            return False
        return len(meta) == 2

    def invalid_value_hint(self, meta):
        prev = super().invalid_value_hint(meta)
        hints = []
        if prev:
            hints.append(prev)
        if len(meta) != 2:
            hints.append(f"There must be exactly 2 (found {len(meta)}) fastq files")
        return ", ".join(hints)


FastqGzPair = FastqGzPairedEnd
FastqPair = FastqPairedEnd
