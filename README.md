# 🧠 Loan Approval Predictor

A machine learning project to predict whether a loan application should be approved based on financial and demographic data.

---

## 🚀 Overview
This project simulates a simplified loan approval system using historical LendingClub data. The team built a logistic regression model, created data visualizations in Tableau, and developed a Flask web application to serve predictions.

---

## 📊 Dataset
- **Source**: [LendingClub Loan Data on Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)
- **Records**: The original dataset contains over 1 million loan applications.  
  _(Note: We are using a cleaned and trimmed subset for this project. Final count will be updated.)_
- **Key Fields**: 

---

## 🧪 Machine Learning Approach
- Binary classification using **Logistic Regression**
- Preprocessing included encoding categorical variables and scaling numeric values
- Dataset split into training and testing sets (80/20)
- Evaluation metrics: `accuracy_score`, `confusion_matrix`, `classification_report` (includes precision, recall, F1-score)

---

## 💻 Running the App
**To run locally:**
```bash
git clone <your-repo-url>
cd loan-approval-predictor
pip install -r requirements.txt
python app.py
```

_Note: Update with final model file and form route if needed._

---

## 📊 Tableau Dashboard
- _[Placeholder for Tableau Public link or embed]_
- Visualizations show approval rates by income, loan purpose, and other features

---

## 🛠️ Technologies Used
- Python (Pandas, Scikit-learn, Flask)
- Jupyter Notebook
- Tableau
- HTML/CSS (for Flask UI)
- GitHub for version control

---

## 👥 Team Members & Roles
- **Cordette** – Data Loading & Exploration
- **Inshirah** – Preprocessing (Encoding, Scaling, Splitting)
- **Fitsum** – Model Training
- **Isaiah** – Model Evaluation
- **Tyquese** – Visualization (Export & Tableau)
- **Logan** – Flask Backend & Documentation
- **Maryann** – Flask Frontend
- **Charles** – Slide Deck & Presentation

---

## 📁 Folder Structure _(to be updated)_
```bash
📦 loan-approval-predictor
 ┣ 📂 static
 ┣ 📂 templates
 ┣ 📜 app.py
 ┣ 📜 model.pkl
 ┣ 📜 notebook.ipynb
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
```

---

## 📄 License
_This project is for educational purposes only._
