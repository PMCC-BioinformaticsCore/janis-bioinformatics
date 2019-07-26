from typing import Any, Dict

from janis_core import File, Array, Logger


class Fastq(Array):
    def __init__(self, optional=False):
        super().__init__(File(optional=False, extension=".fastq"), optional=optional)

    def id(self):
        if self.optional:
            return f"Optional<{self.name()}>"
        return self.name()

    @staticmethod
    def name():
        return "Fastq"

    def doc(self):
        return (
            "FASTQ files are text files containing sequence data with quality score, there are different types"
            "with no standard: https://www.drive5.com/usearch/manual/fastq_files.html"
        )

    @classmethod
    def schema(cls) -> Dict:
        return {"path": {"type": "string", "required": True}}
