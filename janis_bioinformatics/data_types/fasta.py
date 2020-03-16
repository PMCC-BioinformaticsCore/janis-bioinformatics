from typing import List
from janis_core import File, DataType


class Fasta(File):
    def __init__(self, optional=False):
        super().__init__(optional, extension=".fasta")

    @staticmethod
    def name():
        return "Fasta"

    def can_receive_from(self, other, source_has_default=False):

        if isinstance(other, Fasta):
            if other.optional and not self.optional:
                return False
        elif not super().can_receive_from(other, source_has_default):
            return False

        if not self.secondary_files():
            return True

        return set(self.secondary_files()).issubset(set(other.secondary_files() or []))


class FastaFai(Fasta):
    @staticmethod
    def name():
        return "FastaFai"

    @staticmethod
    def secondary_files():
        return [".fai"]


class FastaBwa(Fasta):
    @staticmethod
    def name():
        return "FastaFai"

    @staticmethod
    def secondary_files():
        return [".amb", ".ann", ".bwt", ".pac", ".sa"]


class FastaDict(FastaFai):
    @staticmethod
    def name():
        return "FastDict"

    @staticmethod
    def secondary_files():
        return [*FastaFai().secondary_files(), "^.dict"]


class FastaWithIndexes(Fasta):
    @staticmethod
    def name():
        return "FastaWithIndexes"

    @staticmethod
    def secondary_files():
        return [*FastaBwa.secondary_files(), *FastaDict.secondary_files()]


FastaWithDict = FastaWithIndexes

if __name__ == "__main__":
    bwa, fai, wdict = FastaBwa(), FastaFai(), FastaWithDict()
    print(fai.can_receive_from(wdict))
    print(bwa.can_receive_from(wdict))
    print(wdict.can_receive_from(bwa))
    print(wdict.can_receive_from(wdict))
