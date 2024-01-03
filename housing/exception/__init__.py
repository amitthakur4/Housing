import os
import sys
from housing.logger import logging

class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail : sys) -> None:
        super().__init__(error_message)
        self.error_message= HousingException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail= error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)-> str:
        _,_, exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name  = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured through script : [{file_name}] at line: [{line_number}] with error msg :[{error_message}]"
        return error_message

    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
    

if __name__ == "__main__":
    try:
        9/0
    except Exception as e:
        logging.info("error encountered")
        HousingException.get_detailed_error_message(e, sys)

