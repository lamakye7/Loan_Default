import os
import pandas as pd
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from create_new_features import new_features
app = Flask(__name__)

# Load pre-trained model and preprocessor
with open("model_xgboost.pkl", "rb") as f:
    model = pickle.load(f)
with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)


@app.route('/', methods=['GET'])
def predict_page():
    return render_template('predict.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    
    # Apply feature engineering
    df_processed = new_features(df)
    
    # Prepare features for model
    X = df_processed.drop(['loan_amount', 'monthly_income', 'credit_score', 
                          'dti_ratio', 'num_previous_loans', 'default_history'], axis=1)
    
    # Apply preprocessing
    X_transformed = preprocessor.transform(X)
    
    # Make prediction
    prediction = model.predict(X_transformed)
    
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)