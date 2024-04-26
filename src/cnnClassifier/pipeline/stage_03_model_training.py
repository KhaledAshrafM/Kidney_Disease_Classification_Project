import os
import sys

# Get the absolute path of the project directory (root of the kidney project)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Append the project directory to the system path
sys.path.append(project_root)


from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_training import Training
from src.cnnClassifier import logger


STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == '__main__':
    try:
        logger.info(f"******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e