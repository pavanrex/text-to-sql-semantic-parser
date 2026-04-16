from app.executor.sql_executor import execute_sql

sql = "SELECT * FROM users WHERE country = 'USA';"

results = execute_sql(sql)

print(results)