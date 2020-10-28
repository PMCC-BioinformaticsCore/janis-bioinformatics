import os
import operator
from .base import SamToolsViewBase
from ..samtoolstoolbase import SamToolsToolBase
from ..samtools_1_7 import SamTools_1_7
from ..samtools_1_9 import SamTools_1_9

from janis_core.tool.tool import TTestCompared, TTestExpectedOutput, TTestCase


class SamToolsView_1_7(SamTools_1_7, SamToolsViewBase):
    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "sam": os.path.join(SamToolsToolBase.test_data_path(), "small.bam"),
                },
                output=[
                    TTestExpectedOutput(
                        tag="out",
                        compared=TTestCompared.FileMd5,
                        operator=operator.eq,
                        expected_value="4dd0783b97f4dde4745df4557096a095"
                    ),
                ]
            )
        ]


class SamToolsView_1_9(SamTools_1_9, SamToolsViewBase):
    pass


SamToolsViewLatest = SamToolsView_1_9
