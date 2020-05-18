from .base import GatkIntervallisttoolsBase


class GatkIntervallisttools_4_1_3_0(GatkIntervallisttoolsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
