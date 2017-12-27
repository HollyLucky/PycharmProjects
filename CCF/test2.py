import tensorflow as tf
import os
#每个批次的大小
batch_size=50
#计算一共多少个批次
ls=os.listdir('C:/Users/931/Desktop/初赛数据/切割图片')
count=0
for i in ls:
    if os.path.isfile(os.path.join('C:/Users/931/Desktop/初赛数据/切割图片',i)):
        count=+1
n_batch=count//batch_size

#tfrecord文件存放的路径
TFRECORD_FILE='C:/Users/931/PycharmProjects/CCF/savetfrecord/test.tfrecords'

#从tfrecord读取数据
def read_and_decode(filename):
    #根据文件名生成一个队列
    filename_queue=tf.train.string_input_producer([filename])
    reader=tf.TFRecordReader()
    #返回文件名和文件
    _,serialized_example=reader.read(filename_queue)
    features=tf.parse_single_example(serialized_example,features={
        'image':tf.FixedLenFeature([],tf.string),
        'label':tf.FixedLenFeature([],tf.int64)
    })
    #获取图片
    image=tf.decode_raw(features['image'],tf.float32)
    #tf.train.shuffle_batch必须确定shape
    image = tf.reshape(image,(11,11,3))
    # image = tf.cast(image, tf.float32) / 255.0
    # image = tf.subtract(image, 0.5)
    # image = tf.multiply(image, 2.0)

    #获取label
    label=tf.cast(features['label'],tf.int64)
    return image,label
image,label=read_and_decode(TFRECORD_FILE)
image_batch,label_batch=tf.train.shuffle_batch(
    [image,label],batch_size=batch_size,capacity = 50000, min_after_dequeue=10000, num_threads=1)
#定义网络结构
def weight_variable(shape, stddev=0.02, name=None):
    # print(shape)
    initial = tf.truncated_normal(shape, stddev=stddev)
    if name is None:
        return tf.Variable(initial)
    else:
        return tf.get_variable(name, initializer=initial)

def bias_variable(shape, name=None):
    initial = tf.constant(0.0, shape=shape)
    if name is None:
        return tf.Variable(initial)
    else:
        return tf.get_variable(name, initializer=initial)
#卷积层
def conv2d(x,W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")

# 池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
#定义了两个placeholder
x=tf.placeholder(tf.float32,[None,11,11,3])
y=tf.placeholder(tf.int32,[None])
#学习率
lr=tf.Variable(0.003,dtype=tf.float32)
x_image=tf.reshape(x,[-1,11,11,3])
#初始化第一个卷积层的权值和偏置
def net(image):
    print('输入:',image.shape)
    W_conv1=weight_variable([5,5,3,32])#5*5的采样窗口，32个卷积核从一个平面抽取特征
    b_conv1=bias_variable([32])#每一个卷集核一个偏执值
    #把x_image和权值向量进行卷积，再加上偏执值，然后应用于relu激活函数
    h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
    h_pool1=max_pool_2x2(h_conv1)
    print('第一层池化后:',h_pool1.shape)
    #初始化第二个卷积层的权值和偏置
    W_conv2=weight_variable([5,5,32,64])#5*5的采样窗口，64个卷集核从32个平面抽取特征
    b_conv2=bias_variable([64])#每一个卷积核一个偏置值
    #把h_pool1和权值向量进行卷积，在加上偏置值，然后应用于relu激活函数
    h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
    h_pool2=max_pool_2x2(h_conv2)#进行max-pooling
    print('第二层池化后:',h_pool2.shape)
    return h_pool2

a = net(x_image)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)
    sess.run(tf.global_variables_initializer())
    img = sess.run(image_batch)
    feed = {x:img}
    sess.run(a,feed_dict=feed)