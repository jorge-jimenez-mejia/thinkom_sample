"""
Created Aug 7th
@author: Jorge Jimenez
"""

import time

class BoardComm():
    """
        Generic Method for board communication
    """

    def __init__(self):

        # initialization code here
        pass

    def rx_thread(self) -> None:
        """
        Method to continuously receive
        """

        while True:
            time.sleep(5)

    def tx_thread(self) -> None:
        """
        Method to continuously transmit
        """

        while True:
            time.sleep(5)

    def connect(self) -> bool:
        """
        Method to run threads

        Returns:
            bool: result
        """

        print("run threads here using multiprocess")

        return True
    
    def terminate_communication(self) -> bool:
        """
        Method to close threads

        Returns:
            bool: result
        """

        return True

    def send(self, msg: str) -> bool:
        """
        Method to send data to hardware

        Args:
            msg (str): command

        Returns:
            bool: send status
        """

        # send message here

        return True

    def read(self) -> str:
        """
        Method to read data from hardware

        Returns:
            str: response
        """

        # read data here

        return True