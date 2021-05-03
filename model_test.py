import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from prediction_system import PredictionSystem 
import numpy as np
import pandas as pd
import pickle
import sklearn
import os



#model.predict([[1,80,25,30]])

app=FastAPI()

pickle_file = open('diabetes_prediction.pkl','rb')
model= pickle.load(pickle_file)

#test1 = pd.read_csv('test1.csv')

@app.get('/')
def home():
    return "testing it"


@app.post('/predict')
def predict_diabetes(data: PredictionSystem):
    data = data.dict()
    pregnancies = data['Pregnancies']
    glucose = data['Glucose']
    bmi = data['BMI']
    age = data['Age']
    prediction = model.predict([[pregnancies, glucose, bmi, age]])
    return f'The predicted value is {prediction}'
    
    
if __name__ == '__main__':
    port=int(os.environ.get("PORT",8000))
    uvicorn.run(app,host='127.0.0.1',port=port)
    
    

 