# Mini Agent Chatbot with Tool Use (Task 3)

## Project Overview

This project implements a Mini Agent Chatbot that selects different tools based on the user's question.
The agent decides whether to use document search, weather lookup, or a default response using custom control logic.

**Selected Task:** Task 3 — Mini Agent Chatbot with Tool Use

---

## Architecture Summary

The system is built using FastAPI and follows a modular design:

* **FastAPI**: API layer
* **Agent Logic**: Decides which tool to use
* **Tool A – Document Search**:

  * Uses sentence-transformers for embeddings
  * Performs vector similarity search on local documents
* **Tool B – Weather Lookup**:

  * Uses static JSON data (no external APIs)
* **Database**:

  * SQLite database to store chat logs and tool selections

---

## Project Structure

```
mini_chatbot/
│
├── README.md
├── app.py
├── agent.py
├── db.py
├── requirements.txt
├── setup.sh
│
├── tools/
│   ├── document_tool.py
│   ├── weather_tool.py
│
├── data/
│   ├── documents.txt
│   ├── weather.json

```

---

## Setup Instructions

### Python Version

* Python 3.9+

### Create Environment & Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app:app --reload --port 8001
```

---

## API Endpoints

### POST /chat

**Input**

```json
{
  "question": "What is machine learning?"
}
```

**Output**

```json
{
  "tool_used": "Document Search Tool",
  "response": "Machine Learning is a subset of Artificial Intelligence...",
  "retrieved_context": "Machine Learning is a subset of Artificial Intelligence..."
}
```

### GET /health

Returns API health status.

---

## Agent Decision Logic

1. If the question mentions a city or weather → Weather Tool
2. If the question relates to stored documents → Document Search Tool
3. Otherwise → Default response

---

## Environment Variables

No environment variables are required.

---

## Notes & Assumptions

* Small document set is used for simplicity
* Vector similarity threshold is tuned for small datasets
* No external APIs are used
* Focus is on clarity and explainability
