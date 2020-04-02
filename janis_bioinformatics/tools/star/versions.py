from janis_bioinformatics.tools.star.base import StarAlignerBase


class StarAligner_2_7_1(StarAlignerBase):
    @staticmethod
    def container():
        return "quay.io/biocontainers/star:2.7.3a--0"

    @staticmethod
    def version():
        return "v2.7.1a"


StarAlignerLatest = StarAligner_2_7_1
