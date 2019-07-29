from janis_bioinformatics.tools.babrahambioinformatics.fastqc.base import FastQCBase


class FastQC_0_11_5(FastQCBase):

    @staticmethod
    def version():
        return "v0.11.5"

    @staticmethod
    def container():
        return "biocontainers/fastqc:v0.11.5_cv3"


if __name__ == "__main__":
    print(FastQC_0_11_5().translate("cwl"))