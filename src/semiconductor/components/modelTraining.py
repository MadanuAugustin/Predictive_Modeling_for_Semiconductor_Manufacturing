import sys
import pandas as pd
import joblib
import os
from src.semiconductor.entity.config_entity import ModelTrainerConfig
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from src.semiconductor import logger, CustomException



class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config


    def initiate_model_training(self):
        try:

            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            train_x = train_data.drop([self.config.target_column], axis = 1)
            test_x = test_data.drop([self.config.target_column], axis = 1)
            

            train_y = train_data[[self.config.target_column]]
            test_y = test_data[[self.config.target_column]]

            svc = Pipeline(
            [
                ('pca' , PCA(n_components = 32)),
                ('svc' , SVC())
            ]
            )

            svc.fit(train_x, train_y)

            logger.info(f'-------Model Training completed--------------')

            joblib.dump(svc, os.path.join(self.config.root_dir, self.config.model_name))

            logger.info(f'----------Trained model saved successfully-------------')

        except Exception as e:
            raise CustomException(e, sys)