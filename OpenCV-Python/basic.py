import cv2 as cv

# Baseline
img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# 1. Converting to greyscale
#####################################

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur an image
#####################################

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
#####################################
canny = cv.Canny(img, 125, 175)
cv.imshow('CannyEdges', canny)
cannyblur = cv.Canny(blur, 125,175)
cv.imshow('Blurred CannyEdges', cannyblur)

# Dilating the image
#####################################
dilated = cv.dilate(cannyblur, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
#####################################
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
#####################################
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)





cv.waitKey(0)