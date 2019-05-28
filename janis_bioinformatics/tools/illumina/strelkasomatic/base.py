from datetime import datetime
from janis import CommandTool, ToolInput, ToolOutput, File, Boolean, String, Int, InputSelector, Filename, ToolMetadata


class StrelkaSomaticBaseBase(CommandTool):

    def friendly_name(self) -> str:
        return "Strelka - Somatic Workflow"

    @staticmethod
    def tool_provider():
        return "Illumina"

    @staticmethod
    def tool() -> str:
        return "StrelkaSomaticBase"

    @staticmethod
    def base_command():
        return "configureStrelkaSomaticWorkflow.py"

    def inputs(self):
        return [

        ]

    def outputs(self):
        return [

        ]

    def metadata(self):
        return ToolMetadata(dateCreated=datetime(2019,5,27,15,7,45), dateUpdated=datetime(2019,5,27,15,7,45),
                            documentation="""Usage: configureStrelkaSomaticWorkflow.py [options]
Version: 2.9.10
This script configures Strelka somatic small variant calling.
You must specify an alignment file (BAM or CRAM) for each sample of a matched tumor-normal pair.
Configuration will produce a workflow run script which can execute the workflow on a single node or through
sge and resume any interrupted execution.""")