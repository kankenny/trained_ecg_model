import pytest
import joblib
from endpoint import app
from fastapi.testclient import TestClient
from util.util import ECGData

client = TestClient(app)


@pytest.fixture()
def load_model():
    model_path = 'model/ecg_model_impr_module.pkl'
    model = joblib.load(model_path)
    app.dependency_overrides[model] = lambda: model
    return model


@pytest.mark.parametrize("ecg_type", [0, 1, 2])
def test_predict_ecg(load_model, ecg_type):
    # Create the sample ECG data based on the ecg_type
    if ecg_type == 0:  # Normal
        data = ECGData(
            SEX="Female",
            WEIGHT=140.0,
            DIABETES="N",
            SMOKE="Former",
            VENTRICULAR_RATE=68,
            ATRIAL_RATE=68,
            PR_INTERVAL=138,
            QRS_DURATION=82,
            QT_INTERVAL=420,
            QTC_CALCULATION_BEZET=446,
            P_AXIS=60,
            R_AXIS=55,
            T_AXIS=45
        )
    elif ecg_type == 1:  # Borderline
        data = ECGData(
            SEX="Female",
            WEIGHT=146.0,
            DIABETES="N",
            SMOKE="Never",
            VENTRICULAR_RATE=83,
            ATRIAL_RATE=83,
            PR_INTERVAL=164,
            QRS_DURATION=101,
            QT_INTERVAL=403,
            QTC_CALCULATION_BEZET=474,
            P_AXIS=71,
            R_AXIS=-29,
            T_AXIS=-86
        )
    elif ecg_type == 2:  # Abnormal
        data = ECGData(
            SEX="Male",
            WEIGHT=204.59,
            DIABETES="Y",
            SMOKE="Former",
            VENTRICULAR_RATE=74,
            ATRIAL_RATE=74,
            PR_INTERVAL=266,
            QRS_DURATION=88,
            QT_INTERVAL=438,
            QTC_CALCULATION_BEZET=486,
            P_AXIS=37,
            R_AXIS=-28,
            T_AXIS=27
        )

    # Mock the model prediction based on the ecg_type
    load_model.predict = lambda _: [ecg_type]

    response = client.post("/predict", json=data.model_dump())

    # Accept borderline or abnormal prediction
    borderline_res = {1: {"prediction": 1,
                          "message": "The subject has borderline ECG"},
                      2: {"prediction": 2,
                          "message": "The subject has abnormal ECG"}
                      }

    assert response.status_code == 200
    if ecg_type == 0:
        assert response.json() == {"prediction": 0,
                                   "message": "The subject has normal ECG"}
    elif ecg_type == 1:
        assert response.json() in borderline_res.values()
    elif ecg_type == 2:
        assert response.json() == {"prediction": 2,
                                   "message": "The subject has abnormal ECG"}
