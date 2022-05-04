import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])         # needs a tranform array
    dimensions = (img.shape[1], img.shape[0])         # dimensions are a tuple
    return cv.warpAffine(img, transMat, dimensions)   # takes the photo, the transform array, and the dimensions as arguments


# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down 


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)


resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #shrinking, use AREA... for enlarging, use CUBIC (slower) or LINEAR (faster)
cv.imshow('Resized', resized)

flip = cv.flip(img, -1) # 1 for veritcal, 0 for horizontal, -1 for both
cv.imshow('flip', flip)

cropped = img[200:400, 300:400] # starting x,y coord, ending x,y coord?
cv.imshow('cropped', cropped)

cv.waitKey(0)