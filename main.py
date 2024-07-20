
import sys
from src.semiconductor import logger, CustomException
from src.semiconductor.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipeline
from src.semiconductor.pipeline.stage_02_dataValidation import DataValidationTrainingPipeline
from src.semiconductor.pipeline.stage_03_dataTransformation import DataTransformationPipeline



STAGE_NAME = 'Data Ingestion Stage'


try:
    logger.info(f'--------------------stage {STAGE_NAME} started --------------------------')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'----------------------stage {STAGE_NAME} completed ---------------------')
except Exception as e:
    raise CustomException(e, sys)



STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f'-----------------stage {STAGE_NAME} started-----------------------')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'-----------------stage {STAGE_NAME} completed-----------------------')
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f'-----------stage {STAGE_NAME} started------------------------')
    datatransformation = DataTransformationPipeline()
    datatransformation.main()
except Exception as e:
    raise CustomException(e, sys)