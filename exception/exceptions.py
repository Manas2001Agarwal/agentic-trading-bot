import sys

class TradingBotException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename   
        
    def __str__(self):
        return f"error occured in python script: {self.file_name}, line number: {self.lineno} error message: {str(self.error_message)}"   
    
    
if __name__ == "__main__":
    try:
        x = 1/0 
        print("this line will not be printed")
    except Exception as e:
        raise TradingBotException(e,sys)