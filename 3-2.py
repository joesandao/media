from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def resize_img(img, scale_factor, interpolation):
    '''img: 画像, scale_factor: 拡大率, interpolation: 補間方法'''
    # 画像のサイズを取得
    width, height = img.size
    print("width = ", width)
    print("height = ", height)
    print("interpolation = ", interpolation)
    
    # 拡大後のサイズを計算
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    
    # 画像の拡大
    img_resized = img.resize((new_width, new_height), resample=interpolation)
    
    return img_resized

# 画像の読み込み
img = Image.open('cat.jpg')
plt.imshow(img)
plt.show()

# NEARESTでの拡大

start = time.time()
img_nn = resize_img(img, 2, Image.NEAREST)
plt.imshow(img_nn)
end = time.time()
print("NEAREST time = ", end - start)
plt.show()

# BILINEARでの拡大
start = time.time()
img_bil = resize_img(img, 2, Image.BILINEAR)
plt.imshow(img_bil)
end = time.time()
print("BILINEAR time = ", end - start)
plt.show()

# CUBICでの拡大
start = time.time()
img_cub = resize_img(img, 2, Image.CUBIC)
plt.imshow(img_cub)
end = time.time()
print("CUBIC time = ", end - start)
plt.show()

#結果を保存
img_nn.save('cat_nn.jpg')
img_bil.save('cat_bil.jpg')
img_cub.save('cat_cub.jpg')