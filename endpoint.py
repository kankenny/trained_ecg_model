import joblib
import pandas as pd
import sys

from fastapi import Body, FastAPI, HTTPException
from typing import Annotated

from model.transformers import *
from util.util import ECGData, rename_columns, sample_abnormal, sample_normal


mode = sys.argv[1] if len(sys.argv) > 1 else "dev"

if mode not in ["dev", "prod"]:
    raise EnvironmentError(f"Invalid mode: {mode}. Expected 'dev' or 'prod'.")

app = FastAPI()

if mode == 'dev':
    model = joblib.load('model/ecg_model_impr_module.pkl')
else:
    model = joblib.load('model/ecg_model_main_module.pkl')


@app.get("/")
async def root():
    return {"message": "ECG Model Predictor"}


@app.post("/predict")
async def predict(data: Annotated[ECGData,
                                  Body(openapi_examples=[sample_abnormal, sample_normal])
                                  ]):
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
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")
