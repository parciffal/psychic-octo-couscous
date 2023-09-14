from app import app
from flask import render_template


#
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
def index():
    return render_template("index.html")