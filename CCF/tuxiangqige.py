import tensorflow as tf
import os
from PIL import Image
im=Image.open("C:/Users/931/Desktop/初赛数据/CCF-testing/1_8bits.png")
im1=Image.new('RGB',(300,300),(0,0,0))
box=im.copy()
box=(0,0,300,300)
region=im.crop(box)
# region=region.transpose(Image.ROTATE_180)
im1.paste(region,(0,0))
im1.save('C:/Users/931/Desktop/初赛数据/切割图片/new_2.png')

print(im.format,im.size,im.mode)
im.show()
im1.show()