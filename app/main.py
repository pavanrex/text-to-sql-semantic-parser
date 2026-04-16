from fastapi import FastAPI
from pydantic import BaseModel

from app.pipeline import run_text_to_sql_pipeline


app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "Text-to-SQL API is running"}


@app.post("/query")
def query_database(request: QueryRequest):
    response = run_text_to_sql_pipeline(request.query)
    return response