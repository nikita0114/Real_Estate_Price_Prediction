import json
import pickle
import numpy as np
import os

__location = None
__data_columns = None
__model = None

# Base directory where util.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to artifacts inside the server folder
ARTIFACTS_PATH = os.path.join(BASE_DIR, 'artifacts')

def get_estimated_price(location, sqft, bhk, bath):
    try:
        location = location.lower()
        loc_index = __data_columns.index(location)
    except ValueError:
        return f"Location '{location}' not found in model data."

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    try:
        return round(__model.predict([x])[0], 2)
    except Exception as e:
        return f"Error during prediction: {str(e)}"

def get_location_names():
    return __location

def load_saved_artifacts():
    global __location, __data_columns, __model

    if __location is None:
        try:
            with open(os.path.join(ARTIFACTS_PATH, 'columns.json'), 'r') as col:
                __data_columns = json.load(col)['data_columns']
                __location = __data_columns[3:]  # Skipping sqft, bath, bhk
        except Exception as e:
            print(f"Error loading columns.json: {str(e)}")

    if __model is None:
        try:
            with open(os.path.join(ARTIFACTS_PATH, 'Bengaluru_House_Data.pickle'), 'rb') as f:
                __model = pickle.load(f)
        except Exception as e:
            print(f"Error loading model pickle: {str(e)}")

if __name__ == '__main__':
    load_saved_artifacts()
    print("Locations loaded:", get_location_names())
    print("Sample Prediction:", get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
