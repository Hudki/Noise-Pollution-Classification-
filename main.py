import numpy as np
from __init__ import feature_extraction, train, predict, print_leaderboard
import __init__
import os
import threading
parent_dir = '.'
import time
import numpy
import smtplib, ssl
import glob
import datetime as datetime
import csv
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
    model = train(features, labels, epochs=200,type='cnn', print_summary=True,
        save_model=True)
    model.save('./model.h5')
while True:
    currenttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    newest = max(glob.iglob('*.wav'), key=os.path.getctime)
    pred = predict(model, './' + newest)
    print_leaderboard(pred, './data/')
    bbb = __init__.baa
    list1=[bbb,currenttime]

    with open("people.csv",'a',newline="") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(list1)
    time.sleep(4)
""".
    pred = predict(model, '//10.204.96.243/SharingPi/output.wav')
    print_leaderboard(pred, './data/')
    os.remove('//10.204.96.243/SharingPi/output.wav')
"""
