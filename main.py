# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:07:55 2020

@author: jerry
"""

import os
import sys
import random
import warnings

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from tqdm import tqdm
from itertools import chain
from skimage.io import imread, imshow, imread_collection, concatenate_images
from skimage.transform import resize
from skimage.morphology import label

from keras.models import Model, load_model
from keras.layers import Input
from keras.layers.core import Dropout, Lambda
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import backend as K
import tensorflow as tf
from datetime import datetime, timedelta
from keras.optimizers import *
import configs
import data_loader
import model


def fit_model(epochs, batch_size):
  earlystopper = EarlyStopping(patience=5, verbose=1)
  checkpointer = ModelCheckpoint('model-dsbowl2018-1.h5', verbose=1, save_best_only=True)
  results = model.fit(X_train, Y_train, validation_split=0.1, batch_size=batch_size, epochs=epochs, 
                callbacks=[earlystopper, checkpointer])
  return(results)
  

start = datetime.now()
  
model = unet(learning_rate , optimizer)
results = fit_model(epochs,50)

end = datetime.now()
time = end-start

get_performance()