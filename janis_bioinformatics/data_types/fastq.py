from typing import Any, Dict

from janis_core import File, Array, Logger


class Fastq(File):
    def __init__(self, optional=False):
        super().__init__(optional=optional, extension=".fastq")

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
        super().__init__(optional=optional, extension=".fastq.gz")

    @staticmethod
    def name():
        return "FastqGz"

    def doc(self):
        return (
            "FastqGz files are compressed sequence data with quality score, there are different types"
            "with no standard: https://en.wikipedia.org/wiki/FASTQ_format"
        )


class FastqGzPair(Array):
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
        return (
            super().validate_value(meta, allow_null_if_not_optional) and len(meta) == 2
        )

    def invalid_value_hint(self, meta):
        prev = super().invalid_value_hint(meta)
        hints = []
        if prev:
            hints.append(prev)
        if len(meta) != 2:
            hints.append(f"There must be exactly 2 (found {len(meta)}) fastq files")
        return ", ".join(hints)


class FastqPair(Array):
    def __init__(self, optional=False):
        super().__init__(File(optional=False, extension=".fastq"), optional=optional)

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
