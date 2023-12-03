from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/0fe28898aba951eba567")
blogs = response.json()

@app.route('/')
def home():
    return render_template('index.html', blogs=blogs)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
