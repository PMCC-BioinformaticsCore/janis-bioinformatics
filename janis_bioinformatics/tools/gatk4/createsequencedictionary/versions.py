from .base import Gatk4CreateSequenceDictionaryBase
from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4CreateSequenceDictionary_4_1_2(
    Gatk_4_1_2_0, Gatk4CreateSequenceDictionaryBase
):
    pass


class Gatk4CreateSequenceDictionary_4_1_3(
    Gatk_4_1_3_0, Gatk4CreateSequenceDictionaryBase
):
    pass


class Gatk4CreateSequenceDictionary_4_1_4(
    Gatk_4_1_4_0, Gatk4CreateSequenceDictionaryBase
):
    pass


Gatk4CreateSequenceDictionaryLatest = Gatk4CreateSequenceDictionary_4_1_3

if __name__ == "__main__":
    print(Gatk4CreateSequenceDictionaryBase().help())
