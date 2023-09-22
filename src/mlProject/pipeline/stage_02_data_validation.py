from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger


STAGE_NAME = "Data Validation"

class DataValidationTrainingPipeline:
    
    def __init__(self) -> None:
        pass
        
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
    
if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME} Stage")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.main()
        logger.info(f"{STAGE_NAME} Stage Completed!")
    except Exception as e:
        logger.error(e)
        raise e
    