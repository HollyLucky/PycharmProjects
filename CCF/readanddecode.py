import tensorflow as tf
TFRECORD_FILE = 'CCF/savetfrecord/test.tfrecords'
def read_and_decode(filename):
    #根据文件名生成一个队列
    filename_queue=tf.train.string_input_producer(['CCF/savetfrecord/test.tfrecords'])
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
# image_batch,label_batch=tf.train.shuffle_batch(
#     [image,label],batch_size=100,capacity = 50000, min_after_dequeue=10000, num_threads=1)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)
    sess.run(tf.global_variables_initializer())
    for i in range(10):
        print(sess.run(image))