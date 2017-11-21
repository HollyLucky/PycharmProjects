import tensorflow as tf
x=tf.Variable([1,2])
y=tf.Variable([3,3])
#增加一个减法op
sub=tf.subtract(x,y)
#增加一个加法op
add=tf.add(x,y)
state=tf.Variable(0,name='counter')
new_value=tf.add(state,1)
update=tf.assign(state,new_value)
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    print(sess.run(sub))
    print(sess.run(add))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))