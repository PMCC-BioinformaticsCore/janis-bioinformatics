from .base import Gatk4ApplyBqsrBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4ApplyBqsr_4_0(Gatk_4_0_12, Gatk4ApplyBqsrBase):
    pass


class Gatk4ApplyBqsr_4_1_2(Gatk_4_1_2_0, Gatk4ApplyBqsrBase):
    pass


class Gatk4ApplyBqsr_4_1_3(Gatk_4_1_3_0, Gatk4ApplyBqsrBase):
    pass


class Gatk4ApplyBqsr_4_1_4(Gatk_4_1_4_0, Gatk4ApplyBqsrBase):
    pass


Gatk4ApplyBqsrLatest = Gatk4ApplyBqsr_4_1_3
