from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)


# Loading the model
model = joblib.load(open('heart_disease_random_forest.joblib', 'rb'))


# Route to index.html file which is a base of website
@app.route("/")
def home_page():
    return render_template('index.html')


# Route to questionnaire (getting input from the user)
@app.route("/questionnaire", methods=['POST', 'GET'])
def questionnaire():
    return render_template('questionnaire.html')


# Route to predictions (using user input to predict heart disease)
@app.route('/predictions', methods=['POST', 'GET'])
def prediction_data():
    if request.method == 'POST':
        # Getting data from every question
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

        # Making an array from inputs
        input_array = np.array([[age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope]])

        # Making predictions on the array
        pred = model.predict(input_array)

        # Redirecting the "positive" or "negative" depending on the output
        if pred == 1:
            return redirect(url_for('positive'))
        else:
            return redirect(url_for('negative'))
    return render_template('index.html')


# Route to positive.html file - heart disease diagnosed
@app.route("/positive")
def positive():
    return render_template('positive.html')


# Route to negative.html file - heart disease not diagnosed
@app.route("/negative")
def negative():
    return render_template('negative.html')


if __name__ == "__main__":
    app.run(debug=True)
