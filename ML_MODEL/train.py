import pandas as pd
import numpy as np
import joblib 
from sklearn.linear_model import LinearRegression


df = pd.read_csv('ML_MODEL/housing.csv').iloc[:, :-1].dropna()


X = df.drop(columns=['median_house_value'])
y = df['median_house_value'].copy()


model = LinearRegression().fit(X, y)

joblib.dump(model, 'model.joblib')
