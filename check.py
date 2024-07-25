import pickle

def load_data_from_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            print(f"Loaded data from {file_path}: {data[:5]}")  # Print first 5 items for verification
            return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

movie_list = load_data_from_pickle('movie_list.pkl')
series_list = load_data_from_pickle('series_list.pkl')
anime_list = load_data_from_pickle('anime_list.pkl')


print("Series list:", series_list[:5])

