from src.textSummerizer.config.configuration import configurationManager
from src.textSummerizer.components.model_trainer import ModelTrainerconfig
from src.textSummerizer.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config_manager = configurationManager()
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()