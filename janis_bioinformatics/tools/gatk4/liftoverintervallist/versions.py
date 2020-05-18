from .base import GatkLiftoverintervallistBase


class GatkLiftoverintervallist_4_1_3_0(GatkLiftoverintervallistBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
