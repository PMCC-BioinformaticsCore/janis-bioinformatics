from janis_core import Double

from janis_bioinformatics.data_types import Bam, FastaWithIndexes
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.gatk4 import (
    Gatk4AddOrReplaceReadGroups_4_1_4,
    Gatk4MarkDuplicates_4_1_4,
    Gatk4SplitNCigarReads_4_1_4,
    Gatk4HaplotypeCaller_4_1_4,
    Gatk4ReorderSam_4_1_4,
)
from janis_bioinformatics.tools.gatk4.variantfiltration.versions import (
    Gatk4VariantFiltration_4_1_4,
)


class OncopipeVariantCaller(BioinformaticsWorkflow):
    def id(self) -> str:
        return "oncopipe_variantcaller"

    def friendly_name(self):
        return "Oncopipe: VariantCaller"

    def constructor(self):
        # variant_pipeline = segment {
        #     add_rg +
        #     mark_duplicates +
        #     reorder_bam +
        #     splitncigar +
        #     rnaseq_call_variants +
        #     filter_variants +
        #     + [annotate variants]
        # }

        self.input("bam", Bam)
        self.input("reference", FastaWithIndexes)
        self.input("sample_name", str)
        self.input("platform", str)

        self.step(
            "add_rg",
            Gatk4AddOrReplaceReadGroups_4_1_4(
                inp=self.bam,
                sort_order="coordinate",
                rgid=self.sample_name,
                rglb="lib1",
                rgpl=self.platform,
                rgpu="1",
                rgsm=self.sample_name,
                validation_stringency="LENIENT",
            ),
            doc="Add read group",
        )

        self.step(
            "mark_duplicates",
            Gatk4MarkDuplicates_4_1_4(
                bam=self.add_rg.out, validationStringency="SILENT"
            ),
            doc="Mark duplicates and create index",
        )

        self.step(
            "reorder_bam",
            Gatk4ReorderSam_4_1_4(
                reference=self.reference, inp=self.mark_duplicates.out,
            ),
        )

        # https://gatkforums.broadinstitute.org/gatk/discussion/10800/gatk4-how-to-reassign-star-mapping-quality-from-255-to-60-with-splitncigarreads
        # missing params from migration:
        #   -rf ReassignOneMappingQuality -> readFilter
        #   -RMQF 255
        #   -RMQT 60
        #   -U ALLOW_N_CIGAR_READS
        self.step(
            "splitncigar",
            Gatk4SplitNCigarReads_4_1_4(
                inp=self.reorder_bam.out,
                reference=self.reference,
                readFilter="ReassignOneMappingQuality",
            ),
            doc="split'n'trim and reassign mapping qualities",
        )

        self.step(
            "rnaseq_call_variants",
            Gatk4HaplotypeCaller_4_1_4(
                inputRead=self.splitncigar.out,
                reference=self.reference,
                dontUseSoftClippedBases=True,
                standardMinConfidenceThresholdForCalling=self.input(
                    "call_conf", Double
                ),
            ),
        )

        self.step(
            "filter_variants",
            Gatk4VariantFiltration_4_1_4(
                reference=self.reference,
                variant=self.rnaseq_call_variants.out,
                clusterWindowSize=35,
                clusterSize=3,
                filterName=['FS -filter "FS > 30.0"', 'QD -filter "QD < 2.0"'],
            ),
        )


if __name__ == "__main__":
    OncopipeVariantCaller().translate("wdl")
