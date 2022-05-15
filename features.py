from functools import cache

import librosa
import sklearn

from consts import SCALER_FILENAME, DATASET_FILENAME
from save_load import load_scaler, load_dataset


@cache
def get_const_features(filename):
    X = load_dataset(filename)
    length_mean = int(X.length.mean())
    rms_mean = X.rms_mean.mean()
    rms_var = X.rms_var.mean()
    sbm = X.spectral_bandwidth_mean.mean()
    sbv = X.spectral_bandwidth_var.mean()
    return length_mean, rms_mean, rms_var, sbm, sbv


def get_features(filename):
    """
    :param filename: mp3 file 30 seconds duration
    :return: ready features for genre classification
    """
    y, sr = librosa.load(filename)
    y, _ = librosa.effects.trim(y)
    spectral_rolloff = librosa.feature.spectral_rolloff(y, sr=sr)[0]
    mfccs = librosa.feature.mfcc(y, sr=sr)
    mfccs = sklearn.preprocessing.scale(mfccs, axis=1)
    spectral_centroids = librosa.feature.spectral_centroid(y, sr=sr)[0]
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    y_harm, y_perc = librosa.effects.hpss(y)
    zero_crossings = librosa.zero_crossings(y, pad=False)
    hop_length = 5000
    chromagram = librosa.feature.chroma_stft(y, sr=sr, hop_length=hop_length)
    m = []
    for i in mfccs:
        m += [i.mean(), i.std()]
    length_mean, rms_mean, rms_var, sbm, sbv = get_const_features(DATASET_FILENAME)
    features = [
        length_mean,
        chromagram.mean(),
        chromagram.std(),
        rms_mean,
        rms_var,
        spectral_centroids.mean(),
        spectral_centroids.std(),
        sbm,
        sbv,
        spectral_rolloff.mean(),
        spectral_rolloff.std(),
        zero_crossings.mean(),
        zero_crossings.std(),
        y_harm.mean(),
        y_harm.std(),
        y_perc.mean(),
        y_perc.std(),
        tempo,
        *m
    ]
    min_max_scaler = load_scaler(SCALER_FILENAME)
    result_features = min_max_scaler.transform([features])

    return result_features
