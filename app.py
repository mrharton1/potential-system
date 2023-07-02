
import numpy as np
from flask import Flask, request, render_template
import joblib
import os

# Create the Flask app and load the trained model
app = Flask(__name__)
script_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(script_dir,'model_clf.pkl')
model = joblib.load(model_path)

# Define the '/' root route to display the content from index.html
@app.route('/')
def home():
    return render_template('index2.html')


# Define the '/predict' route to:
# - Get form data and convert them to float values
# - Convert form data to numpy array
# - Pass form data to model for prediction

@app.route('/predict', methods=['POST'])
def predict():
    form_data = [float(x) for x in request.form.values()]

    postal_districts = {
        '01': 1, '02': 1, '03': 1, '04': 1, '05': 1, '06': 1,
        '07': 2, '08': 2,
        '14': 3, '15': 3, '16': 3,
        '09': 4, '10': 4,
        '11': 5, '12': 5, '13': 5,
        '17': 6,
        '18': 7, '19': 7,
        '20': 8, '21': 8,
        '22': 9, '23': 9,
        '24': 10, '25': 10, '26': 10, '27': 10,
        '28': 11, '29': 11, '30': 11,
        '31': 12, '32': 12, '33': 12,
        '34': 13, '35': 13, '36': 13, '37': 13,
        '38': 14, '39': 14, '40': 14, '41': 14,
        '42': 15, '43': 15, '44': 15, '45': 15,
        '46': 16, '47': 16, '48': 16,
        '49': 17, '50': 17, '81': 17,
        '51': 18, '52': 18,
        '53': 19, '54': 19, '55': 19, '82': 19,
        '56': 20, '57': 20,
        '58': 21, '59': 21,
        '60': 22, '61': 22, '62': 22, '63': 22, '64': 22,
        '65': 23, '66': 23, '67': 23, '68': 23,
        '69': 24, '70': 24, '71': 24,
        '72': 25, '73': 25,
        '77': 26, '78': 26,
        '75': 27, '76': 27,
        '79': 28, '80': 28}
    postal_code_input = str(form_data[0])
    postal_district = postal_districts.get(postal_code_input[:2])
    postal_region = {'9': 2, '10': 2, '11': 2, '1': 2, '2': 2, '4': 2, '6': 2, '7': 2,
                     '3': 1, '5': 1, '8': 1, '12': 1, '13': 1, '14': 1, '15': 1, '20': 1,
                     '16': 0, '17': 0, '18': 0, '19': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0,
                     '28': 0}
    form_data[0] = postal_region[str(postal_district)]

    features = [np.array(form_data)]
    prediction = model.predict(features)

    if prediction[0] == 1:
        rentpred = 'Reasonable price for location, features (within or below market rate)'
    else:
        rentpred = "Unreasonable price for location, features (negotiate with landlord)"
    return render_template('index2.html',
                           rental_prediction=rentpred)
