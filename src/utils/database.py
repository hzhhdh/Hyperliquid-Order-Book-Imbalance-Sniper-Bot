import sqlite3
from cryptography.fernet import Fernet

class Database:
    """Handles encrypted local data persistence."""
    def __init__(self, db_path, key):
        self.conn = sqlite3.connect(db_path)
        self.cipher = Fernet(key)
