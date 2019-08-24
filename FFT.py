import pyaudio
import matplotlib.pyplot as plt
import time
import numpy as np
import os
import struct
from tkinter import TclError

fig, ax = plt.subplots(1, figsize=(15, 7))

CHUNK = 1028*4
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
x = np.arange(0,2 * CHUNK, 2)


line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes
ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(-2**15,2**15)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 256, 255])

# show the plot
plt.show(block=False)

while True:

    # binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.frombuffer(data, dtype=np.int16)

    line.set_ydata(data_np)

    # update figure canvas

    fig.canvas.draw()
    fig.canvas.flush_events()
