from flask import Flask
from flask_restful import Api,Resource
import data
import model
app = Flask(__name__)
api = Api(app)

class temp_res(Resource):
    def get(self):
        historical_data = data.request_hourly()
        j_pred = model.train_temp_model(historical_data)
        return j_pred
api.add_resource(temp_res,"/get-temp-predictions")

class rain_res(Resource):
    def get(self):
        historical_data = data.request_hourly()
        j_pred = model.train_rainfall_model(historical_data)
        return j_pred
api.add_resource(rain_res,"/get-rainfall-predictions")

class humidity_res(Resource):
    def get(self):
        historical_data = data.request_hourly()
        j_pred = model.train_humidity_model(historical_data)
        return j_pred
api.add_resource(humidity_res,"/get-humidity-predictions")

class wind_res(Resource):
    def get(self):
        historical_data = data.request_hourly()
        j_pred = model.train_wind_speed_model(historical_data)
        return j_pred
api.add_resource(wind_res,"/get-wind-predictions")

class cloudy_res(Resource):
    def get(self):
        historical_data = data.request_hourly()
        j_pred = model.train_cloudy_model(historical_data)
        return j_pred
api.add_resource(cloudy_res,"/get-cloudy-predictions")

class temp_weekly(Resource):
    def get(self):
        historical_data = data.request_weekly()
        j_pred = model.train_temp_model_weekly(historical_data)
        return j_pred
api.add_resource(temp_weekly,"/get-temp-weekly")


class rain_weekly(Resource):
    def get(self):
        historical_data = data.request_weekly()
        j_pred = model.train_rain_model_weekly(historical_data)
        return j_pred
api.add_resource(rain_weekly,"/get-rain-weekly")


class humidity_weekly(Resource):
    def get(self):
        historical_data = data.request_weekly()
        j_pred = model.train_humidty_model_weekly(historical_data)
        return j_pred
api.add_resource(humidity_weekly,"/get-humidity-weekly")


class cloud_weekly(Resource):
    def get(self):
        historical_data = data.request_weekly()
        j_pred = model.train_cloud_model_weekly(historical_data)
        return j_pred
api.add_resource(cloud_weekly,"/get-cloud-weekly")

class wind_weekly(Resource):
    def get(self):
        historical_data = data.request_weekly()
        j_pred = model.train_wind_model_weekly(historical_data)
        return j_pred
api.add_resource(wind_weekly,"/get-wind-weekly")

if __name__ == "__main__":
    app.run(debug=True)
