# output uncompressed vcf
from .vardictgermline import (
    VarDictGermline_1_5_6,
    VarDictGermline_1_5_7,
    VarDictGermline_1_5_8,
    VarDictGermline_1_6_0,
    VarDictGermline_1_7_0,
)
from .vardictsomatic import (
    VarDictSomatic_1_5_6,
    VarDictSomatic_1_5_8,
    VarDictSomatic_1_6_0,
    VarDictSomatic_1_7_0,
)

# output compressed vcf
from .vardictgermline_compressed import VarDictGermlineCompressed_1_6_0
from .vardictsomatic_compressed import VarDictSomaticCompressed_1_6_0


VarDictGermlineLatest = VarDictGermline_1_6_0
VarDictSomaticLatest = VarDictSomatic_1_6_0
