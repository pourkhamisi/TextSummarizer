from src.textSummerizer.config.configuration import configurationManager
from src.textSummerizer.components.data_ingestion import DataIngestionConfig
from src.textSummerizer.logging import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):

        config_manager = configurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestionConfig(config=data_ingestion_config)
        data_ingestion.download_data()  
        data_ingestion.unzip_data()