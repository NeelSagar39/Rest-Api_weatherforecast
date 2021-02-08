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

if __name__ == "__main__":
    app.run(debug=True)
