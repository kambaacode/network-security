import sys
from networksecurity.logging import logger

class NetworkSecuriyException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_, exec_tb = error_details.exc_info() # exec_tb => exception traceback (Exception_type, Exception_value, Exception_traceback)
        self.line_number = exec_tb.tb_lineno
        self.file_name = exec_tb.tb_frame.f_code.co_filename

    def __str__(self): # tells what to print when you try to print an object of type NetworkSecuriyException
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.line_number, str(self.error_message)
        ) 
