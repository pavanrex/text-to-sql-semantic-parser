from app.pipeline import run_text_to_sql_pipeline

response = run_text_to_sql_pipeline("Show all users from USA")

print(response)