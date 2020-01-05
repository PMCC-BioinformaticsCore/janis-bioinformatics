from janis_bioinformatics.tools.illumina.happy.happybase import HapPyValidatorBase


class HapPyValidator_0_3_9(HapPyValidatorBase):
    def container(self):
        return "pkrusche/hap.py:v0.3.9"

    def version(self):
        return "v0.3.9"


HapPyValidatorLatest = HapPyValidator_0_3_9
