# Text-to-SQL Semantic Parser

LLM-powered natural language to SQL query engine that converts user questions into executable SQL using local language models, schema-aware prompting, validation, and FastAPI.

---

## Overview

This project translates natural language questions into executable SQL queries using a local LLM pipeline powered by Ollama and Phi-3. It automatically extracts database schema context, generates SQL through prompt-engineered semantic parsing, validates the generated query for safety, executes it against a relational database, and returns structured results through a FastAPI API.

---

## Features

* Natural Language → SQL generation using local LLMs (Ollama / Phi-3)
* Automatic database schema extraction for schema-aware prompting
* SQL sanitization and validation layer for safer execution
* SQLite execution engine
* Modular end-to-end pipeline architecture
* FastAPI REST API interface
* Dockerized backend support
* Fully local inference (no paid API dependency)

---

## Architecture

```text
User Query
   ↓
Schema Extraction
   ↓
LLM SQL Generation
   ↓
SQL Validation / Cleanup
   ↓
SQL Execution
   ↓
Results Returned
```

---

## Example

### Input

```text
Show all users from USA
```

### Generated SQL

```sql
SELECT * FROM users WHERE country = 'USA';
```

### Output

```python
[(1, 'Alice', 'USA'), (3, 'Charlie', 'USA')]
```

---

## Tech Stack

* Python
* FastAPI
* Ollama
* Phi-3
* SQLite
* Docker

---

## Project Structure

```text
text-to-sql-semantic-parser/
│
├── app/
│   ├── executor/
│   ├── llm/
│   ├── schema/
│   ├── validator/
│   ├── main.py
│   └── pipeline.py
│
├── data/
│   ├── database.db
│   └── setup_db.py
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/pavanrex/nl-to-sql-semantic-parser.git
cd nl-to-sql-semantic-parser
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Setup Database

```bash
python data/setup_db.py
```

---

### Start Local LLM

```bash
ollama run phi3
```

---

### Run API Server

```bash
uvicorn app.main:app --reload
```

---

## API Usage

Visit Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

### POST `/query`

Request Body:

```json
{
  "query": "Show all users from USA"
}
```

---

## Future Improvements

* Multi-database support (PostgreSQL / MySQL)
* Query history logging / analytics
* Frontend interactive dashboard
* Benchmark suite for SQL generation accuracy
* Advanced SQL parsing / AST validation

```
```
