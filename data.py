import datetime
import json
import time

import dateutil.relativedelta
import requests


def request_hourly():
    current_time = datetime.date.today()
    print(current_time)
    previous_day = current_time + dateutil.relativedelta.relativedelta(days=-1)
    previous_day_2 = current_time + dateutil.relativedelta.relativedelta(days=-2)
    previous_day_3 = current_time + dateutil.relativedelta.relativedelta(days=-3)
    previous_day_4 = current_time + dateutil.relativedelta.relativedelta(days=-4)
    time_0 = int(time.mktime(datetime.datetime.strptime(str(current_time), "%Y-%m-%d").timetuple()))
    time_1 = int(time.mktime(datetime.datetime.strptime(str(previous_day), "%Y-%m-%d").timetuple()))
    time_2 = int(time.mktime(datetime.datetime.strptime(str(previous_day_2), "%Y-%m-%d").timetuple()))
    time_3 = int(time.mktime(datetime.datetime.strptime(str(previous_day_3), "%Y-%m-%d").timetuple()))
    time_4 = int(time.mktime(datetime.datetime.strptime(str(previous_day_4), "%Y-%m-%d").timetuple()))
    historical_data = []
    for t in [time_4, time_3, time_2, time_1, time_0]:
        r = requests.get(
            "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=53.34399&lon=-6.26719&dt=" + str(
                t) + "&appid=6479fa080a30d358d9e38b388fc8c697")
        data = r.content
        data_dict = json.loads(data)
        hourly_data = json.loads(json.dumps(data_dict['hourly']))
        historical_data.append(hourly_data)
    return historical_data


def request_weekly():
    with open('./weather.json') as f:
        default_data = json.load(f)
    current_time = str(datetime.date.today() + dateutil.relativedelta.relativedelta(days=-1)) + "T00:00:00"
    start_day = datetime.date.today() + dateutil.relativedelta.relativedelta(days=-30)
    start_day = str(start_day) + "T00:00:00"
    url = "https://visual-crossing-weather.p.rapidapi.com/history"

    querystring = {"startDateTime": start_day, "aggregateHours": "24", "location": "53.34399,-6.26719",
                   "endDateTime": current_time,
                   "unitGroup": "metric", "dayStartTime": "8:00:00", "contentType": "json", "dayEndTime": "17:00:00",
                   "shortColumnNames": "0"}

    headers = {
        'x-rapidapi-key': "cec8c91ecemshc8b58306c8d2214p173de8jsn3d0e096b467c",
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com"
    }

    response_1 = requests.request("GET", url, headers=headers, params=querystring)
    response_2 = requests.request("GET", 'https://citymanagement.herokuapp.com/flaskdata')
    if response_1.status_code == '200':
        data_dict = json.loads(response_1.text)
        print("help", data_dict)
        data_dict = dict((data_dict['locations']))
        data_dict = dict(data_dict['53.34399,-6.26719'])
        data_dict = data_dict['values']
        return data_dict
    elif response_2.status_code == '200':
        data_dict = json.loads(response_2.text)
        print(data_dict['success'])
        data_dict = data_dict['data']
        return data_dict
    else:
        return default_data
