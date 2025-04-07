from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path
from app.recommender import recommend_query

app = FastAPI()
DATA_PATH = Path("data/shl_assessments.json")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "SHL Recommender API is running 🚀"}

@app.get("/recommend")
def get_all_assessments():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
        return {"results": data}
    return {"results": []}

@app.post("/recommend")
def recommend(req: QueryRequest):
    return {"results": recommend_query(req.query)}
