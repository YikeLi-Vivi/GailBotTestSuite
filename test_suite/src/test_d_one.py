
from test_suite.src.test_module import test
from test_suite.src.test_one import TestOne

class TestDependOne(test):
    def __init__(self) -> None:
        super().__init__()
        self.name = "test depends on test one"
        self.depend = TestOne()
        
