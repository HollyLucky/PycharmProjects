import tensorflow as tf
#创建一个常量op
m1=tf.constant([[3,3]])
#创建一个常量op
m2=tf.constant([[2],[3]])
#创建一个矩阵乘法op，把m1和m2传入
product=tf.matmul(m1,m2)
print(product)
#定义一个会话，启动默认值
with tf.Session() as sess:
    print(sess.run(product))
