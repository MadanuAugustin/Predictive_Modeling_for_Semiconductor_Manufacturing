import os
import sys
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from src.semiconductor import logger, CustomException
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from src.semiconductor.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        
        self.config = config




    def data_split(self):
        try:

            logger.info(f'-----------Entered data_split method---------------')
        
            data = pd.read_csv(self.config.local_data_file)

            train, test = train_test_split(data, test_size=0.2, random_state=42)

            train.to_csv(os.path.join(self.config.train_path, 'train.csv'), index = False, header = True)
        
            test.to_csv(os.path.join(self.config.test_path, 'test.csv'), index = False, header = True)

            logger.info(f'----------------saved train & test data in csv format------------------')

            logger.info(f'------------The shape of the train data is {train.shape}')

            logger.info(f'--------------The shape of the test data is {test.shape}')

            logger.info(f'------------completed data splitting----------------------')

        except Exception as e:
            raise CustomException(e, sys)
        

    def preprocessor_fun(self):
        try:

            logger.info(f'---------------Entered preprocessor function------------------')
            
            logger.info(f'----------creating transformer pipelines---------------')

            preprocessor = Pipeline(
                    [
                        ('scalar' , StandardScaler())
                    ]
            )

            logger.info(f'---------------completed creating transformer pipelines---------------')

            logger.info(f'--------------completed preprocessor function------------------')

            return preprocessor
            

        except Exception as e:
            raise CustomException(e, sys)
        

    
    def initiate_data_transformation(self):

        try:

            logger.info(f'------------started initiate_data_transformation method------------')

            train_df = pd.read_csv('artifacts//data_transformation//train.csv')
            
            test_df = pd.read_csv('artifacts//data_transformation//test.csv')

            logger.info(f'----------obtaining the preprocessor obj-----------')

            independent_train_X = train_df.drop(columns = ['PassFail'], axis = 1)
            dependent_train_Y = train_df[['PassFail']]

            independent_test_X = test_df.drop(columns = ['PassFail'], axis = 1)
            dependent_test_Y = test_df[['PassFail']]

            preprocessor_obj = self.preprocessor_fun()

            transformed_train_df = preprocessor_obj.fit_transform(independent_train_X)

            joblib.dump(preprocessor_obj, os.path.join(self.config.root_dir, 'preprocessor_obj.joblib'))

            transformed_test_df = preprocessor_obj.transform(independent_test_X)

            transformed_train_df = pd.DataFrame(np.c_[transformed_train_df, dependent_train_Y])

            transformed_test_df = pd.DataFrame(np.c_[transformed_test_df, dependent_test_Y])

            transformed_train_df.rename(columns={63 : 'PassFail'}, inplace=True)

            transformed_test_df.rename(columns={63 : 'PassFail'}, inplace=True)

            transformed_train_df.to_csv(os.path.join(self.config.root_dir, 'transformed_train_df.csv'), index = False, header = True)

            transformed_test_df.to_csv(os.path.join(self.config.root_dir, 'transformed_test_df.csv'), index = False, header = True)

            logger.info(f'-------------transformed data using preprocessor obj and saved in csv format----------')

            logger.info(f'--------------completed initiate_data_transformation method--------------')

        except Exception as e:
            raise CustomException(e, sys)