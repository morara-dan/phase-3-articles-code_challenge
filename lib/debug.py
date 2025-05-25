from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection
from lib.db.seed import seed_database
import ipdb

def debug_session():
    conn = get_connection()
    cursor = conn.cursor()

    # Clear and seed the database
    cursor.execute("DROP TABLE IF EXISTS articles")
    cursor.execute("DROP TABLE IF EXISTS authors")
    cursor.execute("DROP TABLE IF EXISTS magazines")
    conn.commit()
    conn.close()
    seed_database()

    print("Database seeded. Starting debug session...")
    ipdb.set_trace()

if __name__ == "__main__":
    debug_session()