from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_model_base import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


# STAGE_NAME = "Data Ingestion stage"
# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
#         data_ingestion = DataIngestionTrainingPipeline()
#         data_ingestion.main()
#         logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\nnx=======x")
#     except Exception as e:
#         logger.exception(e)
#         raise e
    

STAGE_NAME = "Prepare base model"
try:
    logger.info(f"******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation"
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