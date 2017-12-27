import tensorflow as tf
from PIL import Image
import sys
im=Image.open('C:/Users/931/Desktop/初赛数据/CCF-training/1_class_8bits.png')
im1=Image.new('RGB',(190,190),(0,0,0))
box=im.copy()
box=(105,105,295,295)
region=im.crop(box)
im1.paste(region,(0,0))
im1.save('C:/Users/931/Desktop/初赛数据/切割标签/sample.png')
m=0
for i in range(190):
    img=Image.new('RGB',(1,1),(0,0,0))
    for j in range(190):
        box=im.copy()
        box=(105+i,105+j,105+i+1,105+j+1)
        region=im.crop(box)
        img.paste(region, (0, 0))
        img.save('C:/Users/931/Desktop/初赛数据/切割标签/sample' + str(m) + '.png')
        m = m + 1
        sys.stdout.write('\r>>Creating image %d/%d' % (m, 190*190))
        sys.stdout.flush()
sys.stdout.write('\n')
sys.stdout.flush()

print('生成完毕')