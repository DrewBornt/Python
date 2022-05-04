import cv2 as cv
import numpy as np

                 #height, width, number of color channels
blank = np.zeros((500,500,3), dtype='uint8') # uint8 is for images
# cv.imshow('Blank', blank)

# 1. Paint the image a certain color
#####################################

# blank[:] = 0,255,0 #b, g, r
# cv.imshow('Green', blank)

# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green with Red Square', blank)

# 2. Draw a rectangle
#####################################

# rectangle(image, top left corner point, bottom right corner point, color, thickness)
#cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2) #thickness=cv.FILLED or thickness=-1 for filling in the square
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=2) this will create a square with size half the height and half the width
# This starts from the top left corner and goes left to right and down.

#cv.imshow('Blue Rectangle', blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# 3. Draw a circle
#####################################

# circle(image, center of circle, radius in pixels, color, thickness)
# cv.circle(blank, (250,250), 40, (0,255,255), thickness=3)
# cv.imshow('With Circle', blank)

# 4. Draw a line
#####################################

# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,0), thickness=2)
# cv.imshow('Line', blank)

# 5. Text on an image
#####################################

cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)