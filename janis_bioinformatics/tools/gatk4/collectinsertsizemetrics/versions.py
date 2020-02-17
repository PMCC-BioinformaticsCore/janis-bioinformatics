from .base import Gatk4CollectInsertSizeMetricsBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4CollectInsertSizeMetrics_4_0(Gatk_4_0_12, Gatk4CollectInsertSizeMetricsBase):
    pass


class Gatk4CollectInsertSizeMetrics_4_1_2(Gatk_4_1_2_0, Gatk4CollectInsertSizeMetricsBase):
    pass


class Gatk4CollectInsertSizeMetrics_4_1_3(Gatk_4_1_3_0, Gatk4CollectInsertSizeMetricsBase):
    pass


class Gatk4CollectInsertSizeMetrics_4_1_4(Gatk_4_1_4_0, Gatk4CollectInsertSizeMetricsBase):
    pass


Gatk4CollectInsertSizeMetricsLatest = Gatk4CollectInsertSizeMetrics_4_1_3
