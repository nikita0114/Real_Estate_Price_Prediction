from flask import Flask, request, jsonify
from flask_cors import CORS
import server.util as util  # ✅ Use relative import if util.py is in the same 'server' folder

app = Flask(__name__)
CORS(app)

# Load the model and data columns when app starts
util.load_saved_artifacts()


@app.route('/get_location_names')
def get_location_names():
    try:
        locations = util.get_location_names()
        return jsonify({
            'locations': locations
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({
            'estimated_price': round(estimated_price, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ❌ Don't include app.run() — Render uses gunicorn to serve the app
