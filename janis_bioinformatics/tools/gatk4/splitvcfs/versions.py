from .base import GatkSplitvcfsBase


class GatkSplitvcfs_4_1_3_0(GatkSplitvcfsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
