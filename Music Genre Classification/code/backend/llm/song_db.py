import sqlite3
import pandas as pd
from pathlib import Path
# Load the CSV into a DataFrame


csv_file = Path(__file__).parent.parent.parent / 'data' / 'spotify_data_normalized.csv'

df = pd.read_csv(csv_file)


# Change the connection line to:
conn = sqlite3.connect(Path(__file__).parent.parent / 'songs.db')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('songs.db')
cursor = conn.cursor()

# Create the songs table
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL,
    track_name TEXT NOT NULL,
    track_id TEXT NOT NULL UNIQUE,
    popularity INTEGER,
    year INTEGER,
    genre TEXT,
    danceability REAL,
    energy REAL,
    key INTEGER,
    loudness REAL,
    mode INTEGER,
    speechiness REAL,
    acousticness REAL,
    instrumentalness REAL,
    liveness REAL,
    valence REAL,
    tempo REAL,
    duration_ms INTEGER,
    time_signature INTEGER
)
''')

# Insert data into the database
df.to_sql('songs', conn, if_exists='replace', index=False)

# Delete unwanted records
cursor.execute('''
DELETE FROM songs
WHERE LOWER(track_name) LIKE '%white noise%'
   OR LOWER(track_name) LIKE '%hz%'
   OR LOWER(track_id) LIKE '%white noise%';
''')

# Verify deletion
print("Checking for remaining 'White Noise' tracks:")
cursor.execute('''
SELECT track_name, track_id
FROM songs
WHERE LOWER(track_name) LIKE '%white noise%'
   OR LOWER(track_id) LIKE '%white noise%';
''')
results = cursor.fetchall()
for row in results:
    print(row)

# Show distinct genres
print("\nDistinct genres:")
cursor.execute('SELECT DISTINCT genre FROM songs')
genres = cursor.fetchall()
for genre in genres:
    print(genre[0])

# Commit changes and close connection
conn.commit()
conn.close()