from flask_blog import app
from flask import render_template

@app.route("/")
def index():
    return render_template('home.html')

@app.get("/<int:id>")
def blog_get(id):
    return render_template('blog.html',id=id)
