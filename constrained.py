import requests
from schema import WaterStation

prompt = """
Extract the water station information:

El Qanater station is in Qalyubia.
Water level is 16.5 meters.
Date is 10 November 2026.

Return the information as JSON.
The date must be in YYYY-MM-DD format.
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "format": WaterStation.model_json_schema(),
        "stream": False,
        "options": {
            "temperature": 0
        }
    }
)

answer = response.json()["response"]

station = WaterStation.model_validate_json(answer)

print("Success!")
print(station)