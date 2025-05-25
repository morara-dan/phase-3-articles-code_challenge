import pytest
from lib.models.author import Author
from lib.db.connection import get_connection
import os

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS articles")
    cursor.execute("DROP TABLE IF EXISTS authors")
    cursor.execute("DROP TABLE IF EXISTS magazines")
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    yield
    if os.path.exists('articles.db'):
        os.remove('articles.db')

def test_author_creation():
    author = Author.create("John Doe")
    assert author.id is not None
    assert author.name == "John Doe"

def test_author_name_validation():
    with pytest.raises(TypeError):
        Author.create(123)
    with pytest.raises(ValueError):
        Author.create("Jo")
    with pytest.raises(ValueError):
        Author.create("This is a very long name for an author")

def test_find_author_by_id():
    author = Author.create("Jane Smith")
    found_author = Author.find_by_id(author.id)
    assert found_author.name == "Jane Smith"

def test_find_author_by_name():
    author = Author.create("Alice Wonderland")
    found_author = Author.find_by_name("Alice Wonderland")
    assert found_author.id == author.id

def test_author_articles_relationship():
    from lib.models.magazine import Magazine
    from lib.models.article import Article

    author = Author.create("Test Author")
    magazine1 = Magazine.create("Tech Weekly", "Technology")
    magazine2 = Magazine.create("Science Today", "Science")

    article1 = author.add_article(magazine1, "The Future of AI")
    article2 = author.add_article(magazine2, "Quantum Computing Explained")

    articles = author.articles()
    assert len(articles) == 2
    assert article1 in articles
    assert article2 in articles

def test_author_magazines_relationship():
    from lib.models.magazine import Magazine
    from lib.models.article import Article

    author = Author.create("Test Author 2")
    magazine1 = Magazine.create("Tech Monthly", "Technology")
    magazine2 = Magazine.create("Nature Explorer", "Nature")
    magazine3 = Magazine.create("Gaming World", "Gaming")

    author.add_article(magazine1, "New Gadgets")
    author.add_article(magazine2, "Wildlife Photography")
    author.add_article(magazine1, "Software Trends")

    magazines = author.magazines()
    assert len(magazines) == 2
    assert magazine1 in magazines
    assert magazine2 in magazines
    assert magazine3 not in magazines

def test_author_topic_areas():
    from lib.models.magazine import Magazine
    from lib.models.article import Article

    author = Author.create("Test Author 3")
    magazine1 = Magazine.create("Tech Daily", "Technology")
    magazine2 = Magazine.create("Health News", "Health")
    magazine3 = Magazine.create("Tech Reviews", "Technology")

    author.add_article(magazine1, "AI Ethics")
    author.add_article(magazine2, "Healthy Living")
    author.add_article(magazine3, "Latest Smartphones")

    topic_areas = author.topic_areas()
    assert len(topic_areas) == 2
    assert "Technology" in topic_areas
    assert "Health" in topic_areas