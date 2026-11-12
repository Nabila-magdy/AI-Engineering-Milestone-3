import requests
import time
from schema import WaterStation

prompt = """
Extract the water station information:

El Qanater station is in Qalyubia.
Water level is 16.5 meters.
Date is 10 November 2026.

Return only JSON.
The water_level must be a number.
The date must be YYYY-MM-DD.
"""

def run_test(constrained):

    total_tokens = 0
    total_generation_time = 0
    errors = 0
    attempts = 0

    start = time.perf_counter()

    for i in range(3):

        attempts += 1

        settings = {
            "model": "qwen2.5:1.5b",
            "prompt": prompt,
            "stream": False
        }

        if constrained:
            settings["format"] = WaterStation.model_json_schema()

        response = requests.post(
            "http://localhost:11434/api/generate",
            json=settings
        )

       
        result = response.json()
        answer = result["response"]
        print("\nGenerated Data:")
        print(answer)

        total_tokens += result["eval_count"]
        total_generation_time += result["eval_duration"]

        try:
            answer = answer.replace("```json", "")
            answer = answer.replace("```", "")

            station = WaterStation.model_validate_json(answer)


        except Exception as e:
            errors += 1
            print("Error:", e)

    latency = (time.perf_counter() - start) / 3
    generation_seconds = total_generation_time / 1_000_000_000

    if generation_seconds > 0:
        speed = total_tokens / generation_seconds
    else:
        speed = 0

    error_rate = errors / attempts * 100

    return latency, speed, error_rate

print("Unconstrained Results:")

latency, speed, errors = run_test(False)

print("Latency:", round(latency, 2), "seconds")
print("Tokens/sec:", round(speed, 2))
print("Schema Validation Error Rate:", round(errors, 2), "%")

print("\nConstrained Results:")

latency, speed, errors = run_test(True)

print("Latency:", round(latency, 2), "seconds")
print("Tokens/sec:", round(speed, 2))
print("Schema Validation Error Rate:", round(errors, 2), "%")