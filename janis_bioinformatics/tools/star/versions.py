from janis_bioinformatics.tools.star.alignreads import StarAlignReadsBase
from janis_bioinformatics.tools.star.generateindexesbase import StarGenerateIndexesBase
from janis_bioinformatics.tools.star.liftover import StarLiftOverBase
from janis_bioinformatics.tools.star.inputalignmentsfrombam import (
    StarInputAlignmentsFromBamBase,
)


class Star_2_7_1:
    @staticmethod
    def container():
        return "quay.io/biocontainers/star:2.7.3a--0"

    @staticmethod
    def version():
        return "v2.7.1a"


class StarAlignReads(Star_2_7_1, StarAlignReadsBase):
    pass


class StarGenerateIndexes(Star_2_7_1, StarGenerateIndexesBase):
    pass


class StarLiftOver(Star_2_7_1, StarLiftOverBase):
    pass


class StarInputAlignmentsFromBam(Star_2_7_1, StarInputAlignmentsFromBamBase):
    pass
