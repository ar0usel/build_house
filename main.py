import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np

model = Sequential()
model.add(Dense(4, input_dim=2))
model.add(Activation('sigmoid'))
model.add(Dense(5, input_dim=2))
model.add(Activation('sigmoid'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
#model.load_weights('133+36epoch-dense(60)x3.h5')
sgd = SGD(lr=0.2)#Stochastic gradient descent optimizer. lr-learning rate
model.compile(loss='binary_crossentropy', optimizer=sgd)

model.fit(points, domik_np, batch_size=1, nb_epoch=1000)