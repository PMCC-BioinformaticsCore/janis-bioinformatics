from janis_bioinformatics.tools.dawson.utils.typeconversion import (
    cast_input_bams_to_crams,
)

from .base_1_3 import FreeBayesBase_1_3


class FreeBayesCramBase_1_3(FreeBayesBase_1_3):
    def inputs(self):
        # we want every input which is a bam in the original to be a cram now
        return cast_input_bams_to_crams(super().inputs())
