import numpy as np

def translation(img, tx, ty):
    '''tx: x軸方向の移動量, ty: y軸方向の移動量'''
    rows, cols, _ = img.shape
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst

def scaling(img, sx, sy):
    '''sx: x軸方向の拡大率, sy: y軸方向の拡大率'''
    rows, cols, _ = img.shape
    M = np.float32([[sx, 0, 0], [0, sy, 0]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst

def rotation(img, angle):
    '''angle: 回転角度'''
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


def skew(img, skew_x, skew_y):
    '''skew_x: x軸方向の傾き'''
    rows, cols, _ = img.shape
    M = np.float32([[1, skew_y, 0], [skew_x, 1, 0]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst

def flip(img, flip_mode):
    '''flip_mode: 0: x軸方向, 1: y軸方向, -1: 両方'''
    dst = cv2.flip(img, flip_mode)
    return dst

def composite(img):
    dst = translation(img, 50, 50)
    dst = scaling(dst, 1.2, 0.8)
    dst = rotation(dst, 45)
    dst = skew(dst, 0.3, 0.2)
    dst = flip(dst, 1)
    return dst

import cv2

img = cv2.imread('cat.jpg')

'''
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#すべての関数を一通り使用する。

dst = translation(img, 50, 50)
cv2.imshow('translation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = scaling(img, 1.2, 0.8)
cv2.imshow('scaling', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = rotation(img, 45)
cv2.imshow('rotation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


dst = skew(img, 0.3, 0.2)
cv2.imshow('skew', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = flip(img, 1)
cv2.imshow('flip', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
dst = composite(img)
cv2.imshow('composite', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

