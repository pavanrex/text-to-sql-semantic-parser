# Text-to-SQL Semantic Parser

## Features

- Natural language → SQL generation using local LLMs (Ollama / Phi-3)
- Automatic database schema extraction for context-aware prompting
- SQL sanitization and validation layer
- SQLite execution engine
- FastAPI REST API endpoint for querying
- Modular pipeline architecture
- Dockerized backend support

## Architecture

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

## Example

Input:
"Show all users from USA"

Generated SQL:
SELECT * FROM users WHERE country = 'USA';

Output:
[(1, 'Alice', 'USA'), (3, 'Charlie', 'USA')]

## Tech Stack

- Python
- FastAPI
- Ollama
- Phi-3
- SQLite
- Docker
