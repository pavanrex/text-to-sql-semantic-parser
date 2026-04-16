import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_sql(user_query: str, schema: str) -> str:
    prompt = f"""
You are a SQL generation engine.

Your task:
Convert the user request into a SINGLE valid SQLite SQL query.

STRICT RULES:
- Output ONLY SQL
- No explanations
- No markdown
- No comments
- Use ONLY columns/tables from provided schema
- Do NOT invent schema fields
- Prefer simple valid SQL over complex SQL

Database Schema:
{schema}

User Request:
{user_query}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    return result.strip()