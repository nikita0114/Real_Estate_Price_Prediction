import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Ensure location is lowercase to avoid case-sensitive issues
        location = location.lower()

        # Check if location is in data columns
        if location not in __data_columns:
            return f"Location '{location}' is not available in the model data."

        loc_index = __data_columns.index(location)

        # Prepare the feature array for prediction
        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        x[loc_index] = 1

        # Predict the price using the loaded model
        return round(__model.predict([x])[0], 2)
    except Exception as e:
        return f"Error during prediction: {str(e)}"

def get_location_names():
    return __location

def load_saved_artifacts():
    global __location, __data_columns, __model

    # Load column names and location data
    if __location is None:
        try:
            with open('./artifacts/columns.json', 'r') as col:
                __data_columns = json.load(col)['data_columns']
                __location = __data_columns[3:]  # Assuming first 3 columns are not locations
        except Exception as e:
            print(f"Error loading columns.json: {str(e)}")

    # Load the model from the pickle file
    if __model is None:
        try:
            with open("./artifacts/Bengaluru_House_Data.pickle", 'rb') as f:
                __model = pickle.load(f)
        except Exception as e:
            print(f"Error loading pickle model: {str(e)}")

# Debugging: Check if the artifacts are loaded correctly
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())  # Check locations
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))  # Test with a location
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))  # Test with another data
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # Test with a location not in the dataset
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # Test another location
