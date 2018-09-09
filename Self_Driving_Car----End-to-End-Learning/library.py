#library file

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
#from data import generate_samples, preprocess
#from weights_logger_callback import WeightsLogger