from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()
from os import getenv
import requests
app = Flask(__name__)

@app.route('/')
def home():
    ENDPOINT = getenv("URL")
    response = requests.get(ENDPOINT)
    data = response.json()
    return render_template("index.html",posts = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/')
# def home():
#     return render_template("index.html")
# @app.route('/')
# def home():
#     return render_template("index.html")