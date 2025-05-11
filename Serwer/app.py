from flask import Flask,jsonify
from flask.typing import ResponseReturnValue
from controller import WeatherController
from repositories import WeatherRepository
from flask import request
from http import HTTPStatus

app = Flask(__name__)

@app.get("/get")
def get_users() -> ResponseReturnValue:
    return "get", HTTPStatus.OK

@app.post("/post")
def post_user() -> ResponseReturnValue:
    repository = WeatherRepository()
    controller = WeatherController(repository=repository)
    response_json = request.json
    if controller.PostWeatherForecast(response_json) == ValueError:
        return jsonify(), HTTPStatus.BAD_REQUEST
    else:
        return jsonify(), HTTPStatus.OK

if __name__ == '__main__':
    app.run()
    