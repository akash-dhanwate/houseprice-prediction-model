import pandas as pd 
import numpy as np 
import pickle
from preprocess import preprocess_data

model = pickle.load(open('models/HousePriceModel.pkl' , 'rb'))
test = pd.read_csv('data/test.csv')
test_id = test['Id']
test_precessed = preprocess_data(test)
predictions = np.expm1(model.predict(test_precessed))

submission = pd.DataFrame({
    'Id' : test_id , 
    'SalePrice' : predictions

})
submission.to_csv('submission.csv' , index = False)
print('Submission file created successfully!')
