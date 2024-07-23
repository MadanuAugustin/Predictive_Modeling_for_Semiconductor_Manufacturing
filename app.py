



import sys
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from src.semiconductor import logger, CustomException
from src.semiconductor.pipeline.prediction_pipeline import PredictionPipeline



# initializing the flask app

app = Flask(__name__)


# route to display the home page

@app.route('/predict', methods = ['POST', 'GET'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('index.html')
    

    else : 
        try:
            feature_1 = request.form.get('feature_1')
            feature_2 = request.form.get('feature_2')
            feature_3 = request.form.get('feature_3')
            feature_4 = request.form.get('feature_4')
            feature_5 = request.form.get('feature_5')
            feature_6 = request.form.get('feature_6')
            feature_7 = request.form.get('feature_7')
            feature_8 = request.form.get('feature_8')
            feature_9 = request.form.get('feature_9')
            feature_10 = request.form.get('feature_10')
            feature_11 = request.form.get('feature_11')
            feature_12 = request.form.get('feature_12')
            feature_13 = request.form.get('feature_13')
            feature_14 = request.form.get('feature_14')
            feature_15 = request.form.get('feature_15')
            feature_16 = request.form.get('feature_16')
            feature_17 = request.form.get('feature_17')
            feature_18 = request.form.get('feature_18')
            feature_19 = request.form.get('feature_19')
            feature_20 = request.form.get('feature_20')
            feature_21 = request.form.get('feature_21')
            feature_22 = request.form.get('feature_22')
            feature_23 = request.form.get('feature_23')
            feature_24 = request.form.get('feature_24')
            feature_25 = request.form.get('feature_25')
            feature_26 = request.form.get('feature_26')
            feature_27 = request.form.get('feature_27')
            feature_28 = request.form.get('feature_28')
            feature_29 = request.form.get('feature_29')
            feature_30 = request.form.get('feature_30')
            feature_31 = request.form.get('feature_31')
            feature_32 = request.form.get('feature_32')
            feature_33 = request.form.get('feature_33')
            feature_34 = request.form.get('feature_34')
            feature_35 = request.form.get('feature_35')
            feature_36 = request.form.get('feature_36')
            feature_37 = request.form.get('feature_37')
            feature_38 = request.form.get('feature_38')
            feature_39 = request.form.get('feature_39')
            feature_40 = request.form.get('feature_40')
            feature_41 = request.form.get('feature_41')
            feature_42 = request.form.get('feature_42')
            feature_43 = request.form.get('feature_43')
            feature_44 = request.form.get('feature_44')
            feature_45 = request.form.get('feature_45')
            feature_46 = request.form.get('feature_46')
            feature_47 = request.form.get('feature_47')
            feature_48 = request.form.get('feature_48')
            feature_49 = request.form.get('feature_49')
            feature_50 = request.form.get('feature_50')
            feature_51 = request.form.get('feature_51')
            feature_52 = request.form.get('feature_52')
            feature_53 = request.form.get('feature_53')
            feature_54 = request.form.get('feature_54')
            feature_55 = request.form.get('feature_55')
            feature_56 = request.form.get('feature_56')
            feature_57 = request.form.get('feature_57')
            feature_58 = request.form.get('feature_58')
            feature_59 = request.form.get('feature_59')
            feature_60 = request.form.get('feature_60')
            feature_61 = request.form.get('feature_61')
            feature_62 = request.form.get('feature_62')
            feature_63 = request.form.get('feature_63')

            data = [feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9,feature_10,
                    feature_11,feature_12,feature_13,feature_14,feature_15,feature_16,feature_17,feature_18,feature_19,
                    feature_20,feature_21,feature_22,feature_23,feature_24,feature_25,feature_26,feature_27,feature_28,
                    feature_29,feature_30,feature_31,feature_32,feature_33,feature_34,feature_35,feature_36,feature_37,
                    feature_38,feature_39,feature_40,feature_41,feature_42,feature_43,feature_44,feature_45,feature_46,
                    feature_47,feature_48,feature_49,feature_50,feature_51,feature_52,feature_53,feature_54,feature_55,
                    feature_56,feature_57,feature_58,feature_59,feature_60,feature_61,feature_62,feature_63]
            
            logger.info(f'-----------Feteched data successfully from the user--------------')
            

            data = np.array(data).reshape(1, 63)

            data = pd.DataFrame(data)

            print(data)

            obj = PredictionPipeline()

            results = obj.predictDatapoint(data)

            logger.info(f'-----------Below is the final result {results}------------------')

            print(results)

            return render_template('index.html', results = str(results))


        except Exception as e:
            raise CustomException(e, sys)
        



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8080, debug = True) ## http://127.0.0.1:5000





