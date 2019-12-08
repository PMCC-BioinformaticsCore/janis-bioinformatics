from janis_bioinformatics.tools.babrahambioinformatics.fastqc.base import FastQCBase


class FastQC_0_11_8(FastQCBase):
    def version(self):
        return "v0.11.8"

    def container(self):
        return "quay.io/biocontainers/fastqc:0.11.8--1"
