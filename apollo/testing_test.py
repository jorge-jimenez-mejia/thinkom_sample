
import pytest
from common_libs.board_comm import BoardComm
from common_libs.custom_exceptions import TestFailure

def sample_test(hardware_comm: list[BoardComm]):

    result: bool = True

    try:
        for comm in hardware_comm:
            comm.send("hello world")
            response = comm.read()
            if response != "OK":
                raise TestFailure(f"message did not respond with OK: {response}")

    except TestFailure:
        result = False
    finally:
        # any test tear down
        pass

    if not result:
        pytest.fail()