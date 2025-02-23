


from src.semiconductor.config.configuration import ConfigurationManager
from src.semiconductor.components.dataValidation import DataValidation




STAGE_NAME = 'Data_validation_stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()