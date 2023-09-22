from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
            

if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME} !")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed !")
    except Exception as e:
        logger.error(e)
        raise e
