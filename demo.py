from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
import os


def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        
        
        # pipepline = Pipeline()
        # pipepline.start()
        
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
        
        
    
    except Exception as e:
        logging.error(f"{e}")
        print(e)    
    

if __name__ == "__main__":
    main()