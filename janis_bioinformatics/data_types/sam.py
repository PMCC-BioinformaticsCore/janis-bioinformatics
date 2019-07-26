from janis_core import File


class Sam(File):
    def __init__(self, optional=False):
        super().__init__(optional=optional, extension=".sam")

    @staticmethod
    def name():
        return "SAM"

    def doc(self):
        return "Tab-delimited text file that contains sequence alignment data"
