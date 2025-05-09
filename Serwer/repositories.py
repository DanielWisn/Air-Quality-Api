import json

class AirQualityRepository:
    @staticmethod
    def GetAirQuality() -> list:
        with open('./Serwer/data.json','r') as f:
            data = json.load(f)
        
    @staticmethod
    def PostAirQuality() -> None:
        with open('./Serwer/data.json','r') as f:
            data = json.load(f)
        with open('./Serwer/data.json','w') as f:
            json.dump(data,f)