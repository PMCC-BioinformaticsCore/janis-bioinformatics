from .base import WhisperIndexBase
from ..versions import Whisper_2_0


class WhisperIndex_2_0(Whisper_2_0, WhisperIndexBase):
    pass


WhisperIndexLatest = Whisper_2_0
