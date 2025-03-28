from flask import Blueprint, request, render_template
import pickle
import numpy as np

predict_bp = Blueprint('predict_bp', __name__)

# Load the trained model once
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Example inputs — change these to match what your model expects
        income = float(request.form['annual_income'])
        loan_amount = float(request.form['loan_amount'])
        credit_score = float(request.form['credit_score'])
        age = float(request.form['age'])
        loan_purpose = request.form['loan_purpose']  # categorical

        # Simple encoding (this is just placeholder logic)
        loan_purpose_encoded = 1 if loan_purpose == 'home' else 0

        # Final input features — update this list to match your training order
        input_features = np.array([[income, loan_amount, credit_score, age, loan_purpose_encoded]])

        # Prediction
        prediction = model.predict(input_features)[0]
        result = 'Approved' if prediction == 1 else 'Denied'

        return render_template('result.html', prediction=result)

    except Exception as e:
        return f"Error: {e}", 400
