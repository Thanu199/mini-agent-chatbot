from tools.weather_tool import get_weather
from tools.document_tool import search_document

def agent_decide(question: str):
    # Tool B: Weather
    weather = get_weather(question)
    if weather:
        return {
            "tool": "Weather Tool",
            "response": weather,
            "context": None
        }

    # Tool A: Document Search
    doc = search_document(question)
    if doc:
        return {
            "tool": "Document Search Tool",
            "response": doc,
            "context": doc
        }

    # Default
    return {
        "tool": "Default",
        "response": "I do not have enough information to answer that.",
        "context": None
    }
