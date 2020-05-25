from janis_core import File, DataType

class KallistoIdx(File):
    def __init__(self, optional=False):
        super().__init__(optional, extension=".kidx")

    @staticmethod
    def name():
        return "KallistoIdx"

    def can_receive_from(self, other, source_has_default=False):
        return False

