from contextlib import contextmanager

@contextmanager
def database(name):
    db = Database(name)
    try:    
        db.connected = True
        yield db
    finally:
        db.connected = False
        print(f"Disconnected from database: {db.name}")

class Database:
    def __init__(self, name):
        self.name = name
        self.connected = False
        
    def query(self, sql):
        # προσομοίωση query
        pass

with database("users_db") as db:
    db.query("...")
    raise Exception("Database error")