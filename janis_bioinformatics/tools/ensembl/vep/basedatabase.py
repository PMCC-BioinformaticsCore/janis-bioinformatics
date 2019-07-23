from abc import ABC

from janis_core import ToolInput, String, Boolean, Int
from janis_bioinformatics.tools.ensembl.vep.base import VepBase


class VepDatabaseBase(VepBase, ABC):
    def inputs(self):
        return [
            *super().inputs(),
            ToolInput(
                "database",
                Boolean(),
                default=True,
                prefix="--database",
                doc="Enable VEP to use local or remote databases.",
            ),
            ToolInput(
                "host",
                String(optional=True),
                prefix="--host",
                doc="[hostname] Manually define the database host to connect to. Users in the US may find connection "
                "and transfer speeds quicker using our East coast mirror, useastdb.ensembl.org. "
                'Default = "ensembldb.ensembl.org"',
            ),
            ToolInput(
                "user",
                String(optional=True),
                prefix="--user",
                doc='[username] Manually define the database username. Default = "anonymous"',
            ),
            ToolInput(
                "password",
                String(optional=True),
                prefix="--password",
                doc="[password] Manually define the database password.",
            ),
            ToolInput(
                "port",
                Int(optional=True),
                prefix="--port",
                doc="[number] Manually define the database port. Default = 5306",
            ),
            ToolInput(
                "genomes",
                String(optional=True),
                prefix="--genomes",
                doc="Override the default connection settings with those for the Ensembl Genomes public MySQL server. "
                "Required when using any of the Ensembl Genomes species.",
            ),
            ToolInput(
                "isMultispecies",
                Boolean(optional=True),
                prefix="--is_multispecies",
                doc="[0|1] Some of the Ensembl Genomes databases (mainly bacteria and protists) are composed of a "
                "collection of close species. It updates the database connection settings (i.e. the database name) "
                "if the value is set to 1. Default: 0",
            ),
            ToolInput(
                "lrg",
                Boolean(optional=True),
                prefix="--lrg",
                doc="Map input variants to LRG coordinates (or to chromosome coordinates if given in LRG coordinates), "
                "and provide consequences on both LRG and chromosomal transcripts.",
            ),
            ToolInput(
                "dbVersion",
                Int(optional=True),
                prefix="--db_version",
                doc="[number] Force VEP to connect to a specific version of the Ensembl databases. Not recommended as "
                "there may be conflicts between software and database versions.",
            ),
            ToolInput(
                "registry",
                String(optional=True),
                prefix="--registry",
                doc="[filename] Defining a registry file overwrites other connection settings and uses those found in "
                "the specified registry file to connect.",
            ),
        ]
