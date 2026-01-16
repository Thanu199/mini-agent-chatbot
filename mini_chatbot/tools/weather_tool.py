import json

with open("data/weather.json") as f:
    weather_data = json.load(f)

def get_weather(question: str):
    question = question.lower()
    for city in weather_data:
        if city in question:
            return weather_data[city]
    return None
