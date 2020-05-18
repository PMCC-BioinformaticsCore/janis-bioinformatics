from .base import GatkSetnmanduqtagsBase


class GatkSetnmanduqtags_4_1_3_0(GatkSetnmanduqtagsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
