from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from your frontend

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    print(f"Contact form: {name} <{email}>: {message}")
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
