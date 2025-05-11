import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--lat", type=float, help="Szerokość geograficzna", required=False)
parser.add_argument("--lon", type=float, help="Długość geograficzna", required=False)
args = parser.parse_args()

if args.lat != None and args.lon != None:
    coordinates = (args.lat, args.lon)
else:
    coordinates = (52.237049,21.017532)

url = "https://api.open-meteo.com/v1/forecast"

params = {
	"latitude": coordinates[0],
	"longitude": coordinates[1],
	"hourly": ["temperature_2m", "wind_speed_10m", "relative_humidity_2m"],
	"timezone": "auto",
	"forecast_days": 1
}

response = requests.get(url,params=params)
response_json = response.json()
post_json = {
    "latitude": response_json["latitude"],
	"longitude": response_json["longitude"],
	"hourly": response_json["hourly"],
}

requests.post(url="http://127.0.0.1:5000/post",json=post_json)