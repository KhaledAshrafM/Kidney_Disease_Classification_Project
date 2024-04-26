import os
import sys

# Get the absolute path of the project directory (root of the kidney project)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Append the project directory to the system path
sys.path.append(project_root)

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation_mlflow import Evaluation
from src.cnnClassifier import logger



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info("****************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n 'nx========")
    except Exception as e:
        logger.exception(e)
        raise e