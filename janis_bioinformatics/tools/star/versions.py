from janis_bioinformatics.tools.star.base import StarAlignerBase


class StarAligner_2_7_1(StarAlignerBase):
    def container(self):
        return "quay.io/biocontainers/star:2.7.3a--0"

    def version(self):
        return "v2.7.1a"


StarAlignerLatest = StarAligner_2_7_1
