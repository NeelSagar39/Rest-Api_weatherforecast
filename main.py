from flask import Flask
from flask_restful import Api,Resource
import data
import model
app = Flask(__name__)
api = Api(app)

class test_ex(Resource):
    def get(self):
        historical_data = data.request_hourly()
        j_pred = model.train_model(historical_data)
        return j_pred
api.add_resource(test_ex,"/get-predictions")

if __name__ == "__main__":
    app.run(debug=True)
