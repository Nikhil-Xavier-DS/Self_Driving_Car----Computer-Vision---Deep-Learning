#valid_generator library file

import numpy as np
import skimage.transform as sktransform
import random
import matplotlib.image as mpimg
import os
import cv2            
from keras.callbacks import Callback
from keras import *

import os
import shutil

import tensorflow as tf
import pandas as pd
tf.python.control_flow_ops = tf

from sklearn.model_selection import train_test_split

def valid_generator(samples, batch_size=32, key = 0):
    num_samples = len(samples)    
    if (key == 0):
        while 1:  # Loop forever so the generator never terminates
            sklearn.utils.shuffle(samples)
            for offset in range(0, num_samples, batch_size):
                batch_samples = samples[offset:offset + batch_size]

                images = []
                correction_angle = []

                #read center image
                for batch_sample in batch_samples:
                    name_ctr = "C:/Users/NIKHIL XAVIER/git/Self-Driving-Car/P3/CarND-Behavioral-Cloning-P3-master/data/IMG/" + batch_sample[0].split('/')[-1]
                    image_ctr = cv2.imread(name_ctr)
                    image_ctr = cv2.cvtColor(image_ctr, cv2.COLOR_BGR2RGB)
                    angle_ctr = float(batch_sample[3])
                    images.append(image_ctr)
                    angles.append(angle_ctr)

                X_train = np.array(images)
                y_train = np.array(correction_angle)

                yield sklearn.utils.shuffle(X_train, y_train)