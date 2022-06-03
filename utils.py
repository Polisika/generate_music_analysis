import tempfile
from functools import lru_cache

import click
import librosa
import pypianoroll
import soundfile as sf
import torch
import numpy as np
from midi2audio import FluidSynth
from pypianoroll import StandardTrack, Multitrack

from define_model import Generator, n_samples, latent_dim, measure_resolution, n_tracks, programs, is_drums, \
    track_names, n_pitches, lowest_pitch, tempo, beat_resolution


torch.manual_seed(20220524)


def tracks_replace_velocity(midi_file, velocity=50):
    tracks_start = 1
    have_signal = 1
    tracks = midi_file.tracks[tracks_start:]
    is_only_0_and_1 = {message.velocity for message in tracks[0] if message.type == "note_on"} == {0, 1}
    if not is_only_0_and_1:
        click.echo("There are many variations of the velocity. Exit.")
    for track in tracks:
        for message in track:
            if message.type == "note_on" and message.velocity == have_signal:
                message.velocity = velocity


def extract_audio(input_midi_filename, output_audio_filename, shrink_seconds=30):
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=True) as filename:
        fs = FluidSynth()
        fs.midi_to_audio(input_midi_filename, filename.name)
        # Shrink audio to 30 seconds (like need in the model)
        y, sr = librosa.load(filename, duration=shrink_seconds)
        sf.write(output_audio_filename, y, sr, subtype='PCM_24')


def vec_generator():
    vec1 = torch.randn(n_samples, latent_dim)
    vec2 = torch.randn(n_samples, latent_dim)
    vec3 = torch.randn(n_samples, latent_dim)
    while 1:
        yield vec1
        yield vec2
        yield vec3


@lru_cache(maxsize=1)
def get_generator():
    return vec_generator()


def generate_sample(model_path="model.pt", is_random=False):
    # Data
    model = torch.load(model_path)
    gen = Generator()
    gen.load_state_dict(model["generator"])
    gen.eval()
    if is_random:
        sample_latent = torch.randn(n_samples, latent_dim)
    else:
        sample_latent = next(get_generator())
    samples = gen(sample_latent).cpu().detach().numpy()
    samples = samples.transpose(1, 0, 2, 3).reshape(n_tracks, -1, n_pitches)
    tracks = []
    for idx, (program, is_drum, track_name) in enumerate(
            zip(programs, is_drums, track_names)
    ):
        pianoroll = np.pad(
            samples[idx] > 0.5,
            ((0, 0), (lowest_pitch, 128 - lowest_pitch - n_pitches))
        )
        tracks.append(
            StandardTrack(
                name=track_name,
                program=program,
                is_drum=is_drum,
                pianoroll=pianoroll
            )
        )
    tempo_array = np.full((4 * 4 * measure_resolution, 1), tempo)
    m = Multitrack(
        tracks=tracks,
        tempo=tempo_array,
        resolution=beat_resolution)

    temp_name = next(tempfile._get_candidate_names())
    filename = f"{temp_name}.mid"
    pypianoroll.write(filename, m)

    return filename


def get_temp_name(suffix):
    return next(tempfile._get_candidate_names()) + (suffix or ".deleteme")
