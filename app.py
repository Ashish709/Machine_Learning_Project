from flask import Flask, request
import sys
from housing.logger import logging
from housing.exception import HousingException


app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])

def index():
    try:
        raise Exception("We are testing Custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing Logging")
    return "Starting Machine Learning Project"


if __name__ == "__main__":
    app.run()