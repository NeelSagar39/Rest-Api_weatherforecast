import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import time
import datetime
import math

    

def pre_process(historical_data):
    temp = []
    rainfall = []
    for d in historical_data:
        for h in d:
            temp.append(dict(h)['temp']-273.15) 
            rainfall.append(dict(h)['weather'])
    return temp,rainfall
def train_temp_model(historical_data):
    train,rainfall = pre_process(historical_data)
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(train, lags=[6,12,24,48]).fit()
    predictions = model_ar_fit.predict(start = len(train),end=len(train)+24)
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    json_predictions = dict(enumerate(proper_data))
    return json_predictions


def train_rainfall_model(historical_data):
    temp,train = pre_process(historical_data)
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    rainfall_data = []
    rain_final = []
    for i in train:
        print(i)
        temp = dict(i[0])
        rainfall_data.append(temp['main'])
    print(np.unique(rainfall_data))
    for j in rainfall_data:
        if j == 'Clouds':
            rain_final.append(0)
        elif j == 'Drizzle':
            rain_final.append(0.50)
        elif j == 'Rain':
            rain_final.append(1)
    model_ar_fit = AutoReg(rain_final, lags=[6,12,24,48]).fit()
    predictions = model_ar_fit.predict(start = len(rain_final),end=len(rain_final)+24)
    json_predictions = dict(enumerate(predictions))
    return json_predictions

# def train_model(historical_data):
#     temp,rainfall = pre_process(historical_data)
#     rain_data = train_rainfall_model(rainfall)
#     train = temp
#     print(temp[-5:])
#     json_predictions = train_temp_model(train)
#     # model_ar_fit = AutoReg(train, lags=[6,12,24,48]).fit()
#     # predictions = model_ar_fit.predict(start = len(temp),end=len(temp)+24)
#     # proper_data = []
#     # for i in predictions:
#     #     new_i = math.floor(i)
#     #     proper_data.append(new_i)
#     # json_predictions = dict(enumerate(proper_data))
#     return json_predictions
