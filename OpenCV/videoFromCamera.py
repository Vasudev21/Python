# This program uses the webcam to record a video
import cv2
import numpy as np

filename = 'output.avi'

print "Opening video camera is a success"

cap = cv2.VideoCapture(0)
# Create a VideoWriter object to record a video
out = cv2.VideoWriter(filename,cv2.cv.CV_FOURCC('X','V','I','D'),30.0,(640,480))

print "Recording video................."

while(cap.isOpened()):

	ret, frame = cap.read()

	if ret==True:
		out.write(frame)
		cv2.imshow('Frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		out.release()
		break

print "Closing file..................."
print "File saved as %s" % filename
cap.release()
cv2.destroyAllWindows()
