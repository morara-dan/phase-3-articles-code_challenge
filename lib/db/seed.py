from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()

    # Create authors
    author1 = Author.create("Alice Wonderland")
    author2 = Author.create("Bob The Builder")
    author3 = Author.create("Charlie Chaplin")
    author4 = Author.create("Diana Prince")
    author5 = Author.create("Eve Harrington")

    # Create magazines
    magazine1 = Magazine.create("Quantum Quasar", "Physics")
    magazine2 = Magazine.create("Digital Dreams", "Technology")
    magazine3 = Magazine.create("Culinary Canvas", "Food")
    magazine4 = Magazine.create("Wilderness Whispers", "Nature")
    magazine5 = Magazine.create("Cosmic Chronicles", "Astronomy")

    # Create articles
    Article.create("The Fabric of Spacetime", author1.id, magazine1.id)
    Article.create("Neural Networks Unveiled", author1.id, magazine2.id)
    Article.create("Beyond the Event Horizon", author1.id, magazine5.id)
    Article.create("The Art of Sourdough", author2.id, magazine3.id)
    Article.create("Forest Bathing Benefits", author2.id, magazine4.id)
    Article.create("AI in Everyday Life", author3.id, magazine2.id)
    Article.create("Gastronomy of the Future", author3.id, magazine3.id)
    Article.create("Stellar Nurseries", author4.id, magazine5.id)
    Article.create("The Secret Life of Trees", author4.id, magazine4.id)
    Article.create("Blockchain for Beginners", author5.id, magazine2.id)
    Article.create("The Science of Flavor", author5.id, magazine3.id)

    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()