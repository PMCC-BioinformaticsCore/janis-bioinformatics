from .freebayessomaticworkflow import FreeBayesSomaticWorkflow


class FreeBayesSomaticWorkflowCram(FreeBayesSomaticWorkflow):
    def id(self):
        return "FreeBayesSomaticWorkflowCram"

    def friendly_name(self):
        return "Freebayes somatic workflow (CRAM)"

    # this is a way to get the tool without spaghetti code in bam and cram format
    def getFreebayesTool(self):
        from janis_bioinformatics.tools.freebayes.versions import (
            FreeBayesCram_1_3 as freebayes,
        )

        return freebayes

    def getFreebayesInputType(self):
        from janis_bioinformatics.data_types import CramCrai

        return CramCrai


if __name__ == "__main__":

    wf = FreeBayesSomaticWorkflowCram()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
