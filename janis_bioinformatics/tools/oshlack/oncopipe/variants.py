from janis_core import Double, WorkflowMetadata, StringFormatter, File

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

    # def friendly_name(self):
    #     return "Oncopipe: VariantCaller"

    def bind_metadata(self):
        return WorkflowMetadata(
            version="v0.1.0", contributors=["Michael Franklin", "Jiaan Yu"]
        )

    def constructor(self):
        # variant_pipeline = segment {
        #     add_rg +
        #     mark_duplicates +
        #     reorder_bam +
        #     splitncigar +
        #     rnaseq_call_variants +
        #     filter_variants
        # }

        self.input("bam", Bam)
        self.input("reference", FastaWithIndexes)
        self.input("sequence_dictionary", File)
        self.input("sample_name", str)
        self.input("platform", str)
        self.input("call_conf", Double, default=20.0)

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
                create_index=True,
            ),
            doc="Add read group",
        )

        self.step(
            "mark_duplicates",
            Gatk4MarkDuplicates_4_1_4(
                bam=[self.add_rg.out], validationStringency="SILENT", createIndex=True
            ),
            doc="Mark duplicates and create index",
        )

        self.step(
            "reorder_bam",
            Gatk4ReorderSam_4_1_4(
                reference=self.reference,
                inp=self.mark_duplicates.out,
                sequence_dictionary=self.sequence_dictionary,
                create_index=True,
            ),
        )

        # https://github.com/bcbio/bcbio-nextgen/issues/2163
        # missing params from migration:
        #   -rf ReassignOneMappingQuality -> readFilter
        #   -RMQF 255
        #   -RMQT 60
        #   -U ALLOW_N_CIGAR_READS
        # https://gatk.broadinstitute.org/hc/en-us/articles/360036432252-SplitNCigarReads
        # --skip-mapping-quality-transform -skip-mq-transform set to False by default (skip the 255 -> 60 MQ read transform)
        self.step(
            "splitncigar",
            Gatk4SplitNCigarReads_4_1_4(
                inp=[self.reorder_bam.out], reference=self.reference,
            ),
            doc="split'n'trim and reassign mapping qualities",
        )

        self.step(
            "rnaseq_call_variants",
            Gatk4HaplotypeCaller_4_1_4(
                inputRead=self.splitncigar.out,
                reference=self.reference,
                dontUseSoftClippedBases=True,
                standardMinConfidenceThresholdForCalling=self.call_conf,
            ),
        )

        self.step(
            "filter_variants",
            Gatk4VariantFiltration_4_1_4(
                reference=self.reference,
                variant=self.rnaseq_call_variants.out,
                clusterWindowSize=35,
                clusterSize=3,
                filterName=["FS", "QD"],
                filterExpression=["FS > 30.0", "QD < 2.0"],
            ),
        )

        self.output(
            "out_HAP_vcf",
            source=self.rnaseq_call_variants.out,
            output_name=StringFormatter(
                "{sample_name}_HAP", sample_name=self.sample_name
            ),
        )
        self.output(
            "out_HAP_filter_vcf",
            source=self.filter_variants.out,
            output_name=StringFormatter(
                "{sample_name}_HAP.filtered", sample_name=self.sample_name
            ),
        )


if __name__ == "__main__":
    OncopipeVariantCaller().translate("wdl")
