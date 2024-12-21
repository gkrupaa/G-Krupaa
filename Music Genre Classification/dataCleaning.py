from utils.data_preprocessing import *

# Load data
df = pd.read_csv('data/dataset2.csv')

# Drop unnecessary columns
df.drop([df.columns[0], 'track_id','artists','album_name','track_name'], axis=1, inplace=True)

# Specify the genres you want to keep
selected_genres = ['pop', 'rock', 'heavy-metal' 'hip hop', 'jazz', 'classical', 'country']  # Example genres

# Filter the DataFrame to keep only the selected genres
df = df[df['genre'].isin(selected_genres)]

# Fill missing values with the mean
columsToFillNA = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']
df_filled_mean = handle_missing_values(df, strategy="fill", fill_value="mean", columns=columsToFillNA)
df = df_filled_mean

# One-hot encode the 'explicit' column
df['explicit'] = df['explicit'].astype(int)

# Scale the data 
normalizeData(df, columns=df.columns[0:-1])

# Write the cleaned data to a new CSV file
write2csv(df, 'dataset2cleaned.csv')

print("Data cleaning and preprocessing complete.")


