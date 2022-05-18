from pathlib import Path

from mido import MidiFile

from classify import classify
from consts import MID_FILES_SUFFIX, WAV_FILES_SUFFIX
from features import get_features
from utils import extract_audio, tracks_replace_velocity, generate_sample, get_temp_name

if __name__ == '__main__':
    with open("result_another_model.csv", "w") as f:
        for i in range(100):
            need_delete = (generate_sample(), get_temp_name(MID_FILES_SUFFIX), get_temp_name(WAV_FILES_SUFFIX))
            try:
                midi_filename, normalized_filename, audio_filename = need_delete

                midi_file = MidiFile(midi_filename)
                tracks_replace_velocity(midi_file)
                midi_file.save(normalized_filename)
                extract_audio(normalized_filename, audio_filename)
                features = get_features(audio_filename)
                genre, probabilities = classify(features)
                f.write(";".join([str(k) for k in probabilities[0]]) + f";{genre[0]}\n")
            finally:
                for i in need_delete:
                    Path(i).unlink(missing_ok=True)

