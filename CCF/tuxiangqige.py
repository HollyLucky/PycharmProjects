import tensorflow as tf
import os
import sys
from PIL import Image
im=Image.open("C:/Users/931/Desktop/初赛数据/CCF-training/1-8bits.png")
im1=Image.new('RGB',(200,200),(0,0,0))
box=im.copy()
box=(100,100,300,300)
region=im.crop(box)
# region=region.transpose(Image.ROTATE_180)
im1.paste(region,(0,0))
im1.save('C:/Users/931/Desktop/初赛数据/切割图片/sample.png')
m=0
for i in range(190):
    img=Image.new('RGB',(11,11),(0,0,0))
    for j in range(190):
        box=im.copy()
        box=(100+i,100+j,100+i+11,100+j+11)
        region=im.crop(box)
        img.paste(region,(0,0))
        img.save('C:/Users/931/Desktop/初赛数据/切割图片/sample'+str(m)+'.png')
        m=m+1
        sys.stdout.write('\r>>Creating image %d/%d'%(m,190*190))
        sys.stdout.flush()
sys.stdout.write('\n')
sys.stdout.flush()

print('生成完毕')