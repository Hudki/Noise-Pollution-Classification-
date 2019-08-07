import pyaudio  # pip install pyaudio
import numpy as np  # np varial name
import scipy  # pip install scipy
import matplotlib.pylot as plt  # pip install matplotlib

CHANNELS = 1
CHUNK = 4096  # number of data points to read at a time
RATE = 44100  # Sample Rate

p=pyaudio.PyAudio()  # start the PyAudio class & uses default input device
stream=p.open(format=pyaudio.paInt16,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=False,
    frames_per_buffer=CHUNK)


while True:
    try:  # unparsed data to see if mic works
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="▬"*int(50*peak/2**16)
        print("%04d %05d %s"%(peak,bars))   # prints audio level as bars

    except KeyboardInterrupt:  # closes on keystroke detection
        stream.stop_stream()
        stream.close()
        p.terminate()
