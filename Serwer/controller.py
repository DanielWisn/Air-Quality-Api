from repositories import AirQualityRepository
from pydantic import BaseModel
from datetime import datetime
from typing import TypedDict

class HourlyReading(BaseModel):
    time: list[datetime]
    pm10: list[float]
    pm2_5: list[float]
    carbon_monoxide: list[float]

class AirQualityReading(BaseModel):
    latitude: float
    longitude: float
    hourly: HourlyReading

class AirQualityController:
    def __init__(self, repository : AirQualityRepository) -> None:
        self._repository = repository

    def GetAirQuality(self) -> list:
        pass
    def PostAirQuality(self,AirQualityData:AirQualityReading):
        Data = AirQualityData.model_validate_json(AirQualityData)
        print(Data)