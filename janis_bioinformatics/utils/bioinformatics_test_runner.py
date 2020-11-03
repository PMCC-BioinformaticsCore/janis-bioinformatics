import subprocess
from enum import Enum
from typing import Any

from janis_core.tool.test_suite_runner import ToolTestSuiteRunner
from janis_core.tool.test_classes import TTestCompared, TTestExpectedOutput
from janis_bioinformatics.data_types import Bam


class TBioinformaticsTestCompared(Enum):
    GenomicsStat = "genomics-stat"


class BioinformaticsToolTestSuiteRunner(ToolTestSuiteRunner):
    def _transform_value(
        self, test_logic: TTestExpectedOutput, output_value: Any, output_type: Any
    ) -> Any:
        if test_logic.compared == TBioinformaticsTestCompared.GenomicsStat:
            value = self.read_genomics_stat(
                output_value=output_value, output_type=output_type
            )
        else:
            return super()._transform_value(
                test_logic=test_logic,
                output_value=output_value,
                output_type=output_type,
            )

        return value

    def read_genomics_stat(self, output_value: Any, output_type: Any) -> str:
        if isinstance(output_type, Bam):
            command = ["samtools", "flagstat", output_value]
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )

            if result.stderr:
                raise Exception(result.stderr)

            value = result.stdout

        else:
            raise Exception(
                f"{TTestCompared.GenomicsStat} comparison type is not allowed for"
                f" output type {output_type}"
            )

        return value
