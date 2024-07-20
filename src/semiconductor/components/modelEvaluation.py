
import sys
import pandas as pd
import joblib
import dagshub
import mlflow
import os
import mlflow.sklearn
from pathlib import Path
from src.semiconductor.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from src.semiconductor.utils.common import save_json
from src.semiconductor import logger, CustomException


class ModelEvaluation:
    def __init__(self, config : ModelEvaluationConfig):
        
        self.config = config


    
    def eval_metrics(self, actual, pred):
        precision = precision_score(actual, pred, average='weighted')
        recall = recall_score(actual, pred, average='weighted')
        f1 = f1_score(actual, pred, average='weighted')
        accuracy = accuracy_score(actual, pred)
        return precision, recall, f1, accuracy
    


    def log_into_mlflow(self):

        try:
            logger.info(f'-----------Entered log_into_mlflow function----------------')

            test_data = pd.read_csv(self.config.test_data_path)

            model = joblib.load(self.config.model_path)

            logger.info(f'-----------successfully loaded model joblib--------------------------')

            test_x = test_data.drop([self.config.target_column], axis=1)
            test_y = test_data[[self.config.target_column]]

            os.environ["MLFLOW_TRACKING_URI"]='https://dagshub.com/augustin7766/Predictive_Modeling_for_Semiconductor_Manufacturing.mlflow'
            os.environ["MLFLOW_TRACKING_USERNAME"]="augustin7766"
            os.environ["MLFLOW_TRACKING_PASSWORD"]="8a01ee4bec043666cf3ced22edc7d308526b4b42"

            mlflow.set_experiment('fifth_exp_05')

            with mlflow.start_run():

                logger.info(f'------------------mlflow function started--------------------------------')

                predicted = model.predict(test_x)

                (precision, recall, f1, accuracy) = self.eval_metrics(test_y, predicted)

                scores = {'precision' : precision, 'recall' : recall, 'f1' : f1, 'accuracy': accuracy}

                save_json(path = Path(self.config.metric_file_name), data = scores)

                mlflow.log_params(self.config.all_params)

                mlflow.log_metric('precision', precision)
                mlflow.log_metric('recall', recall)
                mlflow.log_metric('f1', f1)
                mlflow.log_metric('accuracy', accuracy)
                
                logger.info(f'---------All parameters logged to MLflow-----------------')

                mlflow.sklearn.log_model(model, 'model', registered_model_name = 'SupportVectorClassifier')

                logger.info(f'------------------------mlflow function completed-----------------------')

        except Exception as e:
            raise CustomException(e, sys)