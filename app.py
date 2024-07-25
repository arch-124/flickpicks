from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Function to load data from a pickle file
def load_data_from_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            print(f"Loading data from {file_path}")
            data = pickle.load(file)
            print(f"Loaded data: {data[:5]}")  # Print first 5 items for verification
            return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

# Load data from the pickle files
movie_list = load_data_from_pickle('movie_list.pkl')
series_list = load_data_from_pickle('series_list.pkl')
anime_list = load_data_from_pickle('anime_list.pkl')
movie_similarity_list = load_data_from_pickle('similary_list.pkl')
series_similarity_list = load_data_from_pickle('similary2_list.pkl')
anime_similarity_list = load_data_from_pickle('similary1_list.pkl')

if movie_list is None or series_list is None or anime_list is None or movie_similarity_list is None or series_similarity_list is None or anime_similarity_list is None:
    print("Error loading data. Please check the pickle files.")
    exit(1)

# Convert lists to DataFrames
movie_df = pd.DataFrame(movie_list)
series_df = pd.DataFrame(series_list)
anime_df = pd.DataFrame(anime_list)

# Print the titles of the movies, series, and anime for verification
print("Movie titles:", movie_df['title'].tolist()[:5])
print("Series titles:", series_df['title'].tolist()[:5])
print("Anime titles:", anime_df['title'].tolist()[:5])

def recommend(content_type, title):
    try:
        if content_type == 'movie':
            df = movie_df
            similarity_list = movie_similarity_list
        elif content_type == 'series':
            df = series_df
            similarity_list = series_similarity_list
        elif content_type == 'anime':
            df = anime_df
            similarity_list = anime_similarity_list
        else:
            return []

        print(f"DataFrame for {content_type}:")
        print(df.head())  # Print first 5 rows of the DataFrame

        print(f"Searching for title: {title}")
        if title in df['title'].values:
            index = df[df['title'] == title].index[0]
            print(f"Found index for title '{title}': {index}")
        else:
            print(f"Title '{title}' not found in DataFrame.")
            return []

        print(f"Similarity list length: {len(similarity_list)}")
        print(f"Similarity list sample (first 5 rows): {similarity_list[:5]}")
        
        if index < len(similarity_list):
            print(f"Similarity row for index {index}: {similarity_list[index]}")
            distances = sorted(list(enumerate(similarity_list[index])), reverse=True, key=lambda x: x[1])
            print(f"Distances: {distances[:10]}")  # Print first 10 distances for verification

            df_length = len(df)
            print(f"DataFrame length: {df_length}")

            # Handle out-of-bounds indices
            valid_indices = [i[0] for i in distances[1:6] if i[0] < df_length]
            print(f"Valid indices: {valid_indices}")

            recommendations = [df.iloc[i]['title'] for i in valid_indices]
            print(f"Recommendations: {recommendations}")
            return recommendations
        else:
            print(f"Index {index} is out of bounds for similarity list of length {len(similarity_list)}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movie_list)

@app.route('/series', methods=['GET'])
def get_series():
    return jsonify(series_list)

@app.route('/anime', methods=['GET'])
def get_anime():
    return jsonify(anime_list)

@app.route('/similarities', methods=['GET'])
def get_similarities():
    return jsonify({"movies": movie_similarity_list, "series": series_similarity_list, "anime": anime_similarity_list})

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    input = json.loads(request.data)
    title = input.get('title')
    content_type = input.get('type')
    if title and content_type:
        recommendations = recommend(content_type, title)
        if recommendations:
            return jsonify(recommendations)
        else:
            return jsonify({"error": "Content not found"}), 404
    return jsonify({"error": "No title or content type provided"}), 400

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
