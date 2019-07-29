from janis_bioinformatics.tools.cutadapt.base_1 import CutAdaptBase_1


class CutAdapt_1_18(CutAdaptBase_1):

    @staticmethod
    def container():
        return "quay.io/biocontainers/cutadapt:1.18--py37h14c3975_1"

    @staticmethod
    def version():
        return "1.18"
