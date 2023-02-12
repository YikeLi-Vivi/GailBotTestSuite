from test_suite.src.test_module import test 

class TestOne(test):
    def __init__(self) -> None:
        super().__init__()
        self.name = "test one"