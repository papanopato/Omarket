from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env locally

from orchestrator.ceo_agent import CEOAgent

app = FastAPI(title="PAPANO AI - Orchestrator")

ceo = CEOAgent()

class Objective(BaseModel):
    objective: str
    context: dict = {}

@app.post("/execute")
async def execute(obj: Objective):
    try:
        report = ceo.execute(obj.objective, obj.context)
        return {"status": "ok", "report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy", "env": os.getenv("OPENAI_API_KEY") is not None}
