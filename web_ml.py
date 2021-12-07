from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)
