from test_suite.src.test_module import test 
from test_suite.src.test_two import TestTwo
from test_suite.src.test_one import TestOne

class TestDependTwo(test):
    def __init__(self) -> None:
        super().__init__()
        self.name = "test depend on test two and test one"
        self.depend = TestTwo()
        self.depend2 = TestOne()