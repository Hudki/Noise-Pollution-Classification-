import pyaudio  # pip install pyaudio
import numpy as np  #np varial name

CHUNK = 4096  # number of data points to read at a time
RATE = 44100  # time resolution of the recording device (Hz)

stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)  #uses default input device

# unparsed data to see if mic works
for i in range(10):  #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(data)

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
