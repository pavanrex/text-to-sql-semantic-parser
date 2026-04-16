import re


FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]


def clean_sql(raw_sql: str) -> str:
    """
    Remove markdown/code fences and extra whitespace.
    """
    raw_sql = re.sub(r"```sql|```", "", raw_sql, flags=re.IGNORECASE)
    return raw_sql.strip()


def validate_sql(sql: str) -> bool:
    """
    Reject dangerous SQL commands.
    """
    upper_sql = sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in upper_sql:
            return False

    return True