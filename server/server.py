from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

util.load_saved_artifacts()


@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    print("Locations:", locations)  # Debugging line to check what locations are being returned
    response = jsonify({
        'locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])  # Ensure 'POST' method is mentioned here
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

if __name__ == "__main__":
    print("Starting Flask app...")  # Debugging line
    app.run(debug=True)  # Enable Flask Debug Mode
