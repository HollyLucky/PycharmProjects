import tensorflow as  tf
import os
import random
import math
import sys
from PIL import Image
import numpy as np
#验证数据集
_NUM_TEST=500
#随机种子
_RANDOM_SEED=0
#数据集路径
DATASET_DIR='C:/Users/931/Desktop/初赛数据/切割图片'
#tfrecord文件存放路径
TFRECORD_DIR='C:\Users\931\PycharmProjects\CCF\savetfrecord'

#判断tfrecord文件是否存在
def _dataset_exists(dataset_dir):
    for split_name in ['train','test']:
        output_filename=os.path.join(dataset_dir,split_name+'.tfrecords')
        if not tf.gfile.Exists(output_filename):
            return False
    return True
#获取所有图片
def _get_filenames_and_classes(data_dir):
    image_filenames=[]
    for filename in os.listdir(data_dir):
        #获取文件路径
        path=os.path.join(data_dir,filename)
        image_filenames.append(path)
    return image_filenames
def int64_feature(values):
    if not isinstance(values,(tuple,list)):
        values=[values]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))
def bytes_feature(values):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))
def image_to_tfexample(image_data,label0,label1,label2,label3,label4):
    return tf.train.Example(features=tf.train.Features(feature={
        'image':bytes_feature(image_data),
        'label0': int64_feature(label0),
        'label1': int64_feature(label1),
        'label2': int64_feature(label2),
        'label3': int64_feature(label3),
        'label4': int64_feature(label4)
    }))
#将数据转为TFRecord格式