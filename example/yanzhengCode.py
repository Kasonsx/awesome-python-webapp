# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math
#随机生成字母或数字
def randChar():
	if round(random.random())==0:
		return chr(random.randint(65,90))
	else:
		return chr(random.randint(48,57))
	
def randColor():
	return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def randColor2():
	return (random.randint(32,127), random.randint(32,127), random.randint(32,127))
#旋转模糊处理
def twist(img):
	src_img = img.copy()
	cycle = 3
	y_amp = 3.5
	for y in range(0,height):
		for x in range(0,width):
			new_y = y + round(math.sin(x*2*math.pi*cycle/width)*y_amp)
			if new_y < height and new_y > 0:
				img.putpixel((x,new_y),src_img.getpixel((x,y)))
	return img
width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255,255,255))

font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=randColor())

for t in range(4):
	draw.text((60*t+10,10),randChar(), font=font,fill=randColor2())

image = image.filter(ImageFilter.BLUR)
image = twist(image)
image.save('code.jpg','jpeg')
