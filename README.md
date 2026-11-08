# 🏡 House Price Prediction using Linear Regression

## 📌 Project Overview

This project focuses on predicting house prices using **Linear Regression**, a supervised Machine Learning algorithm.

The project uses the California Housing dataset to understand the relationship between different housing features and house values. The model is developed using Python and Scikit-learn.

## 🎯 Objectives

- Understand the fundamentals of Linear Regression.
- Explore and analyze the California Housing dataset.
- Build and train a Machine Learning model.
- Predict house values using different input features.
- Evaluate model performance using regression metrics.

## 📊 Dataset Description

The project uses the **California Housing dataset** available through Scikit-learn.

- Total Records: 20,640
- Input Features: 8
- Target Variable: `MedHouseVal`

Some important features include:
- Median Income
- Housing Median Age
- Average Rooms
- Average Bedrooms
- Population
- Latitude and Longitude

## 🛠️ Tools and Technologies

- **Python** – Programming language
- **Jupyter Notebook** – Development environment
- **NumPy** – Numerical computations
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization
- **Scikit-learn** – Machine Learning model and evaluation
- **Joblib** – Model saving and loading
- **PyCharm** – IDE

## ⚙️ Project Workflow

1. Import required Python libraries.
2. Load the California Housing dataset.
3. Perform Exploratory Data Analysis (EDA).
4. Visualize data using graphs.
5. Preprocess the dataset.
6. Split the dataset into training and testing sets.
7. Build and train the Linear Regression model.
8. Predict house values.
9. Evaluate model performance.
10. Save the trained model using Joblib.

## 📈 Model Evaluation

The model is evaluated using the following metrics:

| Metric | Result |
|---|---:|
| MAE | 0.5332 |
| RMSE | 0.7456 |
| R² Score | 0.5758 |

The R² score indicates that the model explains approximately 57.58% of the variation in the test dataset's house values.

## 📁 Project Structure

```text
House-Price-Prediction-Linear-Regression/
│
├── main.py
├── task1_ml_linearRegression.ipynb
├── House_price_model.pkl
├── House_Price_Prediction_Report.pdf
└── README.md
```

## ▶️ How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

```bash
pip install numpy pandas matplotlib
