from abc import ABC

from janis_core import ToolInput, String, Boolean, Directory
from janis_bioinformatics.tools.ensembl.vep.base import VepBase


class VepCacheBase(VepBase, ABC):
    def inputs(self):
        return [
            *super().inputs(),  # cache options
            ToolInput(
                "cache",
                Boolean(optional=True),
                prefix="--cache",
                doc="Enables use of the cache. Add --refseq or --merged to use the refseq or merged cache,",
            ),
            ToolInput(
                "cachePluginDir",
                Directory(optional=True),
                prefix="--dir",
                doc='Specify the base cache/plugin directory to use. Default = "$HOME/.vep/"',
            ),
            ToolInput(
                "cacheDir",
                Directory(optional=True),
                prefix="--dir_cache",
                doc='Specify the cache directory to use. Default = "$HOME/.vep/"',
            ),
            ToolInput(
                "pluginDir",
                Directory(optional=True),
                prefix="--dir_plugin",
                doc='Specify the plugin directory to use. Default = "$HOME/.vep/"',
            ),
            ToolInput(
                "offline",
                Boolean(optional=True),
                prefix="--offline",
                doc="Enable offline mode. No database connections will be made, and a cache file or GFF/GTF file is "
                "required for annotation. Add --refseq to use the refseq cache (if installed). ",
            ),
            ToolInput(
                "fasta",
                Fasta(optional=True),
                prefix="--fasta",
                doc="Specify a FASTA file or a directory containing FASTA files to use to look up reference sequence. "
                "The first time you run VEP, an index will be built which can take a few minutes. This is required "
                "if fetching HGVS annotations (--hgvs) or checking reference sequences (--check_ref) in offline "
                "mode (--offline), and optional with some performance increase in cache mode (--cache). "
                "See documentation for more details. ",
            ),
            ToolInput(
                "refseq",
                String(optional=True),
                prefix="--refseq",
                doc="Specify this option if you have installed the RefSeq cache in order for VEP to pick up the "
                "alternate cache directory. This cache contains transcript objects corresponding to RefSeq "
                "transcripts. Consequence output will be given relative to these transcripts in place of the "
                "default Ensembl transcripts (see documentation)	REFSEQ_MATCH, BAM_EDIT	--gencode_basic",
            ),
            ToolInput(
                "merged",
                String(optional=True),
                prefix="--merged",
                doc="Use the merged Ensembl and RefSeq cache. Consequences are flagged with the SOURCE of each "
                "transcript used.	REFSEQ_MATCH, BAM_EDIT, SOURCE	--refseq",
            ),
            ToolInput(
                "cacheVersion",
                String(optional=True),
                prefix="--cache_version",
                doc="Use a different cache version than the assumed default (the VEP version). This should be used with"
                " Ensembl Genomes caches since their version numbers do not match Ensembl versions. For example, "
                "the VEP/Ensembl version may be 88 and the Ensembl Genomes version 35. ",
            ),
            ToolInput(
                "showCacheInfo",
                String(optional=True),
                prefix="--show_cache_info",
                doc="Show source version information for selected cache and quit",
            ),
            ToolInput(
                "bufferSize",
                String(optional=True),
                prefix="--buffer_size",
                doc="[number] Sets the internal buffer size, corresponding to the number of variants that are read in "
                "to memory simultaneously. Set this lower to use less memory at the expense of longer run time, "
                "and higher to use more memory with a faster run time. Default = 5000",
            ),
        ]
