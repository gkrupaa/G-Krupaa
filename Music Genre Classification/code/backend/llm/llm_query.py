from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import sqlite3
import pandas as pd
import os
from pathlib import Path

# Load the dataset and connect to the SQLite database
# DB_PATH = Path(__file__).parent.parent / "songs.db"

# Use the /tmp directory to store the database in Render
DB_PATH = Path('/tmp/songs.db')
# Change env_path definition
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Function to query ChatGPT using LangChain
def queryChatGPT3(sysMessage, humanMessage):
    try:
        # Initialize the ChatGPT model
        # model = ChatOpenAI(model="ft:gpt-3.5-turbo-1106:personal:song-sql-query:AbdBmbWp")
        model = ChatOpenAI(model="gpt-4o-mini")

        # Prepare messages for the LLM
        messages = [
            SystemMessage(content=sysMessage),
            HumanMessage(content=humanMessage),
        ]

        # Get the response
        response = model.invoke(messages)
        return response
    except Exception as e:
        print(f"Error querying ChatGPT: {e}")
        return None

def parse_preferences_to_sql(query):
    # System message to guide ChatGPT in interpreting user input
    system_message = (
        "You are a helpful assistant that converts user song preferences into an SQL query. No other responses are needed. "
        "The query should be based on numerical feature mappings from user preferences. "
        "Return ONLY the raw SQL query with no formatting, quotes, or markdown."
        "The features include 'danceability', 'energy', 'acousticness', 'valence', 'tempo', 'year', "
        "'genre', 'loudness', 'liveness', and others relevant for music. "
        "Each feature is scaled between 0 and 1, except 'year' which is a 4-digit number, "
        "and 'genre' which is a text string. An example user input might be: "
        "'I want upbeat acoustic songs for working out'. "
        "An example SQL query output for this input might be: "
        "\"SELECT * FROM songs WHERE genre = 'acoustic' AND energy > 0.658 AND tempo > 0.589900517214482 AND valence > 0.6 AND liveness < 0.226 ORDER BY popularity DESC LIMIT 10;\" "
        "KNOW: When a user asks for rock include rock-n-roll as well. Valid genres include [('acoustic',), ('afrobeat',), ('alt-rock',), ('ambient',), ('black-metal',), ('blues',), ('breakbeat',), ('cantopop',), ('chicago-house',), ('chill',), ('classical',), ('club',), ('comedy',), ('country',), ('dance',), ('dancehall',), ('death-metal',), ('deep-house',), ('detroit-techno',), ('disco',), ('drum-and-bass',), ('dub',), ('dubstep',), ('edm',), ('electro',), ('electronic',), ('emo',), ('folk',), ('forro',), ('french',), ('funk',), ('garage',), ('german',), ('gospel',), ('goth',), ('grindcore',), ('groove',), ('guitar',), ('hard-rock',), ('hardcore',), ('hardstyle',), ('heavy-metal',), ('hip-hop',), ('house',), ('indian',), ('indie-pop',), ('industrial',), ('jazz',), ('k-pop',), ('metal',), ('metalcore',), ('minimal-techno',), ('new-age',), ('opera',), ('party',), ('piano',), ('pop',), ('pop-film',), ('power-pop',), ('progressive-house',), ('psych-rock',), ('punk',), ('punk-rock',), ('rock',), ('rock-n-roll',), ('romance',), ('sad',), ('salsa',), ('samba',), ('sertanejo',), ('show-tunes',), ('singer-songwriter',), ('ska',), ('sleep',), ('songwriter',), ('soul',), ('spanish',), ('swedish',), ('tango',), ('techno',), ('trance',), ('trip-hop',)] Do not search for genres that are not in the list. "
        "IMPORTANT: Valid SQL columns include ONLY: id INTEGER PRIMARY KEY, artist_name TEXT NOT NULL, track_name TEXT NOT NULL, track_id TEXT NOT NULL UNIQUE, popularity INTEGER, year INTEGER, genre TEXT, danceability REAL, energy REAL, key INTEGER, loudness REAL, mode INTEGER, acousticness REAL, instrumentalness REAL, liveness REAL, valence REAL, tempo REAL "
        "Make sure to always exclude the sleep genre unless the user specifically asks for it. "
        "Given the user query, generate a complete SQL query, be as specific as you find necessary for the query. The result should always include a LIMIT 10 clause unless otherwise specified by the user."
    )

    response = queryChatGPT3(system_message, query)
    try:
        sql_query = response.content.strip()
        print(f"SQL Query from ChatGPT: {sql_query}")
        return sql_query
    except Exception as e:
        print(f"Error generating SQL query: {e}")
        return ""

def recommend_songs(query, db_path=DB_PATH):
    sql_query = parse_preferences_to_sql(query)
    if not sql_query:
        print("Failed to generate SQL query. Please try again.")
        return pd.DataFrame()

    try:
        with sqlite3.connect(db_path) as conn:
            recommendations = pd.read_sql_query(sql_query, conn)
        
        if recommendations.empty:
            print("No recommendations found. Please try again.")
        else:
            print("\nTop Song Recommendations:")
            print(recommendations[["artist_name", "track_name"]])
        
        return recommendations[["artist_name", "track_name"]]
    except Exception as e:
        print(f"Error querying database: {e}")
        return pd.DataFrame()

# Main Functionality
if __name__ == "__main__":
    print("Welcome to the Song Recommendation System!")
    user_query = input('Enter your song preferences: ')
    recommendations = recommend_songs(user_query)
