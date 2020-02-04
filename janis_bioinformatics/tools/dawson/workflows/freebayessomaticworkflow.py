from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import (
    FastaWithDict,
    BamBai,
    BedTabix,
    VcfTabix,
    CramCrai,
)

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

        self.input("bams", Array(CramCrai))

        self.input("reference", FastaWithDict)
        self.input(
            "callRegions",
            Array(String, optional=True),
            default=[
                "chr1:1-50000000",
                "chr1:50000000-100000000",
                "chr1:100000000-150000000",
                "chr1:150000000-200000000",
                "chr1:200000000-248956422",
                "chr2:1-50000000",
                "chr2:50000000-100000000",
                "chr2:100000000-150000000",
                "chr2:150000000-200000000",
                "chr2:200000000-242193529",
                "chr3:1-50000000",
                "chr3:50000000-100000000",
                "chr3:100000000-150000000",
                "chr3:150000000-198295559",
                "chr4:1-50000000",
                "chr4:50000000-100000000",
                "chr4:100000000-150000000",
                "chr4:150000000-190214555",
                "chr5:1-50000000",
                "chr5:50000000-100000000",
                "chr5:100000000-150000000",
                "chr5:150000000-181538259",
                "chr6:1-50000000",
                "chr6:50000000-100000000",
                "chr6:100000000-150000000",
                "chr6:150000000-170805979",
                "chr7:1-50000000",
                "chr7:50000000-100000000",
                "chr7:100000000-150000000",
                "chr7:150000000-159345973",
                "chr8:1-50000000",
                "chr8:50000000-100000000",
                "chr8:100000000-145138636",
                "chr9:1-50000000",
                "chr9:50000000-100000000",
                "chr9:100000000-138394717",
                "chr10:1-50000000",
                "chr10:50000000-100000000",
                "chr10:100000000-133797422",
                "chr11:1-50000000",
                "chr11:50000000-100000000",
                "chr11:100000000-135086622",
                "chr12:1-50000000",
                "chr12:50000000-100000000",
                "chr12:100000000-133275309",
                "chr13:1-50000000",
                "chr13:50000000-100000000",
                "chr13:100000000-114364328",
                "chr14:1-50000000",
                "chr14:50000000-100000000",
                "chr14:100000000-107043718",
                "chr15:1-50000000",
                "chr15:50000000-100000000",
                "chr15:100000000-101991189",
                "chr16:1-50000000",
                "chr16:50000000-90338345",
                "chr17:1-50000000",
                "chr17:50000000-83257441",
                "chr18:1-50000000",
                "chr18:50000000-80373285",
                "chr19:1-50000000",
                "chr19:50000000-58617616",
                "chr20:1-50000000",
                "chr20:50000000-64444167",
                "chr21:1-46709983",
                "chr22:1-50000000",
                "chr22:50000000-50818468",
                "chrX:1-50000000",
                "chrX:50000000-100000000",
                "chrX:100000000-150000000",
                "chrX:150000000-156040895",
            ],
        )

        self.input("normalSample", String)
        self.input("sampleNames", Array(String, optional=True))

        # for the moment this is a bit wonky, because you need to specify something which is
        # affected by the amount of bams that you specify (bam coverage just gets summed up at this
        # location)
        # so the formula at the moment would be nBams * coverage = skipCov
        # which means for 8 bams with an average coverage of 160 you would probably want
        # 8 * 400 = 1600 to be on the save side
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
                reportMaxGLFlag=True,
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
        # self.step("combineRegions", VcfCombineLatest(vcf=self.callVariants.out))

        #

        # self.step("compressAll", BGZipLatest(file=self.sortAll.out))
        # self.step("indexAll", TabixLatest(file=self.compressAll.out))

        self.step(
            "callSomatic",
            CallSomaticFreeBayes_0_1(
                vcf=self.callVariants.out, normalSampleName=self.normalSample
            ),
            # added for parallel
            scatter="vcf",
        )

        self.step("combineRegions", VcfCombineLatest(vcf=self.callSomatic.out))

        # should not be necessary here, but just to be save
        self.step(
            "sortSomatic1",
            VcfStreamSortLatest(vcf=self.combineRegions.out, inMemoryFlag=True),
        )

        # no need to compress this here if it leads to problems when we dont have an index for the allelic allelicPrimitves
        self.step(
            "normalizeSomatic1",
            BcfToolsNormLatest(
                vcf=self.sortSomatic1.out,
                reference=self.reference,
                outputType="v",
                outputFilename="normalised.vcf",
            ),
        )

        self.step(
            "allelicPrimitves",
            VcfAllelicPrimitivesLatest(
                vcf=self.normalizeSomatic1.out,
                tagParsed="DECOMPOSED",
                keepGenoFlag=True,
            ),
        )

        self.step("fixSplitLines", VcfFixUpLatest(vcf=self.allelicPrimitves.out))

        self.step(
            "sortSomatic2",
            VcfStreamSortLatest(vcf=self.fixSplitLines.out, inMemoryFlag=True),
        )

        self.step(
            "normalizeSomatic2",
            BcfToolsNormLatest(
                vcf=self.sortSomatic2.out,
                reference=self.reference,
                outputType="v",
                outputFilename="normalised.vcf",
            ),
        )

        self.step("uniqueAlleles", VcfUniqAllelesLatest(vcf=self.normalizeSomatic2.out))

        self.step(
            "sortFinal",
            VcfStreamSortLatest(vcf=self.uniqueAlleles.out, inMemoryFlag=True),
        )

        self.step("uniqVcf", VcfUniqLatest(vcf=self.sortFinal.out))

        self.step("compressFinal", BGZipLatest(file=self.uniqVcf.out))

        self.step("indexFinal", TabixLatest(file=self.compressFinal.out))

        self.output("somaticOutVcf", source=self.indexFinal)
        self.output(
            "variantsOutVcf", source=self.callVariants, output_folder=self.callRegions
        )


if __name__ == "__main__":

    wf = FreeBayesSomaticWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
