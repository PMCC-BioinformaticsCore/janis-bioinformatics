from typing import Any, List
from janis_core import File

class WhisperIdx(File):
    def __init__(self, optional=False):
        super().__init__(optional)

    @staticmethod
    def name():
        return "WhisperIdx"

    @staticmethod
    def secondary_files():
        return [
            ".whisper_idx.lut_long_dir",
            ".whisper_idx.lut_long_rc",
            ".whisper_idx.lut_short_dir",
            ".whisper_idx.lut_short_rc",
            ".whisper_idx.ref_seq_desc",
            ".whisper_idx.ref_seq_dir_pck",
            ".whisper_idx.ref_seq_rc_pck",
            ".whisper_idx.sa_dir",
            ".whisper_idx.sa_rc"
        ]

