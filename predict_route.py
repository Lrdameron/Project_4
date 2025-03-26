from flask import Blueprint, request, render_template
import pickle
import numpy as np

# Create a Blueprint object
predict_bp = Blueprint('predict_bp', __name__)

# Load your model once at the top
model = pickle.load(open('model.pkl', 'rb'))

@predict_bp.route('/predict', methods=['POST'])
def predict():
    # Update these fields to match Maryann’s form
    income = float(request.form['annual_income'])
    loan_amount = float(request.form['loan_amount'])
    # Add more fields as needed

    # Prepare input for the model
    input_features = np.array([[income, loan_amount]])  # Add all fields in proper order

    # Make prediction
    prediction = model.predict(input_features)[0]
    result = 'Approved' if prediction == 1 else 'Denied'

    return render_template('result.html', prediction=result)
