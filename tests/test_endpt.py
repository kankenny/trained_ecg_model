import os


def test_prod_model_existence():
    base_path = os.path.join(os.getcwd(), 'model')

    file_path_prod = os.path.join(base_path, 'ecg_model_main_module.pkl')

    assert os.path.isfile(file_path_prod), f"File not found: {file_path_prod}"


def test_dev_model_existence():
    import os

    base_path = os.path.join(os.getcwd(), 'model')

    file_path_dev = os.path.join(base_path, 'ecg_model_impr_module.pkl')

    assert os.path.isfile(file_path_dev), f"File not found: {file_path_dev}"
