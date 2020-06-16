from janis_bioinformatics.tools.illumina.strelka_2_9_9 import Strelka_2_9_9
from janis_bioinformatics.tools.illumina.strelka_2_9_10 import Strelka_2_9_10
from janis_bioinformatics.tools.illumina.strelkasomatic.base import StrelkaSomaticBase
from janis_bioinformatics.tools.illumina.strelkasomatic.base_cram import (
    StrelkaSomaticCramBase,
)


class StrelkaSomatic_2_9_9(Strelka_2_9_9, StrelkaSomaticBase):
    pass


class StrelkaSomatic_2_9_10(Strelka_2_9_10, StrelkaSomaticBase):
    pass


class StrelkaSomaticCram_2_9_9(Strelka_2_9_9, StrelkaSomaticCramBase):
    pass


class StrelkaSomaticCram_2_9_10(Strelka_2_9_10, StrelkaSomaticCramBase):
    pass


StrelkaSomaticLatest = StrelkaSomatic_2_9_10
