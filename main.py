from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["post"])
def result():
    input_code = str(request.form.get("code"))

    if input_code == "None":
        input_code = ""

        print(str(request.form.get('cursorPosition')))

    """if request.form.get('aops') == 'ops':
        input_code = input_code[:request.form.get('cursorPosition')] + "if __name__ == '__main__':" + input_code[:request.form.get('cursorPosition')]"""

    session['input_code'] = input_code
    return redirect('/create', code=302)

@app.route('/create')
def editor():
    code = str(session.get('input_code'))

    return render_template("editor.html", code=code)

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