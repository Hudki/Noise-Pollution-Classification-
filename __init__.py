from __future__ import absolute_import
import os
from feat_extract import parse_audio_files, parse_audio_file
import numpy as np
import models
from keras.utils import to_categorical
from keras.optimizers import SGD
import tensorflow as tf
import matplotlib.pyplot as plt
import smtplib, ssl
from twilio.rest import Client
#from models import svm, nn, cnn



def feature_extraction(data_path):
    """Parses audio files in supplied data path.
    -*- author: mtobeiyf https://github.com/mtobeiyf/audio-classification -*-
    """
    r = os.listdir(data_path)
    r.sort()
    features, labels = parse_audio_files(data_path, r)
    return features, labels

def autotext(message):
    client = Client("AC237898d9e30e666f5848dfb4ec7c03cd", "2d42cd318f0930028cc8d549a85829f0")
    client.messages.create(to="+12016008892", from_="+12054306720", body=message)


def autoemail(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "cleechibi@gmail.com"  # Enter your address
    password = "enter your password"
    receiver_email = "cl493@njit.ed"  # Enter receiver address
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def train(features, labels, type='cnn2d', num_classes=None, print_summary=False,
    save_model=False, lr=0.01, loss_type=None, epochs=50, optimizer='SGD', verbose=True):
    """Trains model based on provided feature & target data
    Options:
    - epochs: The number of iterations. Default is 50.
    - lr: Learning rate. Increase to speed up training time, decrease to get more accurate results (if your loss is 'jumping'). Default is 0.01.
    - optimiser: Default is 'SGD'.
    - print_summary: Prints a summary of the model you'll be training. Default is False.
    - loss_type: Classification type. Default is categorical for >2 classes, and binary otherwise.
    """
    labels = labels.ravel()
    if num_classes == None: num_classes =  np.max(labels, axis=0)


    model = getattr(models, type)(num_classes)
    if print_summary == True: model.summary()

    if loss_type == None:
        loss_type = 'binary' if num_classes <= 2 else 'categorical'
    model.compile(optimizer=SGD(lr=lr),
                  loss='%s_crossentropy' % loss_type,
                  metrics=['accuracy'])
    model.summary()
    if loss_type == 'categorical':
        y = to_categorical(labels - 1, num_classes=num_classes)
    else:
        y = labels -1

    x = np.expand_dims(features, axis=2)

    # Fit the model

    history = model.fit(x, y, batch_size=64, validation_data=(x,y), epochs=epochs, verbose=verbose)

    # list all data in history
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    return model

def predict(model, data_path):

    x_data = parse_audio_file(data_path)
    X_train = np.expand_dims(x_data, axis=2)
    pred = model.predict(X_train)
    return pred

def print_leaderboard(pred, data_path):

    r = os.listdir(data_path)
    r.sort()
    sorted = np.argsort(pred)
    count = 0

    for index in (-pred).argsort()[0]:
        x = round(pred[0][index]*100)
        print('%d.' % (count+1), r[index+1], str(x) + '%', '(index %s)' % index)
        count += 1
        global baa

        baa=r[index+1]

        if (r[index+1] == "Gunshot"):
            autoemail("""Subject: GUNSHOT ALERT

            Gunshot spotted on campus, please seek shelter ASAP!""")
            autotext("Gunshot ALERT")
        break
