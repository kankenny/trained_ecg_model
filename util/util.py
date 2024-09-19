import pandas as pd
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


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Rename columns to match the model's expected input
    return df.rename(columns={
        'ATRIAL_RATE': 'ATRIAL RATE',
        'VENTRICULAR_RATE': 'VENTRICULAR RATE',
        'P_AXIS': 'P AXIS',
        'R_AXIS': 'R AXIS',
        'T_AXIS': 'T AXIS',
        'PR_INTERVAL': 'P-R INTERVAL',
        'QRS_DURATION': 'QRS DURATION',
        'QT_INTERVAL': 'Q-T INTERVAL',
        'QTC_CALCULATION_BEZET': 'QTC CALCULATION (BEZET)'
    })
