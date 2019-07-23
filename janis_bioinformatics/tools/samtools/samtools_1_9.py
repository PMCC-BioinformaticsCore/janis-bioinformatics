from abc import ABC
from .samtoolstoolbase import SamToolsToolBase


class SamTools_1_9(SamToolsToolBase, ABC):
    @staticmethod
    def docker():
        return "quay.io/biocontainers/samtools:1.9--h8571acd_11"

    @staticmethod
    def version():
        return "1.9"
