import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy data for articles, this would normally come from a database
with open('articles.json', 'r') as f:
    ARTICLES = json.load(f)

# Route for the home page. This is the root URL ('/').
@app.route('/')
def home():
    """Renders the main homepage."""
    return render_template('index.html')

# Route for the blog listing page.
@app.route('/blog')
def blog():
    """Renders the blog page with a list of all articles."""
    return render_template('blog.html', articles=ARTICLES.items())

# Route for individual articles, using a slug to identify the article.
@app.route('/article/<slug>')
def article(slug):
    """Renders a single article page based on its slug."""
    article_data = ARTICLES.get(slug)
    if not article_data:
        # You could also render a custom 404 page here
        return "Article not found", 404
    return render_template('article.html', article=article_data)

# API endpoint for handling the contact form submission
@app.route('/api/contact', methods=['POST'])
def contact_api():
    """Handles contact form data submission."""
    # This is a placeholder. In a real app, you would process the form data,
    # save it to a database, or send an email.
    try:
        # data = request.get_json()
        # name = data.get('name')
        # email = data.get('email')
        # message = data.get('message')
        # Here you would add code to handle the message (e.g., save to a file, email it, etc.)
        print("Contact form submitted successfully.")
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error processing contact form: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # When running locally, you must create a dummy articles.json file
    # This will prevent an error when the app tries to load the articles.
    # The file is created only if it doesn't already exist.
    try:
        with open('articles.json', 'x') as f:
            f.write(json.dumps({
                "ai-and-you": {
                    "title": "Artificial Intelligence and You: A Beginner's Guide",
                    "subtitle": "Demystifying the future of AI and its role in everyday life.",
                    "author": "Jane Doe",
                    "date": "July 1, 2024",
                    "image": "https://placehold.co/800x400/FF5733/FFFFFF?text=AI+and+You",
                    "image_alt": "A simple illustration of artificial intelligence connecting with a human",
                    "content": [
                        "Artificial Intelligence (AI) is rapidly becoming a part of our daily lives, from the personalized recommendations we receive on streaming services to the voice assistants in our homes. For many, the topic can seem complex and intimidating, but understanding its basics is key to navigating the future.",
                        "At its core, AI is a branch of computer science focused on creating systems that can perform tasks that would typically require human intelligence. This includes learning, problem-solving, and decision-making. These systems don't think like humans, but they are designed to process vast amounts of data to identify patterns and make predictions.",
                        "One of the most common forms of AI is machine learning, where a computer system is given a large dataset and uses algorithms to 'learn' from the data without being explicitly programmed. This is how recommendation engines on platforms like Netflix and YouTube work, learning your preferences over time to suggest new content.",
                        "As AI becomes more integrated into our world, it's essential to consider its ethical implications. Questions about data privacy, job displacement, and algorithmic bias are at the forefront of the conversation. By becoming more aware of how AI works, we can engage in these discussions and help shape a more responsible and equitable future.",
                        "Ultimately, AI is a powerful tool with the potential to solve some of the world's most pressing challenges. By embracing it with curiosity and a critical mindset, we can harness its power for good and ensure it serves humanity in a positive way."
                    ]
                },
                "cyber-safety": {
                    "title": "Staying Safe Online: 10 Essential Cybersecurity Tips",
                    "subtitle": "Practical and simple steps to protect your digital identity from online threats.",
                    "author": "John Smith",
                    "date": "August 15, 2024",
                    "image": "https://placehold.co/800x400/3498DB/FFFFFF?text=Cyber+Safety",
                    "image_alt": "A padlock icon superimposed over a stylized network grid",
                    "content": [
                        "In today’s connected world, our digital footprint is larger than ever. With more of our lives spent online, protecting ourselves from cyber threats is no longer optional—it's a necessity. From phishing scams to malware attacks, the risks are real, but with a few simple precautions, you can significantly enhance your online security.",
                        "First, practice strong password hygiene. Use unique, complex passwords for each of your accounts. A password manager can help you manage this without having to remember dozens of different combinations. Avoid common passwords like '123456' or your birth date.",
                        "Second, be wary of phishing attempts. Phishing is a type of social engineering where attackers impersonate a trusted entity to trick you into revealing personal information. Always double-check the sender's email address and hover over links before clicking to see the true destination URL. Never provide personal details in response to an unsolicited email.",
                        "Third, keep your software updated. Software updates often include critical security patches that fix vulnerabilities attackers could exploit. This applies to your operating system, web browser, and all your applications. Enable automatic updates whenever possible.",
                        "By implementing these simple tips, you can build a strong defense against common cyber threats and enjoy a safer, more secure online experience. Your digital health is just as important as your physical health."
                    ]
                }
            }, indent=4))
    except FileExistsError:
        pass
        
    app.run(debug=True)
