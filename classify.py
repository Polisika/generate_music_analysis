import catboost
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from consts import SCALER_FILENAME, MODEL_FILENAME, DATASET_FILENAME
from save_load import save_model, save_scaler, load_dataset, load_model


def get_data(filename):
    df = load_dataset(filename)
    y = df.label
    X = df.loc[:, (df.columns != 'label') & (df.columns != "filename")]

    return X, y


def train_model(X_train, X_test, y_train, y_test):
    model = catboost.CatBoostClassifier(iterations=3346,
                                        random_seed=20220512,
                                        depth=6,
                                        l2_leaf_reg=0.1,
                                        task_type="GPU",
                                        devices='0:1',
                                        eval_metric="Accuracy")
    train_pool = catboost.Pool(data=X_train, label=y_train)
    eval_pool = catboost.Pool(data=X_test, label=y_test)
    model.fit(train_pool, eval_set=eval_pool, verbose=1000)
    return model


def train_scaler(X):
    result = preprocessing.MinMaxScaler().fit(X)
    return result


def train_model_and_scaler(filename):
    X, y = get_data(filename)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    min_max_scaler = train_scaler(X_train)
    model = train_model(X_train, X_test, y_train, y_test)

    return model, min_max_scaler


def get_current_state():
    """
    Train all before running experiments.
    All filenames in consts.py.
    :return: nothing
    """
    model, min_max_scaler = train_model_and_scaler(DATASET_FILENAME)
    save_model(model, MODEL_FILENAME)
    save_scaler(min_max_scaler, SCALER_FILENAME)


def classify(features):
    model = load_model(MODEL_FILENAME)
    genre = model.predict(features)
    prob = model.predict_proba(features)

    return genre[0], prob
