from abc import ABC

class Gatk_4_0_12(ABC):

    @staticmethod
    def docker():
        return "broadinstitute/gatk:4.0.12.0"

    @staticmethod
    def version():
        return "4.0.12.0"
