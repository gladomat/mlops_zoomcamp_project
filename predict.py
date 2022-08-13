import os
import pickle
import pandas as pd

import mlflow
from flask import Flask, request, jsonify

with open('.models/full_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

RUN_ID = os.getenv('RUN_ID')

logged_model = f's3:///gladm-mlops-zoomcamp/2/{RUN_ID}/artifacts/model.pkl'
model = mlflow.pyfunc.load_model(logged_model)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def preprocess(df: pd.DataFrame, model_path: str=None):
    """
    Preprocess the dataframe.
    
    :param df: The dataframe to preprocess.
    :return: The preprocessed dataframe and the pipeline.
    """

    # Compute volume of diamonds.
    df['volume'] = df['depth'] * df['table'] * df['price']
    
    # Drop unnecessary columns
    df.drop(['x', 'y', 'z', 'depth', 'table', 'Unnamed: 0'], axis=1, inplace=True)

    # Create dummies and combine with numerical data.
    return pipeline.fit(df)

def predict(features):
    pass

app = Flask('diamond-price-predictor')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = preprocess(pd.DataFrame(data))
    prediction = predict(features)

    result = {'diamon_price': prediction}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)