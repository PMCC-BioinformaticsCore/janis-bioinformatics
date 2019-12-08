from janis_bioinformatics.tools.ucsf.cnvkit.base import CNVKitBase


class CNVKit_0_9_6(CNVKitBase):
    def container(self):
        return "etal/cnvkit:0.9.6"

    def version(self):
        return "0.9.6"


CNVKitLatest = CNVKit_0_9_6
