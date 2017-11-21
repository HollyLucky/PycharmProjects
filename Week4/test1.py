import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据
mnist=input_data.read_data_sets("MNIST_data",one_hot=True)

#每个批次的大小
batch_size=100
#计算一共有多少个批次
n_batch=mnist.train.num_examples//batch_size
#命名空间
with tf.name_scope('input'):
    # 定义两个placeholder
    x = tf.placeholder(tf.float32, [None, 784],name='x-input')
    y = tf.placeholder(tf.float32, [None, 10],name='y-input')
#创建一个简单的神经网络
with tf.name_scope('layer'):
    with tf.name_scope('weights'):
        weight1=tf.Variable(tf.truncated_normal([784,10],stddev=0.1),name='W')
    with tf.name_scope('biases'):
        b1=tf.Variable(tf.zeros([10])+0.1,name='b')
    with tf.name_scope('wx_plus_b'):
        wx_plus_b=tf.matmul(x,weight1)+b1
    with tf.name_scope('softmax'):
        prediction=tf.nn.softmax(wx_plus_b)
# prediction=tf.nn.softmax(tf.matmul(x,weight1)+b)
# #二次代价函数
# loss=tf.reduce_mean(tf.square(y-prediction))
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#使用梯度下降
# train_step=tf.train.GradientDescentOptimizer(0.2).minimize(loss)
train_step=tf.train.GradientDescentOptimizer(0.2).minimize(loss)
#初始化变量
init=tf.global_variables_initializer()
#结果存放在一个布尔型列表中
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
#求准确率
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
with tf.Session() as sess:
    sess.run(init)
    writer=tf.summary.FileWriter('logs/',sess.graph)
    for e in range(1):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        test_acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        train_acc=sess.run(accuracy,feed_dict={x:mnist.train.images,y:mnist.train.labels})
        print("Iter"+str(e)+",Testing Accuracy"+str(test_acc)+",Training Accuracy"+str(train_acc))

