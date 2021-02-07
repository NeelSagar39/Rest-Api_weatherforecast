import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import time
import datetime
import math
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
    

def pre_process(historical_data):
    temp = []
    for d in historical_data:
        for h in d:
            temp.append(dict(h)['temp']-273.15) 
    return temp
def train_model(historical_data):
    temp = pre_process(historical_data)
    train = temp
    print(temp[-5:])
    #test = temp[75::]
    model_ar_fit = AutoReg(train, lags=[6,12,24,48]).fit()
    predictions = model_ar_fit.predict(start = len(temp),end=len(temp)+24)
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    #print(test, predictions)
    #print(mean_squared_error(y_pred=predictions,y_true=test))
    json_predictions = dict(enumerate(proper_data))
    return json_predictions
