import pickle
import numpy as np
import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'baz.txt')

def estimate(MSZoningNums, MSSubClass, UtilitiesNums, StreetNums, SaleConditionNums, OverallQual, GarageCars, GarageArea, TotalBsmtSF, fstFlrSF, FullBath, YearBuilt, LotArea, KitchenNums, LotArea1):
    module_dir = os.path.dirname(__file__)  # get current directory
    filename = os.path.join(module_dir, 'finalized_model.sav')
    loaded_model = pickle.load(open(filename, 'rb'))
    newinput = np.array([MSZoningNums, MSSubClass, UtilitiesNums, StreetNums, SaleConditionNums, OverallQual, GarageCars, GarageArea, TotalBsmtSF, fstFlrSF, FullBath, YearBuilt, LotArea, KitchenNums, LotArea1])
    newinput = newinput.reshape(1, 15)
    predictions = loaded_model.predict(newinput)  # given unlabeled observations X, returns the predicted labels y.
    print('Input sample:', newinput)
    print('Predicted Class:', predictions)
    print(predictions)

    lk = np.exp(predictions)
    return lk[0]