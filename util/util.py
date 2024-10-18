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


def delimiter_decor(fn):
    def wrapper(*args, **kwargs):
        DELIMITER = f'\n\n{"*" * 50}\n\n'
        print(DELIMITER)
        result = fn(*args, **kwargs)
        print(DELIMITER)
        return result
    return wrapper


sample_normal = {
    "summary": "A subject with a normal ECG",
    "value": {
        "SEX": "Female",
        "WEIGHT": 140.0,
        "DIABETES": "N",
        "SMOKE": "Former",
        "VENTRICULAR_RATE": 68,
        "ATRIAL_RATE": 68,
        "PR_INTERVAL": 138,
        "QRS_DURATION": 82,
        "QT_INTERVAL": 420,
        "QTC_CALCULATION_BEZET": 446,
        "P_AXIS": 60,
        "R_AXIS": 55,
        "T_AXIS": 45
    }
}

sample_abnormal = {
    "summary": "A subject with an abnormal ECG",
    "value": {
        "SEX": "Male",
        "WEIGHT": 204.59,
        "DIABETES": "Y",
        "SMOKE": "Former",
        "VENTRICULAR_RATE": 74,
        "ATRIAL_RATE": 74,
        "PR_INTERVAL": 266,
        "QRS_DURATION": 88,
        "QT_INTERVAL": 438,
        "QTC_CALCULATION_BEZET": 486,
        "P_AXIS": 37,
        "R_AXIS": -28,
        "T_AXIS": 27
    }
}
