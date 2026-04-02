import psycopg2
import psycopg2.extras
from config import DB_CONFIG

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            return True
        except Exception as e:
            print(f"DB connection error: {e}")
            return False

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            return True
        except Exception as e:
            print(f"Query error: {e}")
            return False

    def fetch_one(self):
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def fetch_all(self):
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

db = Database()