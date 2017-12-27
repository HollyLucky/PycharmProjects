#图像处理
#在之前的章节中提到一张RGB色彩模式的图像可以看成一个三维矩阵，矩阵中的每一数表示了图像上不同位置，不同颜色的亮度
#然而图像在存储时，并不是直接的记录这些矩阵中的数字，而是记录经过压缩编码之后的结果。所以要将一张图像还原成一个三维矩阵
#需要解码的过程,Tensorflow提供了对jpeg和jpg解码的编码/解码的函数
#matplotlib.pyplot是一个python的画图工具
#在这一节用这个工具来可视化经过TensorFlow处理的图像
import matplotlib.pyplot as plt
import matplotlib.image as img
import tensorflow as tf
import time
import numpy as np
import threading
#读取图像的原始数据,出错大部分是因为文件不是UTF8编码的，而系统默认采用的UTF8解码，将‘r’改成‘rb’的形式即可
image_raw_data=tf.gfile.FastGFile('picture/1.jpg','rb').read()
image=img.imread('C:/Users/931/PycharmProjects/Yanzhengma/picture/1.jpg')
with tf.Session() as sess:
    #将图像使用jepg的格式解码从而得到图像对应的三维矩阵。TensorFlow还提供了tf.image.decode_png函数对png格式的
    #图像进行解码。解码之后的结果为一个张量，在使用它的取值之前需要明确调用运行的过程
    image_data=tf.image.decode_jpeg(image_raw_data)
    # print(image_data.eval())
    # 使用pyplot工具可视化得到的图像
    # plt.imshow(image_data.eval())
    # plt.show()
    # 将数据的类型转化成实数方便下面的样例程序对图像进行处理
    image_data = tf.image.convert_image_dtype(image_data,dtype=tf.float32)
    # 将表示一张图像的三维矩阵重新按照jpeg格式编码并存入文件，打开这张图
    # 可以得到原始图像一样的图像
    # encoded_image = tf.image.encode_jpeg(image_data)
    # with tf.gfile.GFile('/output', 'wb') as f:
    #     f.write(encoded_image.eval())

    #加载原始图像，定义会话等过程和图像编码处理中代码一致，在下面的样例中就全部略去了
    #假设img_data是已经解码且进行过类型转换的图像
    #通过tf.image.resize_images函数调整图像的大小。这个函数第一个参数为原始图像
    #第二个和第三个参数为调整后图像的大小，method参数给出了调整图像的大小
    resized=tf.image.resize_images(image_data, [300, 300],)
    print(resized.get_shape())
    #TensorFlow还提供了API对图像进行裁剪或者填充。以下代码展示了通过tf.image.resize_image_with_crop_or_pad函数来调整图像大小的功能
    #通过tf.image.resize_image_with_crop_or_pad函数调整图像的大小
    #这个函数的原始图像为原始图像，后面两个参数是调整后的目标图像大小。如果原始图像的尺寸大于目标图像，那么这个函数会自动截取原始图像中居中的部分
    #如果目标图像大于原始图像，这个函数会自动在原始图像四周填充0作为背景。
    #第一个命令自动裁剪
    #第二个命令自动填充
    cropped=tf.image.resize_image_with_crop_or_pad(resized,200,200)
    padded=tf.image.resize_image_with_crop_or_pad(resized,400,400)
    # plt.imshow(cropped.eval())
    # plt.show()
    # plt.imshow(padded.eval())
    # plt.show()
    #TensorFlow还支持通过比例调整图像大小，以下代码给出了一个样例
    #通过tf.image.central_crop函数可以按比例裁剪图像。这个函数的第一个参数为原始图像，第二个为调整比例，这个比例需要是一个(0,1]的实数。
    #显示了调整之后的图像
    central_cropped=tf.image.central_crop(resized,0.5)
    # plt.imshow(central_cropped.eval())
    # plt.show()
    #上面介绍的图像裁剪函数都是截取或者填充图像中间的部分。TensorFlow也提供了tf.image.crop_to_bounding_box函数和tf.image.pad_to_bounding_box函数来裁剪或者填充给定区域的图像
    #这两个函数都要求给出的尺寸满足一定的要求，否则程序会报错。比如在使用tf.image.crop_to_bounding_box函数时，否则程序会报错。
    #比如在使用tf.image.crop_to_bounding_box函数时，TensorFlow要求提供的图像尺寸要大于目标尺寸，也就是要求原始图像能够裁剪
    #出目标图像的大小
    img_data=tf.image.crop_to_bounding_box(image_data,20,20,256,256)
    # plt.imshow(img_data.eval())
    # plt.show()
    #图像翻转
    #TensorFlow提供了一些函数来支持对图像的翻转。以下代码实现了将图像上下翻转、左右翻转以及沿对角线翻转的功能
    #将图片上下翻转
    flipped=tf.image.flip_up_down(image_data)
    #将图片左右翻转
    flipped=tf.image.flip_left_right(image_data)
    #将图片沿对角线翻转
    flipped=tf.image.transpose_image(image_data)
    #随机翻转训练图像的方式可以在零成本的情况下很大程度的缓解该问题。所以随机翻转训练图像是一种很常用的图像预处理方式
    #以一定的概率左右翻转
    flipped=tf.image.random_flip_left_right(image_data)
    #以一定的概率上下翻转
    flipped=tf.image.random_flip_up_down(image_data)

    #图像色彩调整
    #将图像的亮度-0.5
    adjusted=tf.image.adjust_brightness(image_data,0.7)
    #以下代码显示了如何调整图像的对比度
    #将图像的对比度-5，得到的图像效果
    adjusted=tf.image.adjust_contrast(image_data,0.01)
    #在[lower,upper]的范围随机调整图的对比度
    adjusted=tf.image.random_contrast(image_data,0.7,0.9)
    #以下代码显示了如何调整图像的色相
    #下面四条命令分别将色相加0.1,0.3,0.6,0.9得到的效果分别在
    adjusted=tf.image.adjust_hue(image_data,0.1)
    adjusted=tf.image.adjust_hue(image_data,0.3)
    adjusted=tf.image.adjust_hue(image_data,0.6)
    adjusted=tf.image.adjust_hue(image_data,0.9)
    #在[-max_delta,max_delta]的范围随机调整图像的色相
    #max_delta的取值在[0,0.5]之间
    adjusted=tf.image.random_hue(image_data,0.2,0.5)
    #将图像的饱和度调整
    adjusted=tf.image.adjust_saturation(image_data,0.5)
    #除了调整图像的亮度、对比度、饱和度和色相，Tensorflow还提供API来完成图像标准化的过程。
    #这个操作就是将图像上的亮度均值变为0，方差变为1
    #将代表一张图像的三维矩阵中的数字均值变为0，方差变为1.
    adjusted=tf.image.per_image_standardization(image)
    #处理标注框
    #下面这段代码展示了如何通过tf.image.draw_bounding_boxes函数在图像中加入标注框
    #将图像缩小一些，这样可视化能让标注框架更加清楚
    img_data=tf.image.resize_images(image_data,[180,267],method=1)
    #tf.image.draw_bounding_boxes函数要求图像矩阵中的数字为实数，所以需要先将图像矩阵转化为实数类型。
    #tf.image.draw_bounding_boxes函数图象的输入时一个batch的数据，也就是多张图像组成的四维矩阵，所以需要将解码之后的图像
    #矩阵加一维。
    # batched=tf.expand_dims(tf.image.convert_image_dtype(resized,dtype=tf.float32),0)
    #给出每一张图像的所有标注框,一个标注框有四个数字，分别代表[ymin,xmin,ymax,xmax]
    #注意这里给出的数字都是图像的相对位置。
    #[0.35,0.47,0.5,0.56]代表了从(63,125)到(90,150)的图像
    # boxes=tf.constant([[[0.05,0.05,0.9,0.7],[0.35,0.47,0.5,0.56]]])
    # #显示了加入了标注框的图像
    # result=tf.image.draw_bounding_boxes(batched,boxes)
    # plt.imshow(result[0].eval())
    # plt.show()
    #和随机翻转图像、随机调整颜色类似，随机截取图像上有信息含量的部分也是一个提高模型健壮性(robustness)的一种方式。
    #这样可以使训练得到的模型不受被识别物体大小的影响
    #下面的程序中展示了如何通过tf.image.sample_distorted_bounding_box函数来完成随机截取图像的过程
    # boxes=tf.constant([[[0.05,0.05,0.9,0.7],[0.35,0.47,0.5,0.56]]])
    # #可以通过提供标注框的方式来告诉随机截取图像的算法哪些部分是“有信息量”的
    # begin,size,bbox_for_draw=tf.image.sample_distorted_bounding_box(tf.shape(image_data),bounding_boxes=boxes)
    # #通过标注框可视化随机截取得到的图像。
    # batched=tf.expand_dims(tf.image.convert_image_dtype(img_data,tf.float32),0)
    # image_with_box=tf.image.draw_bounding_boxes(batched,bbox_for_draw)
    # #截取随机出来的图像。
    # distorted_image=tf.slice(img_data,begin,size)
    # plt.imshow(distorted_image[0].eval())
    # plt.show()
    #多线程输入数据处理框架
    #指定原始数据的文件
    #创建文件列表队列
    #从文件中读取数据
    #数据预处理
    #整理成Batch作为神经网络输入
    #在Tensorflow中，队列不仅是一种数据结构，他更提供了多线程机制。
    #队列也是多线程输入数据处理框架的基础
    #Tensorflow提供了tf.train.string_input_producer函数来有效管理原始输入文件列表。
    #这个流程将处理好的单个训练数据整理成训练数据，这些batch就可以作为数据输入
    #将介绍tf.train.shuffle_batch_join和tf.train.shuffle_batch函数，并比较不同函数的多线程并行方式
    #队列与多线程
    #在TensorFlow中，队列和变量类似，都是计算图上有状态的节点。其他的计算节点可以修改他们的状态。对于变量，可以通过赋值操作修改变量的取值
    #对于队列，修改队列状态的操作主要有Enqueue、EnqueueMany和Dequeue。
    #创建一个先进先出队列，指定队列中最多可以保存两个元素，并指定类型为整数
# q=tf.FIFOQueue(2,'int32')
#     #使用enqueue_many函数来初始化队列中的元素，和变量初始化类似，在使用队列之前
#     #需要明确的调用这个初始化过程
# init=q.enqueue_many(([0,10],))
#     #使用Dequeue函数将队列中的第一个元素出队列，这个元素的值将被存在变量x中。
# x=q.dequeue()
#     #将得到的值加1
# y=x+1
#     #将加1后的值在重新加入队列
# q_inc=q.enqueue([y])
# with tf.Session() as sess:
#         #运行初始化队列的操作
#     init.run()
#     for _ in range(5):
#             #运行q_inc将执行数据出列、出队的元素+1、重新加入队列的整个过程
#         v,_=sess.run([x,q_inc])
#             #打印出队元素的取值
#         print(v)
#TensorFLow中提供了FIFOQueue和RandomShuffleQueue两种队列。FIFOQueue是一个先入先出的队列
#RandomShuffleQueue会将队列中的元素打乱，每次出队列操作得到的是从当前队列所有元素中随机选择一个
#TensorFlow提供了tf.Coordinator和tf.QueueRunner两个类来来完成多线程协同的功能。
#tf.Coordinator主要用于协同多个线程一起停止，并提供了should_stop、request_stop、和join三个函数
#在启动线程之前，需要声明一个tf.Coordinator类，并将这个类传入每一个创建的线程中。启动的线程需要一直查询
#tf.Coordinator类中提供的should_stop函数，当这个函数的返回值为True时，则当前线程也需要退出。每一个启动的
#线程都可以通过调用request_stop函数来通知其他线程退出。当某一个线程调用request_stop函数之后，should_stop函数的
#返回值将被设置为True.这样其他的线程就可以同时终止了
#线程中运行的程序，这个程序每隔1秒判断是否需要停止并打印自己的ID
def MyLoop(coord,worker_id):
    #使用tf.Coordinator类提供的协同工具判断当前线程是否需要停止
    while not coord.should_stop():
        #随机停止所有的线程
        if (np.random.rand()<0.1):
            print('Stop from id:%d\n'%worker_id)
            #调用coord.request_stop()函数来通知其他线程停止
            coord.request_stop()
        else:
            #打印当前线程的ID
            print('Working on id:%d\n'% worker_id)
            #暂停1秒
            time.sleep(1)
#声明一个tf.train.Coordinator类来协同多个线程
coord=tf.train.Coordinator()
#声明创建5个线程
threads=[threading.Thread(target=MyLoop,args=(coord,i,)) for i in range(5)]
#启动所有的线程
for t in threads:t.start()
#等待所有线程退出
coord.join(threads)







