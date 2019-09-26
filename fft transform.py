import pyaudio
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy.fftpack import fft

import os
import struct
from tkinter import TclError

fig, ax = plt.subplots(1, figsize=(15, 7))

CHUNK = 1024*2
CHANNELS = 1
FREQUENCY =  44100 # Hz

p = pyaudio.PyAudio()

# raw data from mic
stream = p.open (
    format = pyaudio.paInt16,
    channels = CHANNELS,
    rate = FREQUENCY,
    input = True,
    output = True,
    frames_per_buffer=CHUNK # No floating values
    )
xf = np.linspace(0, FREQUENCY, CHUNK)     # frequencies (spectrum)20
ax.set_title('AUDIO SPECTRUM')

line, = ax.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes

ax.set_xlim(0, FREQUENCY / 2)

# show the plot
plt.show(block=False)

while True:

    # binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.frombuffer(data, dtype=np.int16)

    yf = fft(data_int) #perform fourier transform on int values
    line.set_ydata(np.abs(yf[0:CHUNK])  / (128 * CHUNK))

    # update figure canvas
    fig.canvas.draw()
    fig.canvas.flush_events()
