
import traceback

class FailTest(Exception):
    """
    Custom exception to raise when failing a test
    """

    def __init__(self, arg = ""):
        print(arg)
        traceback.print_stack(limit=3)
        self.arg = arg
