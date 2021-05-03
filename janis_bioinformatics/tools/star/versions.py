from janis_bioinformatics.tools.star.alignreads import StarAlignReadsBase
from janis_bioinformatics.tools.star.generateindexesbase import StarGenerateIndexesBase
from janis_bioinformatics.tools.star.liftover import StarLiftOverBase
from janis_bioinformatics.tools.star.inputalignmentsfrombam import (
    StarInputAlignmentsFromBamBase,
)


class Star_2_5_3:
    def container(self):
        return "quay.io/biocontainers/star:2.5.3a--0"

    def version(self):
        return "v2.5.3a"


class Star_2_7_1:
    def container(self):
        return "quay.io/biocontainers/star:2.7.1a--0"

    def version(self):
        return "v2.7.1a"


class Star_2_7_3:
    def container(self):
        return "quay.io/biocontainers/star:2.7.3a--0"

    def version(self):
        return "v2.7.3a"


class Star_2_7_5:
    def container(self):
        return "quay.io/biocontainers/star:2.7.5c--0"

    def version(self):
        return "v2.7.5c"


class Star_2_7_7:
    def container(self):
        return "quay.io/biocontainers/star:2.7.7a--0"

    def version(self):
        return "v2.7.7a"


# StarAlignReads
class StarAlignReads_2_5_3(Star_2_5_3, StarAlignReadsBase):
    pass


class StarAlignReads_2_7_1(Star_2_7_1, StarAlignReadsBase):
    pass


class StarAlignReads_2_7_3(Star_2_7_3, StarAlignReadsBase):
    pass


class StarAlignReads_2_7_5(Star_2_7_5, StarAlignReadsBase):
    pass


class StarAlignReads_2_7_7(Star_2_7_7, StarAlignReadsBase):
    pass


# StarGenerateIndexes
class StarGenerateIndexes_2_5_3(Star_2_5_3, StarGenerateIndexesBase):
    pass


class StarGenerateIndexes_2_7_1(Star_2_7_1, StarGenerateIndexesBase):
    pass


class StarGenerateIndexes_2_7_3(Star_2_7_3, StarGenerateIndexesBase):
    pass


class StarGenerateIndexes_2_7_5(Star_2_7_5, StarGenerateIndexesBase):
    pass


class StarGenerateIndexes_2_7_7(Star_2_7_7, StarGenerateIndexesBase):
    pass


# StarLiftOver
class StarLiftOver_2_5_3(Star_2_5_3, StarLiftOverBase):
    pass


class StarLiftOver_2_7_1(Star_2_7_1, StarLiftOverBase):
    pass


class StarLiftOver_2_7_3(Star_2_7_3, StarLiftOverBase):
    pass


class StarLiftOver_2_7_5(Star_2_7_5, StarLiftOverBase):
    pass


class StarLiftOver_2_7_7(Star_2_7_7, StarLiftOverBase):
    pass


# StarInputAlignmentsFromBam
class StarInputAlignmentsFromBam_2_5_3(Star_2_5_3, StarInputAlignmentsFromBamBase):
    pass


class StarInputAlignmentsFromBam_2_7_1(Star_2_7_1, StarInputAlignmentsFromBamBase):
    pass


class StarInputAlignmentsFromBam_2_7_3(Star_2_7_3, StarInputAlignmentsFromBamBase):
    pass


class StarInputAlignmentsFromBam_2_7_5(Star_2_7_5, StarInputAlignmentsFromBamBase):
    pass


class StarInputAlignmentsFromBam_2_7_7(Star_2_7_7, StarInputAlignmentsFromBamBase):
    pass


StarAlignReadsLatest = StarAlignReads_2_7_7
StarGenerateIndexesLatest = StarGenerateIndexes_2_7_7
StarLiftOverLatest = StarLiftOver_2_7_7
StarInputAlignmentsFromBam_2_7_7
