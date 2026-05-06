import pandas as pd 
import numpy as np 
# function to preprocess the data 
def preprocess_data(data):
    data = data.drop('Id' , axis = 1)
    data.fillna(data.median(numeric_only=True) , inplace = True)

    current_year = 2026

    data['HouseAge'] = ( current_year - data['YearBuilt'] ) 
    data['RemodAge'] = (current_year - data['YearRemodAdd'])
    data['GarageAge'] = ( current_year - data['GarageYrBlt'])

    data = data.drop(
        ['YearBuilt' , 'YearRemodAdd' , 'GarageYrBlt'] , axis = 1  
    )

    data = pd.get_dummies(data , drop_first = True)
    return data