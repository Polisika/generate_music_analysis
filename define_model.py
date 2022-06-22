"""
Defines MuseGAN generator module.
"""


import torch

latent_dim = 128
n_pitches = 72  # number of pitches
n_measures = 4  # number of measures per sample
beat_resolution = 4  # temporal resolution of a beat (in timestep)
measure_resolution = 4 * beat_resolution
n_samples = 4
lowest_pitch = 24  # MIDI note number of the lowest pitch
beat_resolution = 4  # temporal resolution of a beat (in timestep)
programs = [0, 0, 25, 33, 48]  # program number for each track
is_drums = [True, False, False, False, False]  # drum indicator for tracks
track_names = ["Drums", "Piano", "Guitar", "Bass", "Strings"]  # name of each track
tempo = 100
n_tracks = 5  # number of tracks


class GeneraterBlock(torch.nn.Module):
    def __init__(self, in_dim, out_dim, kernel, stride):
        super().__init__()
        self.transconv = torch.nn.ConvTranspose3d(in_dim, out_dim, 
                                                  kernel, stride)
        self.batchnorm = torch.nn.BatchNorm3d(out_dim)

    def forward(self, x):
        x = self.transconv(x)
        x = self.batchnorm(x)
        return torch.nn.functional.relu(x)


class Generator(torch.nn.Module):
    """A convolutional neural network (CNN) based
    generator. The generator takes as input a latent
    vector and outputs a fake sample."""

    def __init__(self):
        super().__init__()
        self.transconv0 = GeneraterBlock(latent_dim, 256,
                                         (4, 1, 1), (4, 1, 1))
        self.transconv1 = GeneraterBlock(256, 128, (1, 4, 1), (1, 4, 1))
        self.transconv2 = GeneraterBlock(128, 64, (1, 1, 4), (1, 1, 4))
        self.transconv3 = GeneraterBlock(64, 32, (1, 1, 3), (1, 1, 1))
        self.transconv4 = torch.nn.ModuleList(
            [GeneraterBlock(32, 16, (1, 4, 1), (1, 4, 1))
             for _ in range(n_tracks)]
        )
        self.transconv5 = torch.nn.ModuleList(
            [GeneraterBlock(16, 1, (1, 1, 12), (1, 1, 12))
             for _ in range(n_tracks)]
        )

    def forward(self, x):
        x = x.view(-1, latent_dim, 1, 1, 1)
        x = self.transconv0(x)
        x = self.transconv1(x)
        x = self.transconv2(x)
        x = self.transconv3(x)
        x = [transconv(x) for transconv in self.transconv4]
        x = torch.cat([transconv(x_)
                       for x_, transconv
                       in zip(x, self.transconv5)], 1)
        x = x.view(-1, n_tracks,
                   n_measures * measure_resolution, n_pitches)
        return x
