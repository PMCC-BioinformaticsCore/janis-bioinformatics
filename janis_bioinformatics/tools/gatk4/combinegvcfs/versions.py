from .base import GatkCombinegvcfsBase


class GatkCombinegvcfs_4_1_3_0(GatkCombinegvcfsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
