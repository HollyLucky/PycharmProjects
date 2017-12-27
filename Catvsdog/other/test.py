import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import input_data
BATCH_SIZE=2
CAPACITY=256
IMG_W=208
IMG_H=208
train_dir='C:\\Users\\931\\PycharmProjects\\Catvsdog\\data\\train'
if __name__=="__main__":
    image_list, label_list=input_data.get_files(train_dir)
    image_batch,label_batch=input_data.get_batch(image_list,label_list,IMG_W,IMG_H,BATCH_SIZE,CAPACITY)
with tf.Session() as sess:
    i=0
    coord=tf.train.Coordinator()
    threads=tf.train.start_queue_runners(coord=coord)
    try:
        while not coord.should_stop() and i<1:
            img,label=sess.run([image_batch,label_batch])
            for j in np.arange(BATCH_SIZE):
                print('label:%d'%label[j])
                plt.imshow(img[j,:,:,:])
                plt.show()
            i+=1
    except tf.errors.OutOfRangeError:
            print('done!')
    finally:
        coord.request_stop()




