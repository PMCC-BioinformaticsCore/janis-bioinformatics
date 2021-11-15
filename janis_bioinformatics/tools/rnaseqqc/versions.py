from janis_bioinformatics.tools.rnaseqqc.base import RNASeqQCBase


class RNASeqQC_2_3_5(RNASeqQCBase):
    def version(self):
        return "2.3.5"

    def container(self):
        return "quay.io/biocontainers/rna-seqc:2.3.5--he24ac62_2"
