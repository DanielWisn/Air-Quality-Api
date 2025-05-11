from flask import Flask,jsonify
from flask.typing import ResponseReturnValue
from controller import WeatherController
from repositories import WeatherRepository
from flask import request
from http import HTTPStatus

app = Flask(__name__)

@app.get("/get/<string:date>")
def GetWeatherForecast(date:str) -> ResponseReturnValue:
    repository = WeatherRepository()
    controller = WeatherController(repository=repository)
    data = controller.GetWeatherForecast(date=date)
    if data == ValueError:
        return jsonify(),HTTPStatus.BAD_REQUEST
    else:
        return jsonify(data), HTTPStatus.OK

@app.post("/post")
def PostWeatherForecast() -> ResponseReturnValue:
    repository = WeatherRepository()
    controller = WeatherController(repository=repository)
    response_json = request.json
    if controller.PostWeatherForecast(response_json) == ValueError:
        return jsonify(), HTTPStatus.BAD_REQUEST
    else:
        return jsonify(), HTTPStatus.OK

if __name__ == '__main__':
    app.run()
    