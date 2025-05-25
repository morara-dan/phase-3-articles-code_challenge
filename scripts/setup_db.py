from lib.db.connection import get_connection
import os

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    if os.path.exists('articles.db'):
        os.remove('articles.db')
        print("Existing articles.db removed.")
    setup_database()