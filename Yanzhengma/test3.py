import tensorflow as tf
#创建一个reader来读取TFRecord文件中的样例
reader=tf.TFRecordReader()
#创建一个队列来维护输入文件列表
#tf.train.string_input_producer函数
filename_queue=tf.train.string_input_producer(['TFrecord/output.tfrecords'])
#从文件中读取一个样例。也可以使用read_up_to函数一次性读取多个样例
_,serialized_example=reader.read(filename_queue)
#解析读入的一个样例。如果需要解析多个样例，可以用parse_example函数
features=tf.parse_single_example(serialized_example,features={'image_raw':tf.FixedLenFeature([],tf.string),'pixels':tf.FixedLenFeature([],tf.int64),'label':tf.FixedLenFeature([],tf.int64)})
#tf.decode_raw可以将字符串解析成图像对应的像素数组
images=tf.decode_raw(features['image_raw'],tf.unit8)
labels=tf.cast(features['labels'],tf.int32)
pixels=tf.cast(features['pixels'],tf.int32)
sess=tf.Session()
#启动多线程处理输入数据
coord=tf.train.Coordinator()
threads=tf.train.start_queue_runners(sess=sess,coord=coord)
#每次运行可以读取TFRecord文件中的一个样例。当所有样例都读完之后，在此样例中程序会重头读取
for i in range(10):
    image,label,pixel=sess.run([images,labels,pixels])