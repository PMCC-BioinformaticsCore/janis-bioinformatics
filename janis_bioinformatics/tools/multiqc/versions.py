from janis_bioinformatics.tools.multiqc.base import MultiqcBase


class Multiqc_v1_7(MultiqcBase):
    def version(self):
        return "v1.7"

    def container(self):
        return "ewels/multiqc:v1.7"
