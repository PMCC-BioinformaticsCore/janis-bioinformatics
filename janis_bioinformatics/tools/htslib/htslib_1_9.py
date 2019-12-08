from abc import ABC

from .htslibbase import HtsLibBase


class HTSLib_1_9(HtsLibBase, ABC):
    def container(self):
        return "quay.io/biocontainers/htslib:1.9--ha228f0b_7"

    def version(self):
        return "1.9"
