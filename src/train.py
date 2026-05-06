from preprocess import preprocess_data
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd 
import pickle 

# load data 
train = pd.read_csv('train.csv')

y = np.log1p(train['SalePrice'])
train = train.drop('SalePrice' , axis = 1)

X = preprocess_data(train)
X_train, X_val , y_train , y_val = train_test_split(X , y , test_size = 0.2 , random_state = 42)

# train model 

model = RandomForestRegressor(
    n_estimators = 200, 
    max_depth = 15 , 
    random_state = 42
)
# train model 
model.fit(X_train , y_train)

# save model 

pickle.dump(model , open('HousePriceModel.pkl' , 'wb'))
