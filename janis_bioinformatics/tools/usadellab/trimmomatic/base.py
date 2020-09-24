from datetime import datetime
from datetime import datetime
from typing import List, Optional, Union
from janis_core import (
    ToolInput,
    ToolArgument,
    Int,
    String,
    Boolean,
    Filename,
    ToolOutput,
    Array,
    ToolMetadata,
)

from janis_bioinformatics.tools import BioinformaticsTool


class TrimmomaticBase(BioinformaticsTool):
    def tool_provider(self):
        return "Usadel Lab"

    def base_command(self) -> Optional[Union[str, List[str]]]:
        return "trimmomatic"

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "steps",
                Array(String),
                position=100,
                doc="""\
ILLUMINACLIP: Cut adapter and other illumina-specific sequences from the read.
SLIDINGWINDOW: Performs a sliding window trimming approach. It starts
scanning at the 5" end and clips the read once the average quality within the window
falls below a threshold.
MAXINFO: An adaptive quality trimmer which balances read length and error rate to
maximise the value of each read
LEADING: Cut bases off the start of a read, if below a threshold quality
TRAILING: Cut bases off the end of a read, if below a threshold quality
CROP: Cut the read to a specified length by removing bases from the end
HEADCROP: Cut the specified number of bases from the start of the read
MINLEN: Drop the read if it is below a specified length
AVGQUAL: Drop the read if the average quality is below the specified level
TOPHRED33: Convert quality scores to Phred-33
TOPHRED64: Convert quality scores to Phred-64
""",
            ),
            ToolInput("sampleName", String, doc="Used to name the output"),
            ToolInput("threads", Int(optional=True), prefix="-threads", position=2),
            ToolInput(
                "phred33",
                Boolean(optional=True),
                prefix="-phred33",
                position=3,
                doc="Use phred + 33 quality score. If no quality encoding is specified, "
                "it will be determined automatically",
            ),
            ToolInput(
                "phred64",
                Boolean(optional=True),
                prefix="-phred64",
                position=3,
                doc="Use phred + 64 quality score. If no quality encoding is specified, "
                "it will be determined automatically",
            ),
            ToolInput(
                "trimLogFilename",
                Filename(prefix="trimlog", extension=".log"),
                prefix="-trimlog",
                position=4,
                doc="""\
Specifying a trimlog file creates a log of all read trimmings, indicating the following details:

    - the read name
    - the surviving sequence length
    - the location of the first surviving base, aka. the amount trimmed from the start
    - the location of the last surviving base in the original read
    - the amount trimmed from the end""",
            ),
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["illusional"],
            dateCreated=datetime(2020, 5, 25),
            dateUpdated=datetime(2020, 5, 25),
            citation="Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina Sequence Data. Bioinformatics, btu170.",
            doi="10.1093/bioinformatics/btu170",
            documentationUrl="http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf",
            documentation="""\
Trimmomatic is a fast, multithreaded command line tool that can be used to trim and crop
Illumina (FASTQ) data as well as to remove adapters. These adapters can pose a real problem
depending on the library preparation and downstream application.

There are two major modes of the program: Paired end mode and Single end mode. The
paired end mode will maintain correspondence of read pairs and also use the additional
information contained in paired reads to better find adapter or PCR primer fragments
introduced by the library preparation process.

Trimmomatic works with FASTQ files (using phred + 33 or phred + 64 quality scores,
depending on the Illumina pipeline used). Files compressed using either "gzip" or "bzip2" are
supported, and are identified by use of ".gz" or ".bz2" file extensions. """,
        )
