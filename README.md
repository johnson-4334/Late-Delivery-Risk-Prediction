# 🚚 Machine Learning-Based Late Delivery Risk Prediction in Global Supply Chain Operations

## 📌 Project Overview

This project predicts whether a customer order is likely to be delivered late using Machine Learning. The objective is to help logistics companies identify high-risk shipments in advance so they can take preventive actions and improve customer satisfaction.

This project was developed as part of the **Unified Mentor Data Science Internship**.

---

## 📊 Problem Statement

Late deliveries increase operational costs, reduce customer satisfaction, and impact business performance.

The goal of this project is to build a predictive model that classifies orders as:

- On-Time Delivery (0)
- Late Delivery (1)

using historical supply chain data.

---

## 🗂 Dataset

**Dataset:** APL Logistics Supply Chain Dataset

The dataset contains information such as:

- Shipping Mode
- Market
- Customer Segment
- Product Details
- Sales
- Profit
- Shipping Schedule
- Geographic Information
- Order Details

**Target Variable**

- `Late_delivery_risk`
  - 0 = On-Time Delivery
  - 1 = Late Delivery

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 📈 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Building
7. Model Evaluation
8. Model Comparison
9. Streamlit Deployment

---

## 🤖 Machine Learning Models

The following models were implemented:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| Logistic Regression | 71.41% | 78.68% | 65.65% | 71.58% | 78.21% |
| Random Forest | **76.62%** | **87.31%** | **67.11%** | **75.89%** | **87.31%** |
| XGBoost | 70.35% | 85.12% | 55.66% | 67.31% | 76.39% |

### Best Model

✅ Random Forest Classifier

---

## 📌 Key Features

- Data Cleaning
- Feature Engineering
- Risk Prediction
- Feature Importance Analysis
- Model Comparison
- Streamlit Web Application

---

## 🚀 Streamlit Application

The Streamlit application provides:

- Late Delivery Prediction
- Risk Probability
- User-friendly Interface
- Interactive Inputs

---

## 📂 Project Structure

```
Late-Delivery-Risk-Prediction/
│
├── app.py
├── Late_Delivery.ipynb
├── requirements.txt
├── README.md
└── dataset/
```

---

## ▶️ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📌 Results

The Random Forest model achieved the best performance and was selected as the final deployment model for predicting late delivery risk.

---

## 👨‍💻 Author

**Johnson Kosetti**

B.Sc. Data Science

Aspiring Data Analyst | Machine Learning Enthusiast

---

## 📜 License

This project is developed for educational and internship purposes.
