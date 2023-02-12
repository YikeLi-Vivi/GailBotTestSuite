from test_suite.src.test_module import test 

class TestTwo(test):
    def __init__(self) -> None:
        super().__init__()
        self.name = "test two"