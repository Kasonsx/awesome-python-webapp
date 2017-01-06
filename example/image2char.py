# -*- coding:utf-8 -*-
from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')# 输入文件
parser.add_argument('-o','--output') # 输出文件
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

#获取参数
args = parser.parse_args()
IMG = args.file
Width = args.width
Height = args.height
Output = args.output
# 转换字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256个灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

	unit = (256.0 +1)/length
	return ascii_char[int(gray/unit)]
if __name__ == '__main__':
	im = Image.open(IMG )
	im = im.resize((Width,Height), Image.NEAREST)

	txt = ""

	for i in range(Height):
		for j in range(Width):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'
	print(txt)

	#字符画输出到文件：
	if Output:
		with open(Output,'w') as f:
			f.write(txt)
	else:
		with open("output.txt",'w') as f:
			f.write(txt)

