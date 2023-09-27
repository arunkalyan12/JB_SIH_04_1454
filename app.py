import joblib
import numpy as np
from flask import Flask, request, render_template
import joblib
from feature import FeatureExtraction_main
import pandas as pd

app = Flask(__name__)

# Load saved model
model = joblib.load('model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from post request
    url = request.form['url']
    # Prepare data
    status = FeatureExtraction_main(url)
    status = np.array(status).reshape(1, -1)


    # Predict target values
    y_pred = model.predict(status)

    # Convert prediction to label

    prediction = 'Phishing' if y_pred[0] == 0 else 'Legitimate'

    return render_template('index.html', prediction_text='{}'.format(prediction), url=url)


if __name__ == '__main__':
    app.run(port=5202, debug=True)