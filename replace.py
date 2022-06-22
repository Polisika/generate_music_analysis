"""
In model generates midi-file, in which velocity=1 or 0.
So we need make velocity make bigger.
"""

import click
import mido

from utils import tracks_replace_velocity


@click.command()
@click.option('--name', help='Midi file for replace velocity.')
@click.option('--velocity', default=50, help='If condition matches - then change velocity on this value. Default is 50.')
@click.option('--output', default="out_velocity.mid", help='File for output.')
def replace_velocity(name, velocity, output):
    """Replace velocity for track if there are only 0 and 1 values."""
    try:
        midi_file = mido.MidiFile(name)
    except IOError:
        click.echo("It's not a midi file. Check it out.")
        exit(1)
        return 1

    tracks_replace_velocity(midi_file, velocity)

    click.echo(f"Saved result in {output} file.")
    midi_file.save(output)
    exit(0)


if __name__ == '__main__':
    replace_velocity()
