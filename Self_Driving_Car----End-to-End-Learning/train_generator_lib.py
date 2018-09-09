#train_generator library file

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

def train_generator(samples, batch_size=128, key = 1):
    num_samples = len(samples)
    if (key == 1):
        while 1: # Loop forever so the generator never terminates
            sklearn.utils.shuffle(samples)
            for offset in range(0, num_samples, batch_size):
                batch_samples = samples[offset:offset+batch_size]

                images = []
                correction_angle = []
                # Read three types of images
                for batch_sample in batch_samples:
                    name_ctr = "C:/Users/NIKHIL XAVIER/git/Self-Driving-Car/P3/CarND-Behavioral-Cloning-P3-master/data/IMG/"+batch_sample[0].split('/')[-1]
                    image_ctr = cv2.imread(name_ctr)
                    image_ctr = cv2.cvtColor(image_ctr, cv2.COLOR_BGR2RGB)
                    name_lft = "C:/Users/NIKHIL XAVIER/git/Self-Driving-Car/P3/CarND-Behavioral-Cloning-P3-master/data/IMG/"+batch_sample[1].split('/')[-1]
                    image_lft = cv2.imread(name_lft)
                    image_lft = cv2.cvtColor(image_lft, cv2.COLOR_BGR2RGB)
                    name_rgt = "C:/Users/NIKHIL XAVIER/git/Self-Driving-Car/P3/CarND-Behavioral-Cloning-P3-master/data/IMG/"+batch_sample[2].split('/')[-1]
                    image_rgt = cv2.imread(name_rgt)
                    image_rgt = cv2.cvtColor(image_rgt, cv2.COLOR_BGR2RGB)

                    angle_ctr = float(batch_sample[3])

                    # make a 0.2 correction
                    adjustment_factor = 0.20
                    angle_lft = angle_ctr + adjustment_factor
                    angle_rgt = angle_ctr - adjustment_factor

                    # Randomly include either center, left or right image
                    num = random.random()
                    if (num <= 0.33):
                        image_slt = image_ctr
                        angle_slt = angle_ctr
                        images.append(image_slt)
                        correction_angle.append(angle_slt)
                    elif (num>0.33 and num<=0.66):
                        image_slt = image_lft
                        angle_slt = angle_lft
                        images.append(image_slt)
                        correction_angle.append(angle_slt)
                    elif (num>0.66):
                        image_slt = image_rgt
                        angle_slt = angle_rgt
                        images.append(image_slt)
                        correction_angle.append(angle_slt)

                    # Flip horizontally with probability of 0.2
                    probablity_20 = random.random()
                    if (probability_20 >0.20):
                        image_flp = np.fliplr(image_slt)
                        angle_flp = -1*angle_slt
                        images.append(image_flp)
                        correction_angle.append(angle_flp)                     
                        
                X_train = np.array(images)
                y_train = np.array(angles)

                yield sklearn.utils.shuffle(X_train, y_train)
