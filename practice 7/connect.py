import psycopg2
from psycopg2 import extras
from config import DB_CONFIG


class DatabaseConnection:
    """Class for managing database connections"""
    
    def __init__(self):
        """Initialize with configuration from config.py"""
        self.config = DB_CONFIG
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = psycopg2.connect(**self.config)
            self.cursor = self.connection.cursor(
                cursor_factory=extras.RealDictCursor
            )
            print("✓ Database connection established")
            return True
        except Exception as e:
            print(f"✗ Database connection error: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("✓ Database connection closed")
    
    def execute_query(self, query, params=None):
        """Execute SQL query and return success status"""
        try:
            self.cursor.execute(query, params or ())
            return True
        except Exception as e:
            print(f"✗ Query execution error: {e}")
            return False
    
    def fetch_all(self):
        """Fetch all results from last query"""
        return self.cursor.fetchall()
    
    def fetch_one(self):
        """Fetch single result from last query"""
        return self.cursor.fetchone()
    
    def commit(self):
        """Commit current transaction"""
        self.connection.commit()
    
    def rollback(self):
        """Rollback current transaction"""
        self.connection.rollback()
    
    def create_table(self):
        """Create phonebook table if it doesn't exist"""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            phone_number VARCHAR(20) NOT NULL UNIQUE,
            email VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE INDEX IF NOT EXISTS idx_phone_number ON phonebook(phone_number);
        CREATE INDEX IF NOT EXISTS idx_first_name ON phonebook(first_name);
        CREATE INDEX IF NOT EXISTS idx_name ON phonebook(first_name, last_name);
        """
        
        if self.execute_query(create_table_query):
            self.commit()
            print("✓ Phonebook table created/verified")
            return True
        return False


db = DatabaseConnection()