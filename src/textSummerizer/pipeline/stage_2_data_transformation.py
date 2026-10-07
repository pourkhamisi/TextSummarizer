from src.textSummerizer.config.configuration import configurationManager
from src.textSummerizer.components.data_transformation import DataTransformation
from src.textSummerizer.logging import logger
from textSummerizer import config
from textSummerizer.components import data_transformation
from textSummerizer.entity import DataIngestionConfig

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        config = configurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert_dataset_to_features()


