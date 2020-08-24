from janis_bioinformatics.tools.star.alignreads import StarAlignReadsBase
from janis_bioinformatics.tools.star.generateindexesbase import StarGenerateIndexesBase
from janis_bioinformatics.tools.star.liftover import StarLiftOverBase
from janis_bioinformatics.tools.star.inputalignmentsfrombam import (
    StarInputAlignmentsFromBamBase,
)


class Star_2_7_1:
    def container(self):
        return "quay.io/biocontainers/star:2.7.3a--0"

    def version(self):
        return "v2.7.1a"


class StarAlignReads_2_7_1(Star_2_7_1, StarAlignReadsBase):
    pass


class StarGenerateIndexes_2_7_1(Star_2_7_1, StarGenerateIndexesBase):
    pass


class StarLiftOver_2_7_1(Star_2_7_1, StarLiftOverBase):
    pass


class StarInputAlignmentsFromBam_2_7_1(Star_2_7_1, StarInputAlignmentsFromBamBase):
    pass
