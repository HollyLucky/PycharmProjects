import tensorflow as tf
import os
import random
import math
import sys
from PIL import Image
import numpy as np
#验证数据集
_NUM_TEST=36100
#随机种子
_RANDOM_SEED=0
#数据集路径
DATASET_DIR='C:/Users/931/Desktop/初赛数据/切割图片'
LABEL_DIR='C:/Users/931/Desktop/初赛数据/切割标签'
#tfrecord文件存放路径
TFRECORD_DIR='C:/Users/931/PycharmProjects/CCF/savetfrecord'
#判断tfrecord文件是否存在
def _dataset_exists(dataset_dir):
    for split_name in ['train','test']:
        output_filename=os.path.join(dataset_dir,split_name+'.tfrecords')
        if not tf.gfile.Exists(output_filename):
            return False
    return True
def _get_filenames_and_classes(dataset_dir,label_dir):
    photo_filenames = []
    label_filenames=[]
    for filename in os.listdir(dataset_dir):
        # 获取文件路径
        path = os.path.join(dataset_dir, filename)
        photo_filenames.append(path)
    for filename in os.listdir(label_dir):
        path=os.path.join(label_dir,filename)
        label_filenames.append(path)
    return photo_filenames,label_filenames
def int64_feature(values):
    if not isinstance(values, (tuple, list)):
        values = [values]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def bytes_feature(values):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))
def image_to_tfexample(image_data, label0):
    # Abstract base class for protocol messages.
    return tf.train.Example(features=tf.train.Features(feature={
        'image': bytes_feature(image_data),
        'label0': int64_feature(label0)
    }))
# 把数据转为TFRecord格式
def _convert_dataset(photo_filenames,label_filenames):
    with tf.Session() as sess:
        output_filename = os.path.join(TFRECORD_DIR, 'test.tfrecords')
        with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
            for i, filename in enumerate(photo_filenames):
                try:
                    sys.stdout.write('\r>> Converting image %d/%d' % (i + 1, len(photo_filenames)))
                    sys.stdout.flush()

                    # 读取图片
                    image_data = Image.open(filename)
                    # 根据模型的结构resize
                    image_data = image_data.resize((11,11))
                    # 灰度化
                    image_data = np.array(image_data.convert('L'))
                    # 将图片转化为bytes
                    image_data = image_data.tobytes()


                    # 获取label
                    label = Image.open(label_filenames[i])
                    label=label.tobytes()





                    # 生成protocol数据类型
                    example = image_to_tfexample(image_data, label[0])
                    tfrecord_writer.write(example.SerializeToString())

                except IOError as e:
                    print('Could not read:', filename)
                    print('Error:', e)
                    print('Skip it\n')
    sys.stdout.write('\n')
    sys.stdout.flush()


# 判断tfrecord文件是否存在
if _dataset_exists(TFRECORD_DIR):
    print('tfcecord文件已存在')
else:
    # 获得所有图片
    photo_filenames,label_filenames = _get_filenames_and_classes(DATASET_DIR,LABEL_DIR)

    # 数据转换
    _convert_dataset(photo_filenames,label_filenames)
    print('生成完毕')
