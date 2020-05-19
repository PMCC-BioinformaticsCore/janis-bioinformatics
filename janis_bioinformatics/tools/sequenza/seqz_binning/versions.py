from ..sequenza_2_2_0_9000 import Sequenza_2_2_0_9000
from ..sequenza_3_0_0 import Sequenza_3_0_0
from .base import SeqzBinningBase


class SequenzaBinning_2_2_0_9000(Sequenza_2_2_0_9000, SeqzBinningBase):
    pass


class SequenzaBinning_3_0_0(Sequenza_3_0_0, SeqzBinningBase):
    pass


SequenzaBinningLatest = SequenzaBinning_3_0_0
