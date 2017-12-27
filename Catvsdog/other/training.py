import os
import tensorflow as tf
import numpy as np
import input_data
import model
N_CLASSES=2
IMG_W=208
IMG_H=208
BATCH_SIZE=16
CAPACITY=2000
MAX_STEP=15000
learning_rate=0.0001

def run_training():
    train_dir = 'C:\\Users\\931\\PycharmProjects\\Catvsdog\\data\\train'
    logs_train_dir=''