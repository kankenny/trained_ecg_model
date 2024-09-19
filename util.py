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
