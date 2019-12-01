import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

y, sr = librosa.load('output.wav')
librosa.feature.melspectrogram(y=y, sr=sr)
librosa.feature.mfcc(y=y, sr=sr)
librosa.feature.chroma_stft(y=y, sr=sr)

D = np.abs(librosa.stft(y))**2
S = librosa.feature.melspectrogram(S=D, sr=sr)
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000)
V = np.abs(librosa.stft(y))
a = librosa.effects.harmonic(y)

tonnetz = librosa.feature.tonnetz(y=a, sr=sr)
contrast = librosa.feature.spectral_contrast(S=V, sr=sr)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
chroma = librosa.feature.chroma_stft(S=V, sr=sr)

"""Mel-Frequency Spectrogram"""
plt.figure(figsize=(10, 4))
S_dB = librosa.power_to_db(S, ref=np.max)
librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000)
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram')
plt.tight_layout()


"""Mel-Frequency Cepstral Coefficients"""
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()

"""Spectral Contract"""
plt.figure()
plt.subplot(2, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(V,ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Power spectrogram')
plt.subplot(2, 1, 2)
librosa.display.specshow(contrast, x_axis='time')
plt.colorbar()
plt.ylabel('Frequency bands')
plt.title('Spectral contrast')
plt.tight_layout()

"""Tonnetz"""
plt.figure()
plt.subplot(2, 1, 1)
librosa.display.specshow(tonnetz, y_axis='tonnetz')
plt.colorbar()
plt.title('Tonal Centroids (Tonnetz)')
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.feature.chroma_cqt(a, sr=sr), y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chroma')
plt.tight_layout()

"""Chromagram"""
plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()
