from app.schema.schema_loader import get_schema_text
from app.llm.generator import generate_sql
from app.validator.sql_validator import clean_sql, validate_sql
from app.executor.sql_executor import execute_sql


def run_text_to_sql_pipeline(user_query: str):
    schema = get_schema_text()

    raw_sql = generate_sql(user_query, schema)

    cleaned_sql = clean_sql(raw_sql)

    if not validate_sql(cleaned_sql):
        raise ValueError("Generated SQL failed validation.")

    results = execute_sql(cleaned_sql)

    return {
        "user_query": user_query,
        "generated_sql": cleaned_sql,
        "results": results
    }