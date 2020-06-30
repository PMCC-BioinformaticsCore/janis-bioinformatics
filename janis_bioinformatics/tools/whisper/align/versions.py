from .base import WhisperAlignBase
from ..versions import Whisper_2_0


class WhisperAlign_2_0(Whisper_2_0, WhisperAlignBase):
    pass


WhisperAlignLatest = WhisperAlign_2_0
