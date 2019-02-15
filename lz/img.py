# -*- coding: UTF-8 -*-

#图片剪裁
from PIL import Image,ImageFilter

#打开一个jpg图像文件，注意是当前路径
im = Image.open('timg.jpg')
print(im)
#获得图像尺寸
w,h = im.size
print(w,h)
#缩放到50%
im.thumbnail((w//2,h//2))
im.save('thumbnail.jpg','jpeg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
