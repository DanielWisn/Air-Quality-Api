from flask import Flask,jsonify
from flask.typing import ResponseReturnValue
from flask.views import MethodView
from controller import WeatherController
from repositories import WeatherRepository
from flask import request
from http import HTTPStatus

app = Flask(__name__)

class WeatherAPI(MethodView):
    def __init__(self) -> None:
        self.repository = WeatherRepository()
        self.controller = WeatherController(self.repository)
    
    def get(self, date:str) -> ResponseReturnValue:
        data = self.controller.GetWeatherForecast(date=date)
        if data == ValueError:
            return jsonify(),HTTPStatus.BAD_REQUEST
        else:
            return jsonify(data), HTTPStatus.OK

    def post(self) -> ResponseReturnValue:
        response_json = request.json
        if self.controller.PostWeatherForecast(response_json) == ValueError:
            return jsonify(), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(), HTTPStatus.OK
        
WeatherView = WeatherAPI.as_view('WeatherApi')
app.add_url_rule('/get/<string:date>', view_func=WeatherView)
app.add_url_rule('/post/', view_func=WeatherView)

if __name__ == '__main__':
    app.run()
    