from janis_bioinformatics.tools.multiqc.base import MultiqcBase


class Multiqc_v1_7(MultiqcBase):
    @staticmethod
    def version():
        return "v1.7"

    @staticmethod
    def container():
        return "ewels/multiqc:v1.7"
