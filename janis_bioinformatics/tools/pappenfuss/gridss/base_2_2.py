from datetime import date
from typing import List

from janis_core import (
    ToolOutput,
    ToolInput,
    Filename,
    File,
    String,
    Float,
    Int,
    Boolean,
    Array,
    InputSelector,
)

from janis_bioinformatics.data_types import Bam, FastaWithDict, Bed, Vcf
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class GridssBase_2_2(BioinformaticsTool):
    @staticmethod
    def tool() -> str:
        return "gridss"

    @staticmethod
    def tool_provider():
        return "Papenfuss Labs"

    def friendly_name(self) -> str:
        return "Gridss"

    @staticmethod
    def base_command():
        return [
            "java",
            "-ea",
            "-XX:+UnlockExperimentalVMOptions",
            "-XX:+UseCGroupMemoryLimitForHeap",
            "-XX:MaxRAMFraction=1",
            "-XshowSettings:vm",
            "-Dsamjdk.create_index=true",
            "-Dsamjdk.use_async_io_read_samtools=true",
            "-Dsamjdk.use_async_io_write_samtools=true",
            "-Dsamjdk.use_async_io_write_tribble=true",
            "-Dgridss.gridss.output_to_temp_file=true",
            "-Dsamjdk.buffer_size=4194304",
            "-cp",
            # insert the following line within the VersionedTool:
            # /data/gridss/gridss-$version-gridss-jar-with-dependencies.jar gridss.CallVariants
        ]

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf"),
                prefix="OUTPUT=",
                separate_value_from_prefix=False,
                doc="(O=) VCF structural variation calls. Required.",
            ),
            ToolInput(
                "reference",
                FastaWithDict(),
                prefix="REFERENCE_SEQUENCE=",
                separate_value_from_prefix=False,
            ),
            ToolInput(
                "bams",
                Array(Bam()),
                prefix="INPUT=",
                separate_value_from_prefix=False,
                doc="(I=File Coordinate-sorted input BAM file. Default value: null. "
                "This option may be specified 0 or more times.",
            ),
            ToolInput(
                "assemblyFilename",
                Filename(suffix=".assembled", extension=".bam"),
                prefix="ASSEMBLY=",
                separate_value_from_prefix=False,
                doc="Breakend assemblies which have undergone split read identification Required.",
            ),
            ToolInput(
                "inputLabel",
                String(optional=True),
                prefix="INPUT_LABEL=",
                separate_value_from_prefix=False,
                doc="Input label. Variant calling evidence breakdowns are reported for each label. Default "
                "labels correspond to INPUT filenames. When specifying labels, labels must be provided for "
                "all input files. Default value: null. This option may be specified 0 or more times.",
            ),
            ToolInput(
                "inputMaxFragmentSize",
                Int(optional=True),
                prefix="INPUT_MAX_FRAGMENT_SIZE=",
                separate_value_from_prefix=False,
                doc="Per input maximum concordant fragment size. Default value: null. "
                "This option may be specified 0 or more times.",
            ),
            ToolInput(
                "inputMinFragmentSize",
                Int(optional=True),
                prefix="INPUT_MIN_FRAGMENT_SIZE=",
                separate_value_from_prefix=False,
                doc="Per input minimum concordant fragment size. Default value: null. "
                "This option may be specified 0 or more times.",
            ),
            ToolInput(
                "readPairConcordantPercent",
                Float(optional=True),
                prefix="READ_PAIR_CONCORDANT_PERCENT=",
                separate_value_from_prefix=False,
                doc="Percent of read pairs considered concorant (0.0-1.0). If this is unset, the SAM proper "
                "pair flag is used to determine whether a read is discordantly aligned. Explicit fragment "
                "size specification overrides this setting. Default value: 0.995. "
                "This option can be set to 'null' to clear the default value.",
            ),
            ToolInput(
                "blacklist",
                Bed(),
                prefix="BLACKLIST=",
                separate_value_from_prefix=False,
                doc="(BL=File) BED blacklist of regions to ignore. Assembly of regions such as high-coverage "
                "centromeric repeats is slow, and if such regions are to be filtered in downstream "
                "analysis anyway, blacklisting those region will improve runtime performance. "
                "For human WGS, the ENCODE DAC blacklist is recommended. Default value: null.",
            ),
            ToolInput(
                "configurationFile",
                File(optional=True),
                prefix="CONFIGURATION_FILE=",
                separate_value_from_prefix=False,
                doc="(C=File) gridss configuration file containing overrides Default value: null.",
            ),
            ToolInput(
                "workerThreads",
                Int(optional=True),
                prefix="WORKER_THREADS=",
                separate_value_from_prefix=False,
                doc="(THREADS=Integer  Number of worker threads to spawn. Defaults to number of cores available. "
                "Note that I/O threads are not included in this worker thread count so CPU usage can be "
                "higher than the number of worker thread. Default value: 6. "
                "This option can be set to 'null' to clear the default value.",
            ),
            ToolInput(
                "workingDir",
                String(optional=True),
                prefix="WORKING_DIR=",
                default=".",
                separate_value_from_prefix=False,
                doc="Directory to place intermediate results directories. Default location is the same "
                "directory as the associated input or output file. Default value: null.",
            ),
            ToolInput(
                "ignoreDuplicates",
                Boolean(optional=True),
                prefix="IGNORE_DUPLICATES=",
                separate_value_from_prefix=False,
                doc="Ignore reads marked as duplicates. Default value: true. This option can be set to 'null' "
                "to clear the default value. Possible values: {true, false}",
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("vcf", Vcf(), glob=InputSelector("outputFilename")),
            ToolOutput("assembly", Bam(), glob=InputSelector("assemblyFilename")),
        ]

    def metadata(self):

        self._metadata.maintainer = "Michael Franklin"
        self._metadata.dateCreated = date(2019, 6, 19)
        self._metadata.dateUpdated = date(2019, 7, 3)
        self._metadata.documentationUrl = (
            "https://github.com/PapenfussLab/gridss/wiki/GRIDSS-Documentation"
        )
        self._metadata.doi = "10.1101/gr.222109.117"
        self._metadata.citation = "Daniel L. Cameron, Jan Schröder, Jocelyn Sietsma Penington, Hongdo Do, " \
                                  "Ramyar Molania, Alexander Dobrovic, Terence P. Speed and Anthony T. Papenfuss. " \
                                  "GRIDSS: sensitive and specific genomic rearrangement detection using positional " \
                                  "de Bruijn graph assembly. Genome Research, 2017 doi: 10.1101/gr.222109.117"
        self._metadata.documentation = """\
GRIDSS: the Genomic Rearrangement IDentification Software Suite

GRIDSS is a module software suite containing tools useful for the detection of genomic rearrangements. 
GRIDSS includes a genome-wide break-end assembler, as well as a structural variation caller for Illumina 
sequencing data. GRIDSS calls variants based on alignment-guided positional de Bruijn graph genome-wide 
break-end assembly, split read, and read pair evidence.

GRIDSS makes extensive use of the standard tags defined by SAM specifications. Due to the modular design, 
any step (such as split read identification) can be replaced by another implementation that also outputs 
using the standard tags. It is hoped that GRIDSS can serve as an exemplar modular structural variant 
pipeline designed for interoperability with other tools.

If you have any trouble running GRIDSS, please raise an issue using the Issues tab above. Based on feedback 
from users, a user guide will be produced outlining common workflows, pitfalls, and use cases.
"""
