from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import server.util # Assuming util.py is in the same directory as server.py

app = Flask(__name__, static_folder='client', template_folder='client')  # Set the client folder path
CORS(app)

util.load_saved_artifacts()  # Load model and artifacts

@app.route('/')
def serve_ui():
    return render_template('app.html')  # This will serve the frontend HTML page

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({'estimated_price': round(estimated_price, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
