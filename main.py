from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_training import ModelTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME = "Model Training stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = ModelTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = ModelEvaluationTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e