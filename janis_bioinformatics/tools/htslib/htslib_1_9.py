from abc import ABC

from .htslibbase import HtsLibBase


class HTSLib_1_9(HtsLibBase, ABC):

    @staticmethod
    def container():
        return "quay.io/biocontainers/htslib:1.9--ha228f0b_7"

    @staticmethod
    def version():
        return "1.9"
