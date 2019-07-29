from janis_bioinformatics.tools.babrahambioinformatics.fastqc.base import FastQCBase


class FastQC_0_11_8(FastQCBase):

    @staticmethod
    def version():
        return "v0.11.8"

    @staticmethod
    def container():
        return "quay.io/biocontainers/fastqc:0.11.8--1"

