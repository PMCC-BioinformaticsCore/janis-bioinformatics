from ..sequenza_2_2_0_9000 import Sequenza_2_2_0_9000
from ..sequenza_3_0_0 import Sequenza_3_0_0
from .base import SeqzBam2SeqBase


class SequenzaBam2Seqz_2_2_0_9000(Sequenza_2_2_0_9000, SeqzBam2SeqBase):
    pass


class SequenzaBam2Seqz_3_0_0(Sequenza_3_0_0, SeqzBam2SeqBase):
    pass


SequenzaBam2SeqzLatest = SequenzaBam2Seqz_3_0_0
