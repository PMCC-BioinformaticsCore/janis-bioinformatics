import ruamel.yaml

from janis_bioinformatics.tools.illumina.strelka_2_9_9 import Strelka_2_9_9
from janis_bioinformatics.tools.illumina.strelka_2_9_10 import Strelka_2_9_10

from janis_bioinformatics.tools.illumina.strelkagermline.base import StrelkaGermlineBase


class StrelkaGermline_2_9_9(StrelkaGermlineBase, Strelka_2_9_9):
    pass


class StrelkaGermline_2_9_10(StrelkaGermlineBase, Strelka_2_9_10):
    pass


StrelkaGermlineLatest = StrelkaGermline_2_9_10
