from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('form_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        income = float(request.form['income'])
        loan_amount = float(request.form['loan_amount'])
        fico_low = float(request.form['fico_range_low'])
        fico_high = float(request.form['fico_range_high'])
        dti = float(request.form['dti'])

        input_features = np.array([[income, loan_amount, fico_low, fico_high, dti]])
        raw_prediction = model.predict(input_features)[0]

        # Convert raw prediction to display message (edit this logic to fit your model labels)
        if raw_prediction in ['Charged Off', 'Default', 1]:
            prediction_text = "Likely to Default"
        else:
            prediction_text = "Not Likely to Default"

        return render_template('result.html', prediction=prediction_text)

    except Exception as e:
        return f"Error during prediction: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)