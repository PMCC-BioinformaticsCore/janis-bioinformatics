from janis_bioinformatics.tools.cutadapt.base import CutAdaptBase


class CutAdapt_1_18(CutAdaptBase):

    @staticmethod
    def docker():
        return "quay.io/biocontainers/cutadapt:1.18--py37h14c3975_1"
