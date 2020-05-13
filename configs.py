# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:06:56 2020

@author: jerry
"""


# Set some parameters
IMG_WIDTH = 512
IMG_HEIGHT = 512
IMG_CHANNELS = 3

warnings.filterwarnings('ignore', category=UserWarning, module='skimage')
seed = 42
random.seed = seed
np.random.seed = seed
X_PATH = "./VOCdevkit/VOC2012/JPEGImages/"
Y_PATH = "./VOCdevkit/VOC2012/SegmentationClass/"

train_path = './train_list/train.txt'
test_path = './train_list/val.txt'

learning_rate = 1e-3
optimizer = "Adam"
epochs = 50

def get_time():
  d = datetime.today() - timedelta(hours=5)
  return(d.strftime('%Y-%m-%d %H:%M %p'))