from pathlib import Path

import numpy as np
import pandas as pd
import pypianoroll
from mido import MidiFile

from classify import classify
from consts import MID_FILES_SUFFIX, WAV_FILES_SUFFIX
from features import get_features
from utils import (
    extract_audio,
    tracks_replace_velocity,
    generate_sample,
    get_temp_name
)


def main(f=None):
    """
    Main pipeline for classify of the MuseGAN model.
    Clears all temp files.
    :param f: file descriptor for writing results in csv file.
    :return: nothing
    """
    need_delete = (
        generate_sample(),
        get_temp_name(MID_FILES_SUFFIX),
        get_temp_name(WAV_FILES_SUFFIX),
    )
    try:
        midi_filename, normalized_filename, audio_filename = need_delete
        need_delete = need_delete[1:]
        replace_velocity_file(midi_filename, normalized_filename)
        extract_audio(normalized_filename, audio_filename)
        features = get_features(audio_filename)
        genre, probabilities = classify(features)
        if f:
            f.write(";".join([str(k)
                              for k in probabilities[0]])
                    + f";{genre[0]}\n")
    finally:
        for i in need_delete:
            Path(i).unlink(missing_ok=True)


def replace_velocity_file(midi_filename, normalized_filename):
    """
    Replace velocity for all notes in midi file.
    :param midi_filename: path to midi file.
    :param normalized_filename: path to output midi file.
    :return: nothing
    """
    midi_file = MidiFile(midi_filename)
    tracks_replace_velocity(midi_file)
    midi_file.save(normalized_filename)


def run_musegan_experiments():
    """
    Run experiments for MuseGAN models.
    Uses model_5k.pt model_40k.pt model_100k.pt
    model_200k.pt model_1200k.pt parameters.
    Clears all temp files.
    :return: nothing
    """
    basic_path = "musegan/models"
    for model_path in [
        "model_5k.pt",
        "model_40k.pt",
        "model_100k.pt",
        "model_200k.pt",
        "model_1200k.pt",
    ]:
        for i in range(1, 4):
            d = basic_path + "/" + \
                model_path.split("_", maxsplit=1)[-1].split(".")[0]
            Path(d).mkdir(exist_ok=True)
            source_filename = generate_sample(basic_path + "/" + model_path)
            filename = f"{d}/{i}_normalised.mid"
            replace_velocity_file(source_filename, filename)
            extract_audio(filename, f"{d}/{i}.wav", shrink_seconds=None)

            Path(source_filename).unlink(missing_ok=True)


def themetransformer_convert():
    """
    Extracts MP3 files for midi files in themetransformer directory.
    :return: nothing
    """
    directory = Path("themetransformer")
    for file in directory.glob("*.mid"):
        extract_audio(file, f"{file}.wav", shrink_seconds=None)


def directory_classify(dir_path):
    """
    Classify every *.wav file in the dir_path directory.
    :param dir_path: filepath to directory.
    :return: list of the dicts with genre classify results.
    """
    directory = Path(dir_path)
    result = []
    for file in directory.rglob("*.wav"):
        features = get_features(file)
        genre, probabilities = classify(features)
        result.append(
            {
                "filename": str(file).split("/")[-1],
                "genre": genre,
                **dict(zip(
                    range(0, len(probabilities[0])),
                    probabilities[0])
                ),
            }
        )

    return result


def themetransformer_classify():
    """
    Classify and represents results of the Theme Transformer classify.
    :return: nothing
    """
    dir_ = ["2days_tt", "15000k_epochs", "1_5hour_tt"]
    r = []
    for d in dir_:
        another_dir = "wav_results"
        for i in Path(d).rglob("*.mid"):
            extract_audio(str(i),
                          another_dir + f"/{str(i).split('/')[-1]}.wav")
        res = directory_classify(another_dir)
        r += res

    df = pd.DataFrame(r)
    df.to_csv("musetransformer_classify.csv")

    with open("result.md", "w") as f:
        df.drop(["filename"], axis=1).describe().to_html(f)


def musegan_get_midis(models, dir_path):
    """
    Generates for every model in models 100 random samples.
    :param models: list of filepath.
    :param dir_path: path to the existing directory for storing result.
    :return: nothing
    """
    for model in models:
        for _ in range(100):
            filename = generate_sample(model, is_random=True)
            n_f = f"{dir_path}/n_{filename}"
            replace_velocity_file(filename, n_f)
            Path(filename).unlink()


def transform_musegan_to_themetransformer(midi_filepath: str,
                                          out_midi_filepath: str):
    """
    Get input for Theme Transformer from MuseGAN output.
    :param midi_filepath: result of the MuseGAN model (generate sample).
    Strongly recommends use normalize velocity before.
    :param out_midi_filepath: filepath of the output.
    :return: nothing
    """
    midi = pypianoroll.read(midi_filepath)
    tracks = [i for i in midi.tracks if i.name in ["Guitar", "Piano"]]
    replace_names = {"Guitar": "MELODY", "Piano": "PIANO"}
    shape_tracks = (192, 128)
    for i in tracks:
        i.name = replace_names[i.name]
        i.pianoroll.resize(shape_tracks)
    theme_track = np.zeros(shape_tracks[::-1])
    theme_track[1] = np.ones((128, 1))
    theme_track = theme_track.transpose()
    theme_track = pypianoroll.Track(
        name="Theme info track", program=0,
        is_drum=False, pianoroll=theme_track
    )
    tracks.append(theme_track)
    midi.tracks = tracks
    pypianoroll.save(out_midi_filepath, midi)


if __name__ == "__main__":
    musegan_get_midis(["musegan/models/model_40k.pt"], "musegan_midis")
