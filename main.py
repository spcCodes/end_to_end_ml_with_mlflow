from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

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
