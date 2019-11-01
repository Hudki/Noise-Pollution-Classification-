import numpy as np
from __init__ import feature_extraction, train, predict, print_leaderboard
import os
import threading
parent_dir = '.'
import time

# step 1: preprocessing
if np.DataSource().exists("./feat.npy") and np.DataSource().exists("./label.npy"):
    features, labels = np.load('./feat.npy'), np.load('./label.npy')
else:
    features, labels = feature_extraction('D:/Noise Class/pyAudioClassification-master/pyaudioclassification/data')
    np.save('./feat.npy', features)
    np.save('./label.npy', labels)

# step 2: training

if np.DataSource().exists("./model.h5"):
    from keras.models import load_model
    model = load_model('./model.h5')
else:
    model = train(features, labels, epochs=2000)
    model.save('./model.h5')


# step 3: prediction
while True:
    pred = predict(model, 'D:/Noise Class/pyAudioClassification-master/pyaudioclassification/3-156907-A-15.wav')
    print_leaderboard(pred, './data/')
    time.sleep(5)
