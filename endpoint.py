import joblib
import pandas as pd
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class ECGData(BaseModel):
    SEX: str
    WEIGHT: float
    DIABETES: str
    SMOKE: str
    VENTRICULAR_RATE: float
    ATRIAL_RATE: float
    PR_INTERVAL: float
    QRS_DURATION: float
    QT_INTERVAL: float
    QTC_CALCULATION_BEZET: float
    P_AXIS: float
    R_AXIS: float
    T_AXIS: float


mode = sys.argv[1] if len(sys.argv) > 1 else 'dev'

app = FastAPI()

if mode == 'dev':
    model = joblib.load('model/ecg_model_impr_module.pkl')
elif mode == 'prod':
    model = joblib.load('model/ecg_model_main_module.pkl')
else:
    raise EnvironmentError(f"Invalid mode: {mode}. Expected 'dev' or 'prod'.")


@app.get("/")
async def root():
    return {"message": "ECG Model Predictor"}


@app.post("/predict")
async def predict(data: ECGData):
    try:
        df = pd.DataFrame([data.dict()])

        # Rename columns to match the model's expected input
        df.rename(columns={
            'ATRIAL_RATE': 'ATRIAL RATE',
            'VENTRICULAR_RATE': 'VENTRICULAR RATE',
            'P_AXIS': 'P AXIS',
            'R_AXIS': 'R AXIS',
            'T_AXIS': 'T AXIS',
            'PR_INTERVAL': 'P-R INTERVAL',
            'QRS_DURATION': 'QRS DURATION',
            'QT_INTERVAL': 'Q-T INTERVAL',
            'QTC_CALCULATION_BEZET': 'QTC CALCULATION (BEZET)'
        }, inplace=True)

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
