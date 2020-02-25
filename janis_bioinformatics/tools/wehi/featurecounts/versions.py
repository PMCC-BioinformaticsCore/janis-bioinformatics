from janis_bioinformatics.tools.wehi.featurecounts.base import FeatureCountsBase
#1.6.4
class FeatureCounts_1_6_4(FeatureCountsBase):
    @staticmethod
    def container():
        return "quay.io/biocontainers/subread:1.6.4--h84994c4_1"
    
    @staticmethod
    def version():
        return "1.6.4"