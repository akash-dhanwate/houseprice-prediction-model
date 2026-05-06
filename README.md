# House Price Prediction using Machine Learning

## Project Overview
This project predicts house prices using machine learning techniques on the Kaggle House Prices dataset.

The workflow includes:
- Data preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Random Forest Regression
- Cross-validation
- Feature importance analysis

---

## Dataset
Dataset: Kaggle House Prices - Advanced Regression Techniques

Training data contains housing features and sale prices.
Test data contains unseen houses for prediction.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## Feature Engineering
Created additional meaningful features:
- HouseAge
- GarageAge
- RemodAge
- TotalSF
- TotalBath

---

## Model Used
Random Forest Regressor

Reason:
Random Forest handles:
- non-linear relationships
- feature interactions
- tabular data effectively

---

## Model Performance
- R² Score: ~0.89
- RMSE: ~28,700
- Kaggle Public Score: 0.14688

---

## Key Insights
Top features influencing house prices:
- Overall Quality
- Living Area
- Basement Size
- Garage Capacity

---

## Project Structure

```text
house-price-prediction/
│
├── data/
├── notebooks/
├── src/
├── models/
├── README.md
└── requirements.txt
```

---

## Future Improvements
- XGBoost implementation
- Streamlit deployment
- Ensemble models
- Hyperparameter tuning
