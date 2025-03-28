# 🏦 Loan Default Prediction with Logistic Regression

This project predicts the likelihood of loan defaults using logistic regression. The model is deployed via a Flask API, and results are visualized in a Tableau dashboard to help stakeholders make data-driven decisions about borrower risk.

---

## 🚀 Overview
Our team worked collaboratively to clean and preprocess a dataset of accepted loan applications, train and optimize a logistic regression model, deploy the model with Flask, and create a visualization dashboard in Tableau. 

The goal is to build a functional and interpretable pipeline for predicting loan delinquency, identifying borrowers with a higher likelihood of default.

---

## 📊 Dataset
- **Source**: [LendingClub Loan Data on Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)

---

## 🧪 Machine Learning Approach
- Binary classification using **Logistic Regression**
- Preprocessing included encoding categorical variables and scaling numeric values
- Dataset split into training and testing sets (70/30)
- Evaluation metrics: `accuracy_score`, `confusion_matrix`, `classification_report` (includes precision, recall, F1-score)

---

## 📊 Tableau Dashboard
- _https://public.tableau.com/app/profile/tyquese.taplin/viz/Project4-CreditAnalysis/Story1?publish=yes_
- Visualizations show approval rates by income, loan purpose, and other features

---

## 🛠️ Technologies Used
- **Python** (Pandas, NumPy, Scikit-learn)
- **Jupyter Notebook**
- **Flask** (for API deployment)
- **Tableau** (for visualization)
- **GitHub** (for version control and collaboration)
- **HTML/CSS** (Flask frontend)
- **Microsoft PowerPoint** (for final presentation)

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

| Task Area         | Description                                                                 | Team Member |
|------------------|-----------------------------------------------------------------------------|-------------|
| **Data Cleaning** | Loaded dataset, checked for missing values, removed unnecessary columns, performed feature engineering | Cordette    |
| **Preprocessing** | Encoded categorical variables, normalized numeric features, split into train/test sets | Inshirah    |
| **Modeling**      | Trained logistic regression model                                            | Fitsum      |
| **Optimization**  | Evaluated and optimized model performance (Precision, Recall, F1-score)      | Isaiah      |
| **Visualization** | Exported predictions and built Tableau dashboard for loan risk insights      | Tyquese     |
| **Model Deployment** | Created Flask backend, loaded model, built `/predict` endpoint             | Logan       |
| **Frontend**      | Built frontend form to collect user input and display prediction results     | Maryann     |
| **Documentation** | README & Project Guide                                                      | Logan       |
| **Presentation**  | Created Google Slides deck with project visuals and summary                  | Charles     |

---

## 📄 License
_This project is for educational purposes only._
