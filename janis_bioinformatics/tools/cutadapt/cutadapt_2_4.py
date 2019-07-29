from janis_bioinformatics.tools.cutadapt.base_2 import CutAdaptBase_2


class CutAdapt_2_4(CutAdaptBase_2):

    @staticmethod
    def container():
        return "quay.io/biocontainers/cutadapt:2.4--py37h14c3975_0"

    @staticmethod
    def version():
        return "2.4"
