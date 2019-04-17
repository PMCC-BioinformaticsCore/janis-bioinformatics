from abc import ABC
from datetime import datetime
from typing import List
from janis import ToolOutput, ToolInput, ToolMetadata, File, String, Boolean, Array, WildcardSelector, Directory, Int
from janis.types import CpuSelector
from janis.unix.data_types.zipfile import ZipFile
from janis_bioinformatics.data_types import Fastq

from janis_bioinformatics.tools import BioinformaticsTool


class FastQCBase(BioinformaticsTool, ABC):

    def friendly_name(self) -> str:
        return "FastQC"

    @staticmethod
    def tool():
        return "fastqc"

    @staticmethod
    def base_command():
        return "fastqc"

    def metadata(self):
        return ToolMetadata(
            creator="Simon Andrews",
            maintainer="Michael Franklin",
            date_created=datetime(2019,3,25), date_updated=datetime(2019,3,25),
            institution="Babraham Bioinformatics",
            doi=None, citation=None, keywords=["fastqc", "quality", "qa"],
            documentation_url="http://www.bioinformatics.babraham.ac.uk/projects/fastqc/",
            documentation=
            "FastQC is a program designed to spot potential problems in high througput sequencing datasets. "
            "It runs a set of analyses on one or more raw sequence files in fastq or bam format and produces a "
            "report which summarises the results.\n"
            "FastQC will highlight any areas where this library looks unusual and where you should take a closer look. "
            "The program is not tied to any specific type of sequencing technique and can be used to look at libraries "
            "coming from a large number of different experiment types "
            "(Genomic Sequencing, ChIP-Seq, RNA-Seq, BS-Seq etc etc).")

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("reads", Fastq(), position=5),
            *self.additional_inputs
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("out", Array(ZipFile()), glob=WildcardSelector(wildcard="*.zip"))
        ]

    additional_inputs = [
            ToolInput("outdir", String(optional=True), default=".", prefix="--outdir",
                      doc="(-o) Create all output files in the specified output directory. Please note that this "
                          "directory must exist as the program will not create it.  If this option is not set then "
                          "the output file for each sequence file is created in the same directory as the sequence "
                          "file which was processed."),
            ToolInput("casava", Boolean(optional=True), prefix="--casava",
                      doc="Files come from raw casava output. Files in the same sample group "
                          "(differing only by the group number) will be analysed as a set rather than individually. "
                          "Sequences with the filter flag set in the header will be excluded from the analysis. "
                          "Files must have the same names given to them by casava (including being gzipped and "
                          "ending with .gz) otherwise they won't be grouped together correctly."),
            ToolInput("nano", Boolean(optional=True), prefix="--nano",
                      doc="Files come from naopore sequences and are in fast5 format. In this mode you can pass in "
                          "directories to process and the program will take in all fast5 files within those "
                          "directories and produce a single output file from the sequences found in all files."),
            ToolInput("nofilter", Boolean(optional=True), prefix="--nofilter",
                      doc="If running with --casava then don't remove read flagged by casava as poor quality when "
                          "performing the QC analysis."),
            ToolInput("extract", Boolean(optional=True), prefix="--extract",
                      doc="If set then the zipped output file will be uncompressed in the same directory after it has "
                          "been created.  By default this option will be set if fastqc is run in non-interactive mode."),
            ToolInput("java", String(optional=True), prefix="--java",
                      doc="(-j) Provides the full path to the java binary you want to use to launch fastqc. "
                          "If not supplied then java is assumed to be in your path."),
            ToolInput("noextract", Boolean(optional=True), default=True, prefix="--noextract",
                      doc="Do not uncompress the output file after creating it.  You should set this option if you do"
                          "not wish to uncompress the output when running in non-interactive mode. "),
            ToolInput("nogroup", Boolean(optional=True), prefix="--nogroup",
                      doc="Disable grouping of bases for reads >50bp. "
                          "All reports will show data for every base in the read. "
                          "WARNING: Using this option will cause fastqc to crash and burn if you use it on "
                          "really long reads, and your plots may end up a ridiculous size. You have been warned! "),
            ToolInput("format", String(optional=True), prefix="--format",
                      doc="(-f) Bypasses the normal sequence file format detection and forces the program to use the "
                          "specified format.  Valid formats are bam,sam,bam_mapped,sam_mapped and fastq "),
            ToolInput("threads", Int(optional=True), prefix="--threads", default=CpuSelector(),
                      doc="(-t) Specifies the number of files which can be processed simultaneously. "
                          "Each thread will be allocated 250MB of memory so you shouldn't run more threads than your "
                          "available memory will cope with, and not more than 6 threads on a 32 bit machine"),
            ToolInput("contaminants", File(optional=True), prefix="--contaminants",
                      doc="(-c) Specifies a non-default file which contains the list of contaminants to screen "
                          "overrepresented sequences against. The file must contain sets of named contaminants in "
                          "the form name[tab]sequence.  Lines prefixed with a hash will be ignored."),
            ToolInput("adapters", File(optional=True), prefix="--adapters",
                      doc="(-a) Specifies a non-default file which contains the list of adapter sequences which will "
                          "be explicity searched against the library. The file must contain sets of named adapters in "
                          "the form name[tab]sequence.  Lines prefixed with a hash will be ignored. "),
            ToolInput("limits", File(optional=True), prefix="--limits",
                      doc="(-l) Specifies a non-default file which contains a set of criteria which will be used to "
                          "determine the warn/error limits for the various modules.  This file can also be used to "
                          "selectively  remove some modules from the output all together. "
                          "The format needs to mirror the default limits.txt file found in the Configuration folder."),
            ToolInput("kmers", Int(optional=True), prefix="--kmers",
                      doc="(-k) Specifies the length of Kmer to look for in the Kmer content module. "
                          "Specified Kmer length must be between 2 and 10. Default length is 7 if not specified. "),
            ToolInput("quiet", Boolean(optional=True), prefix="--quiet",
                      doc="(-q) Supress all progress messages on stdout and only report errors."),
            ToolInput("dir", Directory(optional=True), prefix="--dir",
                      doc="(-d) Selects a directory to be used for temporary files written when generating report images."
                          "Defaults to system temp directory if not specified."),
        ]
# from typing import Dict
#
# from janis import Step, ToolInput, ToolOutput
#
#
# class FastQCFactory(StepFactory):
#     @classmethod
#     def type(cls):
#         return 'fastqc'
#
#     @classmethod
#     def label(cls):
#         return 'fastqc'
#
#     @classmethod
#     def description(cls):
#         return cls.label()
#
#     @classmethod
#     def schema(cls):
#         return {
#             'schema': {},
#             'nullable': True
#         }
#
#     @classmethod
#     def build(cls, meta, debug=False):
#         return FastQCStep(meta, debug=debug)
#
#
#
# class FastQCStep(Step):
#
#     def translate(self):
#         pass
#
#     def input_labels(self) -> [str]:
#         return [FastQCStep.input1]
#
#     def requires(self) -> Dict[str, ToolInput]:
#         inp = self.get_input1()
#         return { inp.tag: inp }
#
#     def provides(self) -> Dict[str, ToolOutput]:
#         outp = self.get_output()
#         return { outp.tag: outp }
#
#     # def provides(self):
#     #     return [
#     #         {
#     #             Step.STR_ID: "reports",
#     #             Step.STR_TYPE: "Text"
#     #         }
#     #     ]
#     #
#     # def requires(self) -> List[StepInput]:
#     #     """
#     #     Only returns a SequenceReadArchivePaired object, with tag: input
#     #     :return:
#     #     """
#     #     return [self.get_input1()]
#
#     def get_input1(self) -> ToolInput:
#         return ToolInput("input", "SequenceReadArchivePaired")
#
#     def get_output(self) -> ToolOutput:
#         return ToolOutput("reports", "Text")
