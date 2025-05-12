import json
from models import WeatherReading

class WeatherRepository:
    @staticmethod
    def GetWeatherForecast(date:str) -> list:
        with open('./data.json','r') as f:
            data = json.load(f)

        for forecast in data:
            hourly = forecast["hourly"]
            dates = hourly["time"]
            if date in dates:
                index = dates.index(date)
                return {
                    "time": date,
                    "temperature_2m": hourly["temperature_2m"][index],
                    "wind_speed_10m": hourly["wind_speed_10m"][index],
                    "relative_humidity_2m": hourly["relative_humidity_2m"][index]
                }
        
    @staticmethod
    def PostWeatherForecast(WeatherForecast:WeatherReading) -> None:
        with open('./data.json','r') as f:
            data = json.load(f)
        new_times = WeatherForecast.hourly.time

        for entry in data:
            if entry["hourly"]["time"] == new_times:
                return ValueError
            
        data.append(WeatherForecast.model_dump())
        with open('./data.json','w') as f:
            json.dump(data,f)