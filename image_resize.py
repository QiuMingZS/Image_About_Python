# -*- coding:utf-8 -*-
# image_resize.py
from PIL import Image

img = Image.open('Images/grant.jpg')
img_size = img.size
print('Size: {}'.format(img_size))

if img_size[0] <= img_size[1]:
    new_size = img_size[0]
    left = 0
    up = (img_size(1) - new_size) / 2
else:
    new_size = img_size[1]
    left = (img_size[0] - new_size) / 2
    up = 0
width = new_size
depth = new_size

region = img.crop((left, up, left + width, up + depth))
region.save("./Images_resize/grant_square.jpg")
