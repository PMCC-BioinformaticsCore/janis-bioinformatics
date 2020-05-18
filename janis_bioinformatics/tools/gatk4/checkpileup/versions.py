from .base import GatkCheckpileupBase


class GatkCheckpileup_4_1_3_0(GatkCheckpileupBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
