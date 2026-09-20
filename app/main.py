from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="k-public-data-mcp",version="0.3.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-public-data-mcp","version":"0.3.0"}
@app.post("/analyze")
def analyze(req:Query): return {"domain":"public-data-router","query":req.query,"checks":["railway","land/building","transport","tourism","policy"],"status":"prototype"}
