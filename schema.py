from pydantic import BaseModel
from datetime import date

class WaterStation(BaseModel):
    station_name: str
    governorate: str
    water_level: float
    date: date