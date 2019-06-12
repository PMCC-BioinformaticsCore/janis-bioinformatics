from janis_bioinformatics.tools.illumina.strelka_2_9_9 import Strelka_2_9_9
from janis_bioinformatics.tools.illumina.strelka_2_9_10 import Strelka_2_9_10

from janis_bioinformatics.tools.illumina.strelkagermline.base import StrelkaGermlineBase


class StrelkaGermline_2_9_9(Strelka_2_9_9, StrelkaGermlineBase):
    pass


class StrelkaGermline_2_9_10(Strelka_2_9_10, StrelkaGermlineBase):
    pass


StrelkaGermlineLatest = StrelkaGermline_2_9_10
