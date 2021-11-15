from janis_bioinformatics.tools.multiqc.base import MultiqcBase


class Multiqc_1_7(MultiqcBase):
    def version(self):
        return "1.7"

    def container(self):
        return "quay.io/biocontainers/multiqc:1.7--py_4"


class Multiqc_1_11(MultiqcBase):
    def version(self):
        return "1.11"

    def container(self):
        return "quay.io/biocontainers/multiqc:1.11--pyhdfd78af_0"


MultiqcLatest = Multiqc_1_11
