from src.textSummerizer.logger import logger
from src.textSummerizer.pipeline.stage_2_data_transformation import DataTransformationPipeline
from src.textSummerizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline
from textSummerizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 