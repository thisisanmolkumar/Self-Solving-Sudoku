from keras.datasets import mnist
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from random import randint
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Flatten, Dense, Dropout
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report


def showIm(n):
    plt.figure()
    plt.imshow(np.array(xTrain[n]).reshape((28, 28)), cmap='binary_r')
    plt.xlabel(f'Value: {yTrain[n]}', fontsize=18)
    plt.show()


def modelBuild(inp_shape):
    model = Sequential()

    model.add(Conv2D(32, (5, 5), padding='same', input_shape=inp_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(10))
    model.add(Activation('softmax'))
    
    return model


if __name__ == '__main__':
    (xTrain, yTrain), (xTest, yTest) = mnist.load_data()

    xTrain = xTrain.reshape((xTrain.shape[0], 28, 28, 1))
    xTest = xTest.reshape((xTest.shape[0], 28, 28, 1))

    xTrain, xTest = xTrain / 255.0, xTest / 255.0

    # showIm(randint(0, 10000))

    batch = 128
    epoch = 10
    
    le = LabelBinarizer()
    yTrain = le.fit_transform(yTrain)
    yTest = le.transform(yTest)

    model = modelBuild((28, 28, 1))
    model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

    history = model.fit(
        xTrain, yTrain,
        validation_data=(xTest, yTest),
        batch_size=batch,
        epochs=epoch,
        verbose=1)

    predictions = model.predict(xTest)
    print(classification_report(yTest.argmax(axis=1), predictions.argmax(axis=1), target_names=[str(x) for x in le.classes_]))
    
    model.save('model.h5', save_format='h5')