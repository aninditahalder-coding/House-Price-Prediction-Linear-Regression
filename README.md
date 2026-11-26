# 🏡 House Price Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting house prices using Machine Learning regression algorithms.

The project uses the **California Housing Dataset** to understand the relationship between different housing features and house values. It involves building, training, evaluating, and comparing multiple regression models using Python and Scikit-learn.

Three Machine Learning algorithms are implemented:

- Linear Regression
- Ridge Regression
- Decision Tree Regression

The project also compares model performance to identify the best-performing model.

## 🎯 Objectives

- Understand the fundamentals of Machine Learning and regression algorithms.
- Explore and analyze the California Housing dataset.
- Perform data preprocessing and Exploratory Data Analysis (EDA).
- Build and train multiple regression models.
- Compare model performance using evaluation metrics.
- Identify the best-performing model.
- Save the trained model for future predictions.

## 📊 Dataset Description

The project uses the **California Housing Dataset** available through Scikit-learn.

- Total Records: 20,640
- Input Features: 8
- Target Variable: `MedHouseVal`

Important features include:

- Median Income
- Housing Median Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

## 🛠️ Tools and Technologies

- **Python** – Programming language
- **Jupyter Notebook** – Development environment
- **NumPy** – Numerical computations
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization
- **Scikit-learn** – Machine Learning algorithms and evaluation
- **Joblib / Pickle** – Model saving and loading
- **PyCharm** – IDE
- **Git and GitHub** – Version control and project hosting

## ⚙️ Project Workflow

### Task 1: Linear Regression

1. Import required Python libraries.
2. Load the California Housing dataset.
3. Perform Exploratory Data Analysis (EDA).
4. Visualize the dataset using graphs.
5. Preprocess the data.
6. Split the dataset into training and testing sets.
7. Build and train the Linear Regression model.
8. Predict house values.
9. Evaluate model performance.
10. Save the trained model.

### Task 2: Model Comparison

1. Load and prepare the California Housing dataset.
2. Build a Linear Regression model.
3. Implement Ridge Regression.
4. Implement Decision Tree Regression.
5. Train and test all three models.
6. Generate predictions using each model.
7. Evaluate models using MAE, RMSE, and R² Score.
8. Compare model performance.
9. Identify the best-performing model.
10. Save the best model using Pickle.
11. Export model comparison and prediction results into CSV files.

## 📈 Model Comparison and Evaluation

The models are evaluated using three regression metrics:

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted values.
- **RMSE (Root Mean Squared Error):** Measures prediction error while giving greater weight to larger errors.
- **R² Score:** Measures how much variation in the target variable is explained by the model.

### Model Comparison Results

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.5332 | 0.7456 | 0.5758 |
| Ridge Regression | 0.5332 | 0.7455 | 0.5759 |
| Decision Tree Regression | 0.4542 | 0.7030 | 0.6228 |

### Best Performing Model

**Decision Tree Regression** achieved the best performance among the three models.

- MAE: 0.4542
- RMSE: 0.7030
- R² Score: 0.6228

It achieved the lowest MAE and RMSE and the highest R² Score in this comparison.

## 📁 Project Structure

```text
House-Price-Prediction-Linear-Regression/
│
├── task1_ml_linearRegression.ipynb
├── AI-ML task2 model comparison.ipynb
│
├── House_price_model.pkl
├── best_house_price_model.pkl
│
├── model_comparison.csv
├── prediction_comparison.csv
│
├── House_Price_Prediction_Report.pdf
└── README.md
```

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/aninditahalder-coding/House-Price-Prediction-Linear-Regression.git
```

### 2. Navigate to the Project Folder

```bash
cd House-Price-Prediction-Linear-Regression
```

### 3. Install the Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn joblib jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

### 5. Run the Notebooks

Open and execute the notebooks:

- `task1_ml_linearRegression.ipynb`
- `AI-ML task2 model comparison.ipynb`

Run the cells sequentially to explore the implementation, predictions, and model evaluation results.

## 🚀 Future Improvements

- Experiment with additional Machine Learning algorithms.
- Perform hyperparameter tuning to improve model performance.
- Explore advanced ensemble learning techniques.
- Improve prediction accuracy through feature engineering.
- Develop a user-friendly interface for house price prediction.

## 📝 Conclusion

This project provided practical experience in implementing Machine Learning regression algorithms using Python and Scikit-learn.

Task 1 focused on building a Linear Regression model, while Task 2 extended the project by implementing and comparing Linear Regression, Ridge Regression, and Decision Tree Regression.

Based on the evaluation results, Decision Tree Regression performed best among the three models.

The project helped develop an understanding of data preprocessing, model training, prediction, evaluation, model comparison, and model saving.

## 👩‍💻 Author

**Anindita Halder**

GitHub: https://github.com/aninditahalder-coding
