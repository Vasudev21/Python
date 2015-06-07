import cv2
import numpy as np


print "Opening video camera is a success"
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi',cv2.cv.CV_FOURCC('X','V','I','D'),30.0,(640,480))
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
	#	gray = cv2.cvtColor(frame,cv2.cv.COLOR_BGR2GRAY)
		out.write(frame)
		cv2.imshow('Frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		out.release()
		break

cap.release()
cv2.destroyAllWindows()
