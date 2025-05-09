from flask import Flask,jsonify
from flask.typing import ResponseReturnValue
from controller import AirQualityController
from repositories import AirQualityRepository
from flask import request
from http import HTTPStatus

app = Flask(__name__)

@app.get("/get")
def get_users() -> ResponseReturnValue:
    return "get", HTTPStatus.OK

@app.post("/post")
def post_user() -> ResponseReturnValue:
    repository = AirQualityRepository()
    controller = AirQualityController(repository=repository)
    response_json = request.json
    controller.PostAirQuality(response_json)
    # print(response_json["latitude"])
    # print(response_json["longitude"])
    # for i in range(len(response_json["hourly"]["time"])):
    #     print(response_json["hourly"]["time"][i],response_json["hourly"]["pm10"][i],response_json["hourly"]["pm2_5"][i], response_json["hourly"]["carbon_monoxide"][i])
    return response_json, HTTPStatus.OK

if __name__ == '__main__':
    app.run()
    