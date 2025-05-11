import json

class WeatherRepository:
    @staticmethod
    def GetWeatherForecast() -> list:
        with open('./Serwer/data.json','r') as f:
            data = json.load(f)
        
    @staticmethod
    def PostWeatherForecast() -> None:
        with open('./Serwer/data.json','r') as f:
            data = json.load(f)
        with open('./Serwer/data.json','w') as f:
            json.dump(data,f)