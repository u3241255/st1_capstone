import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

COLUMNS = ["Regionname_Southern Metropolitan", "Rooms", "Bathroom", "Type_h", "Type_u", "Longtitude", "Lattitude"]

def loadPredictionModel():
    with open('XGBModelFinal.pkl', 'rb') as fin:
        return pickle.load(fin)

def getModelPrediction(isSouthernMetro, rooms, bathrooms, isHouse, lat, lon):
    inputData = pd.DataFrame(data=[[isSouthernMetro, rooms, bathrooms, isHouse, not isHouse, lon, lat]], columns=COLUMNS)
    numInputs = inputData.shape[0]

    inputDataWithDummyVars = pd.get_dummies(inputData)

    X=inputDataWithDummyVars[COLUMNS].values[0:numInputs]

    model = loadPredictionModel()

    return(float(pd.DataFrame(model.predict(X), columns=['Prediction']).values[0]))
