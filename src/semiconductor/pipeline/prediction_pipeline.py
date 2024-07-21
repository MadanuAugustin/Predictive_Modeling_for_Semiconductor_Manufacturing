




import sys
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.semiconductor  import logger, CustomException


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts//model_trainer//model.joblib'))
        self.preprocessorObj = joblib.load(Path('artifacts//data_transformation//preprocessor_obj.joblib'))


    # the below method takes the data from the user to predict

    def predictDatapoint(self, data):
        
        try:

            # data_df = data.rename(columns = {0 : 'age', 1 : 'bmi', 2 : 'sex', 3 : 'smoker'})

            data_df = data
            
            print(data_df)

            transformed_numeric_cols = self.preprocessorObj.transform(data_df)

            logger.info(f'---------Below is the transformed user input----------------')

            print(transformed_numeric_cols)

            prediction = self.model.predict(transformed_numeric_cols)

            list_output  = []

            if prediction == [1.]:
                list_output.append('Pass')
            elif prediction == [-1.]:
                list_output.append('Fail')

            logger.info(f'-----------Below output is predicted by the model---------------')

            print(prediction)

            return list_output
        
        
        except Exception as e:
            raise CustomException(e, sys)