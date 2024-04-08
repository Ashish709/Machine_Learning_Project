import logging
from datetime import datetime
import os

LOG_DIR = "housing_logs" # loggin directiry name

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}" # cuurent time stamp

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)  # Creating a Logging files path

logging.basicConfig(
    filemode='w',
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)
import logging
from datetime import datetime
import os
import pandas as pd
from housing.constants import get_current_time_stamp 
LOG_DIR="logs"

def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME=get_log_file_name()

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)



logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)

def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]


# if __name__ == "__main__":
#     logging.info("Logging has started")
