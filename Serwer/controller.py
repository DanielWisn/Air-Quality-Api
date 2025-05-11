from repositories import WeatherRepository
from models import WeatherReading
from datetime import datetime

class WeatherController:
    def __init__(self, repository : WeatherRepository) -> None:
        self._repository = repository

    def GetWeatherForecast(self,date:str) -> list:
        try:
            datetime.strptime(date, "%Y-%m-%dT%H:%M")
        except ValueError:
            return ValueError
        return self._repository.GetWeatherForecast(date)

    def PostWeatherForecast(self,WeatherData:WeatherReading) -> None:
        try:
            Data = WeatherReading(**WeatherData)
        except ValueError:
            return ValueError
        
        self._repository.PostWeatherForecast(Data)