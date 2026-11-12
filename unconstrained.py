import requests
import json
from schema import WaterStation

prompt = """
Extract the water station information from this text:

El Qanater station is in Qalyubia.
Water level is 16.5 meters.
Date is 10 November 2026.

Return only a valid JSON object.

Rules:
1. station_name must be a string.
2. governorate must be a string.
3. water_level must be a number only.
4. date must be in YYYY-MM-DD format.
5. Do not use markdown or code fences.
"""

for attempt in range(3):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:1.5b",
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]
    print("Model Answer:")
    print(answer)
    
    try:
        answer = answer.replace("```json", "")
        answer = answer.replace("```", "")
        data = json.loads(answer)
        station = WaterStation.model_validate(data)

        print("Success!")
        print(station)
        break

    except Exception as e:
        print("Error:", e)
        print("Invalid answer. Trying again...")
else:
    print("Failed after 3 attempts.")