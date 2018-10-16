import pickle
import numpy as np

def predict(MSZoningNums, MSSubClass, UtilitiesNums, StreetNums, SaleConditionNums, OverallQual, GarageCars, GarageArea, TotalBsmtSF, 1stFlrSF, FullBath, YearBuilt, LotArea, KitchenNums, LotArea):
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    newinput = np.array(['MSZoningNums', 'MSSubClass', 'UtilitiesNums', 'StreetNums', 'SaleConditionNums', 'OverallQual', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath', 'YearBuilt', 'LotArea', 'KitchenNums', 'LotArea'])
    newinput = newinput.reshape(1, 15)
    predictions = loaded_model.predict(newinput)  # given unlabeled observations X, returns the predicted labels y.
    print('Input sample:', newinput)
    print('Predicted Class:', predictions)
    print(predictions)

    lk = np.exp(predictions)
    return lk