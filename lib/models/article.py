from lib.db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        self._title = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                           (self.title, self.author_id, self.magazine_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                           (self.title, self.author_id, self.magazine_id, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, title, author_id, magazine_id):
        article = cls(title=title, author_id=author_id, magazine_id=magazine_id)
        article.save()
        return article

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) if row else None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = cursor.fetchone()
        conn.close()
        return cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) if row else None

    @classmethod
    def find_by_author(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in rows]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in rows]

    def author(self):
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)