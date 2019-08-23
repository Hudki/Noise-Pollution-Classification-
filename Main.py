import pyaudio  # pip install pyaudio
import numpy as np  # np varial name
import scipy  # pip install scipy
import matplotlib.pyplot as plt  # pip install matplotlib

CHANNELS = 1
RATE = 44100  # Sample Rate
t = 0.1  # seconds of sampling
CHUNK = RATE*t   # number of data points to read at a time
test = 4400


def applyfft(stream): # FFT on data stream
    # FFT
    Y_k = np.fft.fft(stream)[0:int(CHUNK/2)]/CHUNK # FFT function from numpy
    Y_k[1:] = 2*Y_k[1:] # need to take the single-sided spectrum only
    Pxx = np.abs(Y_k) # be sure to get rid of imaginary part
    freqvector = RATE*np.arange((CHUNK/2))/CHUNK;
    # PLOT, may need to move to main instead of having in fft function
    fig,ax = plt.subplots()
    plt.plot(freqvector,Pxx,linewidth=5)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.ylabel('Amplitude')
    plt.xlabel('Frequency [Hz]')
    plt.show()

p=pyaudio.PyAudio()  # start the PyAudio class & uses default input device
stream=p.open(format=pyaudio.paInt16,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=False,
    frames_per_buffer=test)

try:
    print('Press a key to close...')
    while True:  # unparsed data to see if mic works
        data = np.fromstring(stream.read(test),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="▬"*int(50*peak/2**16)
        print("%04d %s"%(peak,bars))   # prints audio level as bars

except KeyboardInterrupt:  # closes on keystroke detection
    stream.stop_stream()
    stream.close()
    p.terminate()
