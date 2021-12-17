from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load(open('heart_disease_random_forest.joblib', 'rb'))

@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/questionnaire", methods=['POST', 'GET'])
def questionnaire():
    return render_template('questionnaire.html')


@app.route('/predictions', methods=['POST', 'GET'])
def prediction_data():
    if request.method == 'POST':
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

        input_array = np.array([[age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope]])

        pred = model.predict(input_array)
        if pred == 1:
            return redirect(url_for('positive'))
        else:
            return redirect(url_for('negative'))
    return render_template('index.html')


@app.route("/positive")
def positive():
    return render_template('positive.html')


@app.route("/negative")
def negative():
    return render_template('negative.html')


# if __name__ == "__main__":
#     app.run(debug=True)