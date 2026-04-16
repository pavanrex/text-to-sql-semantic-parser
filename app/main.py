from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.pipeline import run_text_to_sql_pipeline


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "Text-to-SQL API is running"}


@app.post("/query")
def query_database(request: QueryRequest):
    response = run_text_to_sql_pipeline(request.query)
    return response