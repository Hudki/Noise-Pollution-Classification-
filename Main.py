import pyaudio  # pip install pyaudio
import numpy as np  # np varial name
import scipy  # pip install scipy
import matplotlib  # pip install matplotlib


CHUNK = 4096  # number of data points to read at a time
RATE = 44100  # Sample Rate

p=pyaudio.PyAudio()  # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)  #uses default input device

# unparsed data to see if mic works
for i in range(20*44100/1024):  # Read multiple data
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="▬"*int(50*peak/2**16)
    print("%04d %05d %s"%(i,peak,bars))

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
