from fastmcp import FastMCP
import mysql.connector

mcp = FastMCP("Database_Expert")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="inventory_db"
    )

@mcp.tool()
def query_database(sql_query: str) -> str:
    """Executes a SQL query and returns results. Use only for SELECT statements."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql_query)
        return str(cursor.fetchall())
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        conn.close()

if __name__ == "__main__":
    mcp.run(transport="stdio")