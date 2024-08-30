def create_diagnosis_col(df):
    # Consolidate diagnosis columns
    diagnosis_cols = df.columns[13:]
    df['DIAGNOSIS'] = df[diagnosis_cols].apply(
        lambda row: ' '.join(row.dropna().astype(str)), axis=1)
    df.drop(diagnosis_cols, axis=1, inplace=True)

    target_map = {
        'abnormal ecg': 2,
        'borderline ecg': 1,
        'normal ecg': 0
    }

    def encode_target(diagnosis):
        for key, value in target_map.items():
            if key in diagnosis.lower():  # case-insensitive matching
                return value
        return None  # Return None if no match is found

    df['DIAGNOSIS'] = df['DIAGNOSIS'].apply(encode_target)

    return df


def drop_missing_target_rows(df):
    """
    WARNING: This is a baseline and naive method. A better method
    (implemented in the future) would be to perform semi-supervised learning
    """
    df.dropna(subset=['DIAGNOSIS'], inplace=True)

    return df


def correct_smoker_col(df):
    # Smoker values = {Former, Never, Never Assessed, Some Days, Unknown,
    #                  (Smoker, Current Status Unknown), Every Day, Light Smoker,
    #                  Passive Smoke Exposure - Never Smoker, Heavy Smoker}
    # |Smoker| = 10: too much values and some label values are redundant

    categories = {
        'never': 0,
        'never assessed': 1,
        'unknown': 1,
        'former': 2,
        'smoker, current status unknown': 3,
        'light smoker': 3,
        'some days': 3,
        'passive smoke exposure - never smoker': 3,
        'every day': 4,
        'heavy smoker': 4
    }

    def encode_smoker(smoker):
        for key, value in categories.items():
            if key in smoker.lower():  # case-insensitive matching
                return value
        return None  # Return None if no match is found

    df['SMOKE'] = df['SMOKE'].apply(encode_smoker).astype('int64')

    return df
