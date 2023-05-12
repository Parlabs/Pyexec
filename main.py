from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create')
def editor():
    return render_template("editor.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/join')
def join():
    return render_template("join.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500