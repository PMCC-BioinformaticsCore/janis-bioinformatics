from janis_bioinformatics.tools.illumina.happy.happybase import HapPyValidatorBase


class HapPyValidator_0_3_9(HapPyValidatorBase):
    @staticmethod
    def container():
        return "pkrusche/hap.py:v0.3.9"

    @staticmethod
    def version():
        return "v0.3.9"

HapPyValidatorLatest = HapPyValidator_0_3_9
