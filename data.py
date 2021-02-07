import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import time
import datetime
import requests
##http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=53.34399&lon=-6.26719&dt=1612310400&appid=6479fa080a30d358d9e38b388fc8c697
# r = requests.get("http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=53.34399&lon=-6.26719&dt=1612310400&appid=6479fa080a30d358d9e38b388fc8c697")
# data = r.content
# data_dict = json.loads(data)
#print(data_dict['hourly'])
def request_hourly():
  current_time = datetime.date.today()
  previous_day = str(current_time.year)+"-0"+str(current_time.month)+"-0"+str(current_time.day-1)
  previous_day_2 = str(current_time.year)+"-0"+str(current_time.month)+"-0"+str(current_time.day-2)
  previous_day_3 = str(current_time.year)+"-0"+str(current_time.month)+"-0"+str(current_time.day-3)
  previous_day_4 = str(current_time.year)+"-0"+str(current_time.month)+"-0"+str(current_time.day-4)
  time_0 = int(time.mktime(datetime.datetime.strptime(str(current_time), "%Y-%m-%d").timetuple()))
  time_1 = int(time.mktime(datetime.datetime.strptime(previous_day, "%Y-%m-%d").timetuple()))
  time_2 = int(time.mktime(datetime.datetime.strptime(previous_day_2, "%Y-%m-%d").timetuple()))
  time_3 = int(time.mktime(datetime.datetime.strptime(previous_day_3, "%Y-%m-%d").timetuple()))
  time_4 = int(time.mktime(datetime.datetime.strptime(previous_day_4, "%Y-%m-%d").timetuple()))
  historical_data = []
  for t in [time_4,time_3,time_2,time_1,time_0]:
    r = requests.get("http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=53.34399&lon=-6.26719&dt="+str(t)+"&appid=6479fa080a30d358d9e38b388fc8c697")
    data = r.content
    data_dict = json.loads(data)
    hourly_data = json.loads(json.dumps(data_dict['hourly']))
    historical_data.append(hourly_data)
  return historical_data

historical_data = request_hourly()
