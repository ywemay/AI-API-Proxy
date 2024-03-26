from flask import Flask, jsonify, make_response, request 
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)

load_dotenv()

@app.route('/api/generate', methods=['POST'])
def proxy():
    data = request.get_json()  # Assuming JSON as request body
    authorization_header = request.headers.get('Authorization')

    target_url = os.getenv('OLLAMA_URL')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization_header
    }

    response = requests.post(target_url, json=data, headers=headers)

    resp = make_response(jsonify(response.json()))
    resp.headers['Content-Type'] = 'application/json'  # Allow all origins
    resp.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    return resp

@app.before_request
def add_headers():
    if request.method == 'OPTIONS':  # Handle preflight requests (OPTIONS method) for CORS
        response = make_response(jsonify({'message': 'CORS headers allowed.'}), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'  # Supported methods
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'  # Allowed headers
        return response

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT'))
