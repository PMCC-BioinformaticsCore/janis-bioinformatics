from .base import Gatk4ApplyBqsrBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_3_0 import Gatk_4_1_3_0
from ..gatk_latest import Gatk4Latest


class Gatk4ApplyBqsr_4_0(Gatk_4_0_12, Gatk4ApplyBqsrBase):
    pass


class Gatk4ApplyBqsr_4_1_3(Gatk_4_1_3_0, Gatk4ApplyBqsrBase):
    pass


Gatk4ApplyBqsrLatest = Gatk4ApplyBqsr_4_1_3
