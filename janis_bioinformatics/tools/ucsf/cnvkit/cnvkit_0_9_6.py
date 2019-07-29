from janis_bioinformatics.tools.ucsf.cnvkit.base import CNVKitBase


class CNVKit_0_9_6(CNVKitBase):
    @staticmethod
    def container():
        return "etal/cnvkit:0.9.6"

    @staticmethod
    def version():
        return "0.9.6"


CNVKitLatest = CNVKit_0_9_6
