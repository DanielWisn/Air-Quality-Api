from pydantic import BaseModel,AfterValidator
from typing_extensions import Annotated

def PossiblePercentage(values:list) -> int:
    for i in values:
        if i < 0 or i > 100:
            raise ValueError(f"Invalid percentge: {i}")
    return values

def PossibleTemperature(values:list) -> int:
    for i in values:
        if i < -90 or i > 60:
            raise ValueError(f"Invalid temperature: {i}")
    return values

def PossibleWindSpeed(values:list) -> int:
    for i in values:
        if i < 0 or i > 120:
            raise ValueError(f"Invalid wind speed: {i}")
    return values

class HourlyReading(BaseModel):
    time: list[str]
    temperature_2m: Annotated[list[float], AfterValidator(PossibleTemperature)]
    wind_speed_10m: Annotated[list[float], AfterValidator(PossibleWindSpeed)]
    relative_humidity_2m: Annotated[list[int], AfterValidator(PossiblePercentage)]

class WeatherReading(BaseModel):
    latitude: float
    longitude: float
    hourly: HourlyReading