from datetime import datetime
from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Array,
    Boolean,
    String,
    Int,
    InputSelector,
    Filename,
    ToolMetadata,
    Float,
)
from janis_core import Directory, CpuSelector, MemorySelector
from janis_unix import Csv


class CellRangerMkfastqBase(CommandTool):
    def friendly_name(self) -> str:
        return "CellRanger mkfastq"

    @staticmethod
    def tool_provider():
        return "CellRanger"

    @staticmethod
    def tool() -> str:
        return "CellRangerMkfastq"

    @staticmethod
    def base_command():
        return ["cellranger", "mkfastq"]

    def inputs(self):
        return [
            ToolInput(
                tag="run",
                input_type=Directory(),
                prefix="--run=",
                separate_value_from_prefix=False,
                doc="Path of Illumina BCL run folder.",
            ),
            ToolInput(
                tag="id",
                input_type=String(optional=True),
                prefix="--id=",
                separate_value_from_prefix=False,
                doc="Name of the folder created by mkfastq. If not supplied, will default to the name of the flowcell referred to by the --run argument.",
            ),
            ToolInput(
                tag="outputFoldername",
                input_type=Filename(),
                prefix="--output-dir=",
                separate_value_from_prefix=False,
                doc="Same as in bcl2fastq. Folder where FASTQs, reports and stats will be generated.",
            ),
            ToolInput(
                tag="csv",
                input_type=Csv(optional=True),
                prefix="--csv=",
                separate_value_from_prefix=False,
                doc="Apparently the same as `sampleSheet`. The sample sheet can either be a simple CSV with lane, sample and index columns, or an Illumina Experiment Manager-compatible sample sheet.  Sample sheet indexes can refer to 10x sample index set names (e.g., SI-GA-A12).",
            ),
            ToolInput(
                tag="sampleSheet",
                input_type=File(optional=True),
                prefix="--sample-sheet=",
                separate_value_from_prefix=False,
                doc="(--samplesheet= | --csv=) Path to the sample sheet. The sample sheet can either be a simple CSV with lane, sample and index columns, or an Illumina Experiment Manager-compatible sample sheet.  Sample sheet indexes can refer to 10x sample index set names (e.g., SI-GA-A12).",
            ),
            ToolInput(
                tag="ignoreDualIndex",
                input_type=Boolean(optional=True),
                prefix="--ignore-dual-index",
                separate_value_from_prefix=True,
                doc="On a dual-indexed flowcell, ignore the second sample index, if the second sample index was not used for the 10x sample.",
            ),
            ToolInput(
                tag="qc",
                input_type=Boolean(optional=True),
                prefix="--qc",
                separate_value_from_prefix=True,
                doc="Calculate both sequencing and 10x-specific metrics, including per-sample barcode matching rate. Will not be performed unless this flag is specified.",
            ),
            ToolInput(
                tag="lanes",
                input_type=Array(String, optional=True),
                prefix="--lanes=",
                separate_value_from_prefix=False,
                separator=",",
                doc="Comma-delimited series of lanes to demultiplex. Shortcut for the --tiles argument.",
            ),
            ToolInput(
                tag="useBasesMask",
                input_type=String(optional=True),
                prefix="--use-bases-mask=",
                separate_value_from_prefix=False,
                doc="Same as bcl2fastq; override the read lengths as specified in RunInfo.xml. See Illumina bcl2fastq documentation for more information.",
            ),
            ToolInput(
                tag="deleteUndetermined",
                input_type=Boolean(optional=True),
                prefix="--delete-undetermined",
                separate_value_from_prefix=True,
                doc="Delete the Undetermined FASTQ files left by bcl2fastq.  Useful if your sample sheet is only expected to match a subset of the flowcell.",
            ),
            ToolInput(
                tag="project",
                input_type=String(optional=True),
                prefix="--project=",
                separate_value_from_prefix=False,
                doc="Custom project name, to override the samplesheet or to use in conjunction with the --csv argument.",
            ),
            # mfranklin: These are only supported in cluster modes which I've disabled
            # ToolInput(
            #     tag="jobmode",
            #     input_type=String(optional=True),
            #     prefix="--jobmode=",
            #     separate_value_from_prefix=False,
            #     doc="Job manager to use. Valid options: local (default), sge, lsf, or a .template file",
            # ),
            # ToolInput(
            #     tag="mempercore",
            #     input_type=String(optional=True),
            #     prefix="--mempercore=",
            #     separate_value_from_prefix=False,
            #     doc="Set max GB each job may use at one time. Only applies in cluster jobmodes.",
            # ),
            # ToolInput(
            #     tag="maxjobs",
            #     input_type=String(optional=True),
            #     prefix="--maxjobs=",
            #     separate_value_from_prefix=False,
            #     doc="Set max jobs submitted to cluster at one time. Only applies in cluster jobmodes.",
            # ),
            # ToolInput(
            #     tag="jobinterval",
            #     input_type=String(optional=True),
            #     prefix="--jobinterval=",
            #     separate_value_from_prefix=False,
            #     doc="Set delay between submitting jobs to cluster, in ms. Only applies in cluster jobmodes.",
            # ),
            # ToolInput(
            #     tag="overrides",
            #     input_type=File(optional=True),
            #     prefix="--overrides=",
            #     separate_value_from_prefix=False,
            #     doc="The path to a JSON file that specifies stage-level overrides for cores and memory.  Finer-grained than --localcores, --mempercore and --localmem. Consult the 10x support website for an example override file.",
            # ),
            ToolInput(
                tag="localcores",
                input_type=Int(optional=True),
                default=CpuSelector(),
                prefix="--localcores=",
                separate_value_from_prefix=False,
                doc="Set max cores the pipeline may request at one time. Only applies when --jobmode=local.",
            ),
            ToolInput(
                tag="localmem",
                input_type=Float(optional=True),
                default=MemorySelector(),
                prefix="--localmem=",
                separate_value_from_prefix=False,
                doc="Set max GB the pipeline may request at one time. Only applies when --jobmode=local.",
            ),
            # ToolInput(
            #     tag="uiport",
            #     input_type=Boolean(optional=True),
            #     prefix="--uiport=",
            #     separate_value_from_prefix=False,
            #     doc="Serve web UI at http://localhost:PORT",
            # ),
            # ToolInput(
            #     tag="disableUi",
            #     input_type=String(optional=True),
            #     prefix="--disable-ui",
            #     separate_value_from_prefix=True,
            #     doc="Do not serve the UI.",
            # ),
            # ToolInput(
            #     tag="noexit",
            #     input_type=String(optional=True),
            #     prefix="--noexit",
            #     separate_value_from_prefix=True,
            #     doc="Keep web UI running after pipestance completes or fails.",
            # ),
            ToolInput(
                tag="nopreflight",
                input_type=Boolean(optional=True),
                prefix="--nopreflight",
                separate_value_from_prefix=True,
                doc="Skip preflight checks.",
            ),
            # ToolInput(
            #     tag="help",
            #     input_type=String(optional=True),
            #     prefix="-h",
            #     separate_value_from_prefix=True,
            #     doc="Show this message.",
            # ),
            # ToolInput(
            #     tag="version",
            #     input_type=String(optional=True),
            #     prefix="--version",
            #     separate_value_from_prefix=True,
            #     doc="Show version.",
            # ),
        ]

    def outputs(self):
        return [ToolOutput("out", Directory, glob=InputSelector("outputFoldername"))]

    def metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime.fromisoformat("2019-10-24T12:29:47.687842"),
            dateUpdated=datetime.fromisoformat("2019-10-24T12:29:47.687856"),
            documentation="""\
/opt/cellranger-3.0.2/cellranger-cs/3.0.2/bin
cellranger mkfastq (3.0.2)
Copyright (c) 2019 10x Genomics, Inc.  All rights reserved.
-------------------------------------------------------------------------------
Run Illumina demultiplexer on sample sheets that contain 10x-specific sample 
index sets, and generate 10x-specific quality metrics after the demultiplex.  
Any bcl2fastq argument will work (except a few that are set by the pipeline 
to ensure proper trimming and sample indexing). The FASTQ output generated 
will be the same as when running bcl2fastq directly.
These bcl2fastq arguments are overridden by this pipeline:
    --fastq-cluster-count
    --minimum-trimmed-read-length
    --mask-short-adapter-reads
Usage:
    cellranger mkfastq --run=PATH [options]
    cellranger mkfastq -h | --help | --version
""",
        )
