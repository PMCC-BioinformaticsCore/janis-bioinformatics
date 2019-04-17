import os

class TestResources:

    def __init__(self, resources=None):
        if resources is None:
            print(os.environ["SHEPHERD_RESOURCE_DIR"])
