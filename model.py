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
    print(train)
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(train, lags=[6,12,24,48]).fit()
    predictions = model_ar_fit.predict(start = len(train),end=len(train)+(12))
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    json_predictions = dict(enumerate(proper_data))
    return json_predictions


def train_rainfall_model(historical_data):
    not_important,train = pre_process(historical_data)
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
            rain_final.append(0.30)
        elif j == 'Drizzle':
            rain_final.append(0.50)
        elif j == 'Rain':
            rain_final.append(1)
        else:
            rain_final.append(0)
    model_ar_fit = AutoReg(rain_final, lags=[6,12,24,48]).fit()
    predictions = model_ar_fit.predict(start = len(rain_final),end=len(rain_final)+(12))
    json_predictions = dict(enumerate(predictions))
    return json_predictions

def train_humidity_model(historical_data):
    humidity = []
    for d in historical_data:
        for h in d:
            humidity.append(dict(h)['humidity']) 
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(humidity, lags=[6,12]).fit()
    predictions = model_ar_fit.predict(start = len(humidity),end=len(humidity)+(12))
    json_predictions = dict(enumerate(predictions))
    return json_predictions                

def train_wind_speed_model(historical_data):
    windspeed = []
    for d in historical_data:
        for h in d:
            
            windspeed.append(dict(h)['wind_speed']) 
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(windspeed, lags=24).fit()
    predictions = model_ar_fit.predict(start = len(windspeed),end=len(windspeed)+(12))
    json_predictions = dict(enumerate(predictions))
    return json_predictions

def train_cloudy_model(historical_data):
    cloudy = []
    for d in historical_data:
        for h in d:
            cloudy.append(dict(h)['clouds'])
    cloudy_final = []
    for j in cloudy:
        if j >= 75:
            cloudy_final.append(1)
        elif j >= 50:
            cloudy_final.append(0.50)
        elif j >= 0:
            cloudy_final.append(0)
        else:
            cloudy_final.append(0)
    print(cloudy_final)
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(cloudy_final, lags=[24]).fit()
    predictions = model_ar_fit.predict(start = len(cloudy_final),end=len(cloudy_final)+(12))
    json_predictions = dict(enumerate(predictions))
    return json_predictions

def train_temp_model_weekly(historical_data):
    daily_temp = []
    for d in historical_data:
        daily_temp.append(dict(d)['temp'])
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(daily_temp, lags=7).fit()
    predictions = model_ar_fit.predict(start=len(daily_temp),end=len(daily_temp)+7)
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    json_predictions = dict(enumerate(proper_data))
    return json_predictions


def train_humidty_model_weekly(historical_data):
    daily_temp = []
    for d in historical_data:
        daily_temp.append(dict(d)['humidity'])
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(daily_temp, lags=7).fit()
    predictions = model_ar_fit.predict(start=len(daily_temp),end=len(daily_temp)+7)
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    json_predictions = dict(enumerate(proper_data))
    return json_predictions

def train_cloud_model_weekly(historical_data):
    daily_temp = []
    for d in historical_data:
        daily_temp.append(dict(d)['cloudcover'])
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(daily_temp, lags=7).fit()
    predictions = model_ar_fit.predict(start=len(daily_temp),end=len(daily_temp)+7)
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    json_predictions = dict(enumerate(proper_data))
    return json_predictions

def train_rain_model_weekly(historical_data):
    daily_temp = []
    for d in historical_data:
        daily_temp.append((dict(d)['precipcover']/24)*100)
    print(daily_temp)
    from statsmodels.tsa.ar_model import AutoReg
    from sklearn.metrics import mean_squared_error
    model_ar_fit = AutoReg(daily_temp, lags=7).fit()
    predictions = model_ar_fit.predict(start=len(daily_temp),end=len(daily_temp)+7)
    proper_data = []
    for i in predictions:
        new_i = math.floor(i)
        proper_data.append(new_i)
    json_predictions = dict(enumerate(proper_data))
    return json_predictions  
    
    # from statsmodels.tsa.ar_model import AutoReg
    # from sklearn.metrics import mean_squared_error
    # model_ar_fit = AutoReg(daily_temp, lags=7).fit()
    # predictions = model_ar_fit.predict(start=len(daily_temp),end=len(daily_temp)+7)
    # proper_data = []
    # for i in predictions:
    #     new_i = math.floor(i)
    #     proper_data.append(new_i)
    # json_predictions = dict(enumerate(proper_data))
    # return "null"




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