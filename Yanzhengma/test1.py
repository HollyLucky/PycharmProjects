from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:  
# font = ImageFont.truetype('Arial.ttf', 36)
font = ImageFont.truetype('C:/Users/931/AppData/Local/Programs/Python/Python35/arial.ttf', 36)
# 创建Draw对象:  
draw = ImageDraw.Draw(image)
# 填充每个像素:  
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
        # 输出文字:
# 创建一个元组存在验证码  
tup = ''
for t in range(4):
    # 随机字母
    sj = rndChar()
    draw.text((60 * t + 10, 10), sj, font=font, fill=rndColor2())
    tup += sj
# 模糊:  
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');
# 遍历验证码
for yzm in tup:
    print(yzm)
print('你的验证码为;' + tup)
