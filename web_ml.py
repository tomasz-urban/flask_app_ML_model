from flask import Flask, render_template, send_from_directory
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('heart_disease_random_forest.joblib', 'rb'))

@app.route("/")
def home_page():
    return render_template('index.html')

# @app.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)
#
# @app.route("/ML/heart_disease", methods=['POST'])
# def heart_disease():
