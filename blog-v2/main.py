from flask import Flask, render_template, request
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
    print(data)
    return render_template("index.html",posts = data)
    

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    ENDPOINT = getenv('URL')
    response = requests.get(ENDPOINT)
    posts = response.json()
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "Post not found", 404

@app.route('/submit',methods = ["POST"])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get("phone")
    message = request.form.get("message")
    return f"name:{name} email:{email}"

if __name__ == "__main__":
    app.run(debug=True)


