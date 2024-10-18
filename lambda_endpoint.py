import joblib
import pandas as pd
import sys

from model.transformers import *
from util.util import rename_columns


model = joblib.load('model/ecg_model_impr_module.pkl')


def predict(data):
    try:
        df = pd.DataFrame([data.dict()])
        df = rename_columns(df)

        prediction = model.predict(df)

        if prediction == 0:
            message = "The subject has normal ECG"
        elif prediction == 1:
            message = "The subject has borderline ECG"
        else:
            message = "The subject has abnormal ECG"

        return {"prediction": prediction[0], "message": message}
    except Exception as e:
        raise e
