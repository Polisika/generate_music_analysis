from functools import cache

import joblib
import pandas as pd
from catboost import CatBoostClassifier


def save_scaler(scaler, filename):
    assert ".gz" in filename
    joblib.dump(scaler, filename)


@cache
def load_dataset(filename):
    assert ".csv" in filename
    df = pd.read_csv(filename)
    return df


@cache
def load_scaler(filename):
    assert ".gz" in filename
    return joblib.load(filename)


def save_model(model, filename):
    assert ".cbm" in filename
    model.save_model(filename)


@cache
def load_model(filename):
    assert ".cbm" in filename

    from_file = CatBoostClassifier()
    from_file.load_model(filename)

    return from_file
