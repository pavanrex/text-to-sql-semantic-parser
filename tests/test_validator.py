from app.validator.sql_validator import clean_sql, validate_sql

raw_sql = """```sql
SELECT * FROM users WHERE country = 'USA';
```"""

cleaned = clean_sql(raw_sql)

print("Cleaned SQL:")
print(cleaned)

print("Is Valid:", validate_sql(cleaned))