"""
conftest.py
"""

import time
import datetime
import logging
import pytest
from _pytest.fixtures import FixtureRequest
from _pytest.nodes import Item
from _pytest.reports import TestReport
from _pytest.config.argparsing import Parser
from common_libs.board_comm import BoardComm

logger = logging.getlogger(__name__)

@pytest.fixture(scope="session", autouse=True)
def hardware_comm():
    """
    Method to initialize board communication at the beginning of session and closes at the end
    """
    logger.info("Starting communication session...")

    # get available hardware
    available_hardware = get_hardware()

    comm_obj = []
    for hardware in available_hardware:
        comm_obj = BoardComm()
        comm_obj.connect()

    yield comm_obj

    logger.info("Closing communication session...")
    for hardware in comm_obj:
        hardware.terminate_communication()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item):
    """
    Hook that gets called at setup, call, and teardown of each test.
    Code retrieves yield at the end of each test, and if the state is in 'call'
    and the test failed, it executes a function to grab logs from the test board
    args:
        item (pytest obj): the test item, used to gain test file path to
                        determine board to grab logs from
    """

    outcome: TestReport = yield
    result: TestReport = outcome.get_result()
    if result.when == "call" and result.failed:

        # collect logs and so on
        pass

def save_logs_to_file(test_name, logs):
    """
    Method to save hardware logging
    """
    log_file = f"logs/{test_name}.log"
    with open(log_file, "w") as f:
        f.write(str(logs))
    logger.info(f"Saved failure logs to {log_file}")

