from janis_bioinformatics.tools.illumina.strelka_2_9_9 import Strelka_2_9_9
from janis_bioinformatics.tools.illumina.strelka_2_9_10 import Strelka_2_9_10

from janis_bioinformatics.tools.illumina.strelkasomatic.base import StrelkaSomaticBase


class StrelkaSomatic_2_9_9(Strelka_2_9_9, StrelkaSomaticBase):
    pass


class StrelkaSomatic_2_9_10(Strelka_2_9_10, StrelkaSomaticBase):
    pass


StrelkaSomaticLatest = StrelkaSomatic_2_9_10
