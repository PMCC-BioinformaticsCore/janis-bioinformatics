from janis_bioinformatics.data_types import Vcf, VcfTabix
from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import (
    ToolOutput,
    ToolInput,
    Boolean,
    Stdout,
    String,
)


class UncompressVcf(BioinformaticsTool):
    def tool(self):
        return "UncompressVcf"

    def friendly_name(self):
        return "UncompressVcf"

    def tool_provider(self):
        return "unix"

    def base_command(self):
        return "gzip"

    def container(self):
        return "ubuntu:latest"

    def version(self):
        return "v1.0.0"

    def inputs(self):
        return [ToolInput("vcfTabix", VcfTabix(), position=1), *self.additional_inputs]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf),)]

    additional_inputs = [
        ToolInput(
            "stdout",
            Boolean(optional=True),
            prefix="-c",
            doc="write on standard output, keep original files unchanged",
        ),
        ToolInput("decompress", Boolean(optional=True), prefix="-d", doc="decompress"),
        ToolInput(
            "force",
            Boolean(optional=True),
            prefix="-f",
            doc="force overwrite of output file and compress links",
        ),
        ToolInput(
            "keep",
            Boolean(optional=True),
            prefix="-k",
            doc="keep (don't delete) input files",
        ),
        ToolInput(
            "list",
            Boolean(optional=True),
            prefix="-l",
            doc="list compressed file contents",
        ),
        ToolInput(
            "noName",
            Boolean(optional=True),
            prefix="-n",
            doc="do not save or restore the original name and time stamp",
        ),
        ToolInput(
            "name",
            Boolean(optional=True),
            prefix="-N",
            doc="save or restore the original name and time stamp",
        ),
        ToolInput(
            "quiet", Boolean(optional=True), prefix="-q", doc="suppress all warnings"
        ),
        ToolInput(
            "recursive",
            Boolean(optional=True),
            prefix="-r",
            doc="operate recursively on directories",
        ),
        ToolInput(
            "suffix",
            String(optional=True),
            prefix="-s",
            doc="use suffix SUF on compressed files",
        ),
        ToolInput(
            "test",
            Boolean(optional=True),
            prefix="-t",
            doc="test compressed file integrity",
        ),
        ToolInput("fast", Boolean(optional=True), prefix="-1", doc="compress faster"),
        ToolInput("best", Boolean(optional=True), prefix="-9", doc="compress better"),
        ToolInput(
            "rsyncable",
            Boolean(optional=True),
            prefix="--rsyncable",
            doc="Make rsync-friendly archive",
        ),
    ]
