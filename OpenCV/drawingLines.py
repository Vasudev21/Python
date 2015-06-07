# Program draws primitives on an image.
import cv2
import numpy as np

# Create a blank black image of width,height,depth: 512x512x3
img = np.zeros((512,512,3), np.uint8)

# Draw a line from (0,0) to (511,511)
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a rectangle from (384,0) to (510,510)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle with center (450,63) and radius 63
cv2.circle(img,(450,63),63,(0,0,255),-1)

# Draw an ellipse center location (255,255) and major axis: 100 and minor axis 50)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw a polygon with points below
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.CV_AA)

# Display the image
cv2.imshow('frame',img)

# Wait for a key before closing the image (0 means indefinitely)
cv2.waitKey(0)
