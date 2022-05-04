import cv2 as cv

# ctrl + / for comment toggles!!!!

# FUNCTIONS START
def rescaleFrame(frame, scale=0.75):
    #works on Images/Video/'Live' Video
    width = int(frame.shape[1] * scale)          # 1 references width
    height = int(frame.shape[0] * scale)         # 0 references height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Works on live video only (camera/webcam)
    capture.set(3,width) # 3 references width
    capture.set(4,height) #4 references the height

# FUNCTIONS END

# Reading images
img = cv.imread('Photos/cat_large.jpg')

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

# Maniputing/Displaying the image
resized_image = rescaleFrame(img)
cv.imshow('Cat Resized', resized_image)
cv.imshow('Cat', img)


# Manipulating/Displaying the video (no audio)
while True:
   isTrue, frame = capture.read()              # Reads the video frame by frame
   frame_resized = rescaleFrame(frame)         # manipulates the read frame of the video

   cv.imshow('Video', frame)
   cv.imshow('Video Resized', frame_resized)


   if cv.waitKey(20) & 0xFF==ord('d'):         # Makes sure the video doesn't infinite loop
       break
capture.release()


# Closes the windows made
cv.destroyAllWindows()
cv.waitKey(0)                 # 0 means to wait infinitely (until the window is closed)