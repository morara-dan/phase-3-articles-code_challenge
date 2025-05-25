from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database
from lib.db.connection import get_connection
from scripts.setup_db import setup_database
import os

def run_queries():
    if os.path.exists('articles.db'):
        os.remove('articles.db')
        print("Existing articles.db removed.")
    setup_database()
    seed_database()
    print("\n--- Running Example Queries ---")

    # Example 1: Get all articles by a specific author
    author = Author.find_by_name("Alice Wonderland")
    if author:
        print(f"\nArticles by {author.name}:")
        for article in author.articles():
            print(f"- {article.title}")

    # Example 2: Find all magazines an author has contributed to
    if author:
        print(f"\nMagazines {author.name} has contributed to:")
        for magazine in author.magazines():
            print(f"- {magazine.name} ({magazine.category})")

    # Example 3: Get all authors who have written for a specific magazine
    magazine = Magazine.find_by_name("Digital Dreams")
    if magazine:
        print(f"\nAuthors who have written for {magazine.name}:")
        for author_obj in magazine.contributors():
            print(f"- {author_obj.name}")

    # Example 4: Find magazines with articles by at least 2 different authors
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(DISTINCT a.author_id) AS num_authors
        FROM magazines m
        JOIN articles art ON m.id = art.magazine_id
        JOIN authors a ON art.author_id = a.id
        GROUP BY m.id
        HAVING num_authors >= 2
    """)
    print("\nMagazines with articles by at least 2 different authors:")
    for row in cursor.fetchall():
        print(f"- {row['name']} (by {row['num_authors']} authors)")
    conn.close()

    # Example 5: Count the number of articles in each magazine
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) AS article_count
        FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    print("\nNumber of articles in each magazine:")
    for row in cursor.fetchall():
        print(f"- {row['name']}: {row['article_count']} articles")
    conn.close()

    # Example 6: Find the author who has written the most articles
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT au.name, COUNT(ar.id) AS article_count
        FROM authors au
        JOIN articles ar ON au.id = ar.author_id
        GROUP BY au.id
        ORDER BY article_count DESC
        LIMIT 1
    """)
    most_articles_author = cursor.fetchone()
    if most_articles_author:
        print(f"\nAuthor who has written the most articles: {most_articles_author['name']} ({most_articles_author['article_count']} articles)")
    conn.close()

    # Example 7: Magazine.top_publisher() (Bonus)
    # This would be a class method on Magazine, but for demonstration, we'll run the query here.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) AS article_count
        FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        ORDER BY article_count DESC
        LIMIT 1
    """)
    top_magazine = cursor.fetchone()
    if top_magazine:
        print(f"\nTop publisher magazine: {top_magazine['name']} ({top_magazine['article_count']} articles)")
    conn.close()

    # Example 8: Transaction handling (demonstrated in Author.add_article implicitly)
    # For a more explicit example, you'd define a function like add_author_with_articles
    # as shown in the problem statement.

if __name__ == "__main__":
    run_queries()