from .base import GatkMergemutect2Callswithmc3Base


class GatkMergemutect2Callswithmc3_4_1_3_0(GatkMergemutect2Callswithmc3Base):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
