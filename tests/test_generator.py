from app.schema.schema_loader import get_schema_text
from app.llm.generator import generate_sql


schema = get_schema_text()

query = "Show all users from USA"

sql = generate_sql(query, schema)

print(sql)