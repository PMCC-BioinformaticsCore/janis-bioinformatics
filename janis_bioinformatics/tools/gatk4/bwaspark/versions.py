from .base import GatkBwasparkBase


class GatkBwaspark_4_1_3_0(GatkBwasparkBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
