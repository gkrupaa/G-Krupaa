import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "songs.db"
print(f"Checking database at: {db_path}")
print(f"Database exists: {db_path.exists()}")

try:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("\nTables in database:", tables)
        
        # If songs table exists, show sample
        if ('songs',) in tables:
            cursor.execute("SELECT COUNT(*) FROM songs")
            count = cursor.fetchone()[0]
            print(f"\nTotal songs: {count}")
            
            cursor.execute("SELECT * FROM songs LIMIT 1")
            print("\nSample record:", cursor.fetchone())
        else:
            print("\nNo 'songs' table found!")
except Exception as e:
    print(f"Error accessing database: {e}")