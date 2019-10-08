from abc import ABC


class Gatk_4_1_3_0(ABC):
    @staticmethod
    def container():
        return "broadinstitute/gatk:4.1.3.0"

    @staticmethod
    def version():
        return "4.1.3.0"
