from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)  # Allow requests from your frontend

# Route to serve the homepage (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve the blog page (blog.html)
@app.route('/blog.html')
def blog():
    return render_template('blog.html')

# Route to serve a specific article page (article.html)
@app.route('/article.html')
def article():
    return render_template('article.html')

# Route to handle the contact form submission
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
