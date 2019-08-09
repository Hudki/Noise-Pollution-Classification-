import pyaudio  # pip install pyaudio
import numpy as np  # np varial name
import matplotlib.pyplot as plt  # pip install matplotlib
import time
from twisted.internet import task, reactor

timeout = 5 # seconds
CHANNELS = 1
RATE = 44100  # Sample Rate
CHUNK = 4098
t = 0.1  # secondsof sampling
n = RATE*t   # number of data points to read at a time

def applyfft(self): # FFT on data stream
    # FFT
    Y_k = np.fft.fft(self)[0:int(n/2)]/n # FFT function from numpy
    Y_k[1:] = 2*Y_k[1:] # need to take the single-sided spectrum only
    Pxx = np.abs(Y_k) # be sure to get rid of imaginary part
    freqvector = RATE*np.arange((n/2))/n;

    # PLOT, may need to move to main instead of having in fft function
    fig,ax = plt.subplots()
    plt.plot(freqvector,Pxx,linewidth=5)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.ylabel('Amplitude')
    plt.xlabel('Frequency [Hz]')
    plt.show()

if __name__=="__main__":
    p=pyaudio.PyAudio()  # start the PyAudio class & uses default input device
    stream=p.open(format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=False,
        frames_per_buffer=CHUNK)

    try:
        print('Press a key to close...')
        while True:  # unparsed data to see if mic works
                data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
                peak=np.average(np.abs(data))*2
                bars="█"*int(50*peak/2**16)
                print("%04d %05d %s"(peak,bars))   # prints audio level as bars

                applyfft(data)
                delay = task.LoopingCall(applyfft(stream))
                delay.start(timeout)  # start function after 5s
                reactor.run()

    except KeyboardInterrupt:  # closes on keystroke detection
        stream.stop_stream()
        stream.close()
        p.terminate()
