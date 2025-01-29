import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.create_tables()

    def create_tables(self):
        """Creates necessary tables for the application."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table for PDF metadata
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pdf_metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Table for header templates
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS header_templates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')

            # Table for footer templates
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS footer_templates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')

            # Table for application settings
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL UNIQUE,
                    value TEXT
                )
            ''')

    def save_pdf_metadata(self, filename, file_path):
        """Saves metadata for a generated PDF."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pdf_metadata (filename, file_path)
                VALUES (?, ?)
            ''', (filename, file_path))

    def fetch_templates(self):
        """Fetches all header and footer templates."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM header_templates')
            headers = cursor.fetchall()
            cursor.execute('SELECT * FROM footer_templates')
            footers = cursor.fetchall()
            return {'headers': headers, 'footers': footers}

    def fetch_headers(self):
        """Fetches all header templates."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM header_templates')
            return cursor.fetchall()

    def fetch_footers(self):
        """Fetches all footer templates."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM footer_templates')
            return cursor.fetchall()

    def fetch_settings(self):
        """Fetches application settings."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT key, value FROM settings')
            return dict(cursor.fetchall())

    def update_settings(self, settings_data):
        """Updates application settings."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for key, value in settings_data.items():
                cursor.execute('''
                    INSERT INTO settings (key, value) VALUES (?, ?)
                    ON CONFLICT(key) DO UPDATE SET value=excluded.value
                ''', (key, value))
