
import traceback

class TestFailure(Exception):
    """
    Custom exception to raise when failing a test
    """

    def __init__(self, arg = ""):
        print(arg)
        traceback.print_stack(limit=5)
        self.arg = arg