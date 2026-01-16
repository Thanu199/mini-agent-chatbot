from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent_decide
from db import cursor, conn

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(req: ChatRequest):
    result = agent_decide(req.question)

    cursor.execute(
        "INSERT INTO chat_logs VALUES (?, ?)",
        (req.question, result["tool"])
    )
    conn.commit()

    return {
        "tool_used": result["tool"],
        "response": result["response"],
        "retrieved_context": result["context"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

