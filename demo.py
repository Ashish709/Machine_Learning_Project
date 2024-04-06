from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging

def main():
    try:
        pipepline = Pipeline()
        pipepline.run_pipeline()
    
    except Exception as e:
        logging.error(f"{e}")
        print(e)    
    

if __name__ == "__main__":
    main()