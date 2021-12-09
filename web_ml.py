from flask import Flask, render_template, send_from_directory, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('heart_disease_random_forest.joblib', 'rb'))

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route('/predict_heart_disease', methods = ['POST'])
def prediction_data():
    age = request.form['age']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restcg = request.form['restcg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    input_array = np.array([[age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]])
    pred = model.predict(input_array)
    if pred == 1:
        return
    "According to the provided data You have a heart disease. Please contact a doctor immediately. " \
    "[NOTE: Remember that this app is only for educational purposes. " \
    "This result doesn't provide any medical indication or contraindication for treatment!"
    else:
        return
    "According to the provided data You don't have a heart disease." \
    "[NOTE: Remember that this app is only for educational purposes. " \
    "This result doesn't provide any medical indication or contraindication for treatment!"





# @app.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)
#
# @app.route("/ML/heart_disease", methods=['POST'])
# def heart_disease():
