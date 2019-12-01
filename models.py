import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Reshape, BatchNormalization
from keras.layers import Conv2D, GlobalAveragePooling2D, MaxPooling2D

def svm(num_classes):
    """Support vector machine.
    """
    from sklearn.svm import SVC

    return SVC(C=20.0, gamma=0.00001)

def nn(num_classes):
    """Multi-layer perceptron.
    """
    activation = 'softmax' if num_classes > 2 else 'sigmoid'
    model = Sequential()
    model.add(Dense(256, input_shape=(193, 1)))
    model.add(Activation('relu'))
    model.add(Dropout(0.6))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.6))
    model.add(Flatten())
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model

def cnn(num_classes):
    """1D Convolutional Neural Network.
    """
    from keras.layers import Embedding
    from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D

    activation = 'softmax' if num_classes > 2 else 'sigmoid'
    model = Sequential()
    model.add(Conv1D(64, 3, input_shape=(193, 1)))
    model.add(Activation('relu'))
    model.add(Conv1D(64, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling1D(3))
    model.add(Conv1D(128, 3))
    model.add(Activation('relu'))
    model.add(Conv1D(128, 3))
    model.add(Activation('relu'))
    model.add(GlobalAveragePooling1D())
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation(activation))


    return model

def cnn2d(num_classes):
    """2D Convolutional Neural Network.
    -*- ref: panotti https://github.com/drscotthawley/panotti -*-
    """
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(193,193,1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    return model
