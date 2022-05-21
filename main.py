from pathlib import Path

from mido import MidiFile

from classify import classify
from consts import MID_FILES_SUFFIX, WAV_FILES_SUFFIX
from features import get_features
from utils import extract_audio, tracks_replace_velocity, generate_sample, get_temp_name


def main(f):
    need_delete = (generate_sample(), get_temp_name(MID_FILES_SUFFIX), get_temp_name(WAV_FILES_SUFFIX))
    try:
        midi_filename, normalized_filename, audio_filename = need_delete
        need_delete=need_delete[1:]
        replace_velocity_file(midi_filename, normalized_filename)
        extract_audio(normalized_filename, audio_filename)
        features = get_features(audio_filename)
        genre, probabilities = classify(features)
        #f.write(";".join([str(k) for k in probabilities[0]]) + f";{genre[0]}\n")
    finally:
        for i in need_delete:
            Path(i).unlink(missing_ok=True)


def replace_velocity_file(midi_filename, normalized_filename):
    midi_file = MidiFile(midi_filename)
    tracks_replace_velocity(midi_file)
    midi_file.save(normalized_filename)


if __name__ == '__main__':
    # with open("result_another_model_5000123.csv", "w") as f:
    #     for _ in range(100):
    #         main(f)
    #main(2)
    for i in range(1, 4):
        replace_velocity_file(f"{i}.mid", f"{i}_n.mid")
        extract_audio(f"{i}_n.mid", f"{i}.wav")
