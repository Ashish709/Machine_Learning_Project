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


# if __name__ == "__main__":
#     logging.info("Logging has started")