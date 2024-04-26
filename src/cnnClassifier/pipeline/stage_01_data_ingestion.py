import os
import sys

# Get the absolute path of the project directory (root of the kidney project)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Append the project directory to the system path
sys.path.append(project_root)

# Now you can import the desired class from configuration.py
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\nnx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
