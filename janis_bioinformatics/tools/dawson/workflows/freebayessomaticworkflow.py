from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix, VcfTabix

from janis_core import Array, Boolean, String, Int, Filename

from janis_bioinformatics.tools.dawson import CallSomaticFreeBayes_0_1
from janis_bioinformatics.tools.freebayes import FreeBayes_1_3

from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest
from janis_bioinformatics.tools.bcftools import BcfToolsNormLatest, BcfToolsSortLatest

from janis_bioinformatics.tools.vcflib import (
    VcfUniqLatest,
    VcfFixUpLatest,
    VcfUniqAllelesLatest,
    VcfAllelicPrimitivesLatest,
    VcfCombineLatest,
    VcfStreamSortLatest,
)


class FreeBayesSomaticWorkflow(BioinformaticsWorkflow):
    def id(self):
        return "FreeBayesSomaticWorkflow"

    def friendly_name(self):
        return "Freebayes somatic workflow"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 18)
        self.metadata.dateUpdated = date(2019, 10, 25)

        self.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = [
            "variants",
            "freebayes",
            "variant caller",
            "multi sample",
        ]
        self.metadata.documentation = """
        This workflow uses the capabilities of freebayes to output all variants independent of the
        diploid model which then in turn allows us to create a likelihood based difference between
        the normal sample and an arbitrary amount of samples.
        This allows a joint somatic genotyping of multiple samples of the same individual.
                """.strip()

    def constructor(self):

        self.input("bams", Array(BamBai))

        self.input("reference", FastaWithDict)
        self.input(
            "callRegions",
            Array(String, optional=True),
            default=[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "X",
                "Y",
                "MT",
            ],
        )

        self.input("normalSample", String)
        self.input("sampleNames", Array(String, optional=True))

        self.input("skipCov", Int(optional=True), default=500)

        self.step(
            "callVariants",
            FreeBayes_1_3(
                bams=self.bams,
                reference=self.reference,
                pooledDiscreteFlag=True,
                gtQuals=True,
                strictFlag=True,
                pooledContinousFlag=True,
                repoprtMaxGLFlag=True,
                noABPriorsFlag=True,
                maxNumOfAlleles=5,
                noPartObsFlag=True,
                region=self.callRegions,
                skipCov=self.skipCov,
                # things that are actually default, but janis does not recognize yet
                useDupFlag=False,
                minBaseQual=0,
                minSupQsum=0,
                minSupMQsum=0,
                minAltQSum=0,
                minCov=0,
            ),
            scatter="region",
        )
        # might actually rewrite this once everything works, to not combine the files here, but do
        # all of it scattered and then only combine the final output
        self.step("combineRegions", VcfCombineLatest(vcf=self.callVariants.out))

        self.step(
            "sortAll",
            VcfStreamSortLatest(vcf=self.combineRegions.out, inMemoryFlag=True),
        )

        self.step("compressAll", BGZipLatest(file=self.sortAll.out))
        self.step("indexAll", TabixLatest(file=self.compressAll.out))

        self.step(
            "callSomatic",
            CallSomaticFreeBayes_0_1(
                vcf=self.indexAll.out, normalSampleName=self.normalSample
            ),
        )

        # no need to compress this here if it leads to problems when we dont have an index for the allelic allelicPrimitves
        self.step(
            "normalizeSomatic1",
            BcfToolsNormLatest(vcf=self.callSomatic.out, reference=self.reference),
        )

        self.step("indexNorm1", TabixLatest(file=self.normalizeSomatic1))

        self.step(
            "allelicPrimitves",
            VcfAllelicPrimitivesLatest(vcf=self.indexNorm1.out, tagParsed="DECOMPOSED"),
        )

        self.step("fixSplitLines", VcfFixUpLatest(vcf=self.allelicPrimitves.out))

        self.step(
            "sortSomatic",
            VcfStreamSortLatest(vcf=self.fixSplitLines.out, inMemoryFlag=True),
        )

        self.step(
            "normalizeSomatic2",
            BcfToolsNormLatest(vcf=self.sortSomatic.out, reference=self.reference),
        )

        self.step("indexNorm2", TabixLatest(file=self.normalizeSomatic2))

        self.step("uniqueAlleles", VcfUniqAllelesLatest(vcf=self.indexNorm2.out))

        self.step(
            "sortFinal",
            VcfStreamSortLatest(vcf=self.uniqueAlleles.out, inMemoryFlag=True),
        )

        self.step("uniqVcf", VcfUniqLatest(vcf=self.sortFinal.out))

        self.step("compressFinal", BGZipLatest(file=self.uniqVcf.out))

        self.step("indexFinal", TabixLatest(file=self.compressFinal.out))

        self.output("out", source=self.indexFinal)


if __name__ == "__main__":

    wf = FreeBayesSomaticWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
