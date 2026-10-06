import os
import urllib.request as request
import zipfile
from src.textSummerizer.logging import logger
from src.textSummerizer.entity import DataIngestionConfig


class DataIngestionConfig:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"Downloaded file: {filename} with headers: {headers}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")
    
    def unzip_data(self):
        if not os.path.exists(self.config.unzip_dir):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Unzipped data to {self.config.unzip_dir}")
        else:
            logger.info(f"Data already unzipped at {self.config.unzip_dir}")    