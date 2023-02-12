from test_suite.src.test_module import test 
from test_suite.src.test_two import TestTwo
from test_suite.src.test_d_two import TestDependTwo

class TestDependThree(test):
    def __init__(self) -> None:
        super().__init__()
        self.name = "test depends on test two and test dd two"
        self.depend = TestTwo()
        self.depend2 = TestDependTwo()