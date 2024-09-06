import joblib
from model.transformers import *

model = joblib.load('model/ecg_model.pkl')
print(model)
