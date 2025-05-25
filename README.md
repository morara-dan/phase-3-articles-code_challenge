# Object Relations Code Challenge - Articles

This project models the relationships between Authors, Articles, and Magazines, with data persisted in a SQL database.

## Setup Instructions

1.  **Install dependencies**:
    ```bash
    pipenv install pytest
    ```
2.  **Activate virtual environment**:
    ```bash
    pipenv shell
    ```

## Project Structure

```
code-challenge/
├── lib/
│ ├── models/
│ │ ├── __init__.py
│ │ ├── author.py
│ │ ├── article.py
│ │ └── magazine.py
│ ├── db/
│ │ ├── __init__.py
│ │ ├── connection.py
│ │ ├── seed.py
│ │ └── schema.sql
│ ├── debug.py
│ └── __init__.py
├── tests/
│ ├── __init__.py
│ ├── test_author.py
│ ├── test_article.py
│ └── test_magazine.py
├── scripts/
│ ├── setup_db.py
│ └── run_queries.py
└── README.md
└── .gitignore
```

## Database Setup

This project uses SQLite. The database connection is configured in [`lib/db/connection.py`](lib/db/connection.py).

## Running Tests

To run tests, ensure you have activated the virtual environment and then execute:
```bash
pytest
```

## Deliverables

-   **Database Schema**: Defined in [`lib/db/schema.sql`](lib/db/schema.sql).
-   **Python Classes with SQL Methods**: `Author`, `Article`, and `Magazine` classes implemented in `lib/models/`.
-   **SQL Query Methods**: Various relationship queries implemented within the model classes.
-   **Database Transactions**: Example transaction handling for adding authors and articles.