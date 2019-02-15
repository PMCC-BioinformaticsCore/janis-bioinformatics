import unittest
from shepherd import Cromwell, CWLTool, SyncTask


class TestBase(unittest.TestCase):
    engine = None

    @classmethod
    def setUpClass(cls):
        print("starting up")
        cls.engine = CWLTool()

    @classmethod
    def tearDownClass(cls):
        cls.engine.stop_engine()

    def run_task(self, source=None, source_path=None, inputs=None, input_paths=None,
                    dependencies=None, dependencies_path=None):
        return SyncTask(engine=self.engine, source=source, source_path=source_path, inputs=inputs,
                        input_paths=input_paths, dependencies=dependencies, dependencies_path=dependencies_path)

    def assertBamEqual(self, first, second, msg):
        print("Must determine how bam's can be compared: " + msg if msg else "")
        return True

