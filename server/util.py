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
        loc_index = __data_columns.index(location)
    except ValueError:
        # If the location is not found in the columns, return an error message
        return f"Location '{location}' is not available in the model data."

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    try:
        # Return the predicted price from the model
        return round(__model.predict([x])[0], 2)
    except Exception as e:
        # Catch any errors during prediction and return an error message
        return f"Error during prediction: {str(e)}"

def get_location_names():
    return __location

def load_saved_artifacts():
    global __location, __data_columns, __model

    if __location is None:
        try:
            with open('./artifacts/columns.json', 'r') as col:
                __data_columns = json.load(col)['data_columns']
                __location = __data_columns[3:]  # Assuming first 3 columns are not locations
        except Exception as e:
            print(f"Error loading columns.json: {str(e)}")

    if __model is None:
        try:
            with open("./artifacts/Bengaluru_House_Data.pickle", 'rb') as f:
                __model = pickle.load(f)
        except Exception as e:
            print(f"Error loading pickle model: {str(e)}")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
