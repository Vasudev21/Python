import cv2
import numpy

cap = cv2.VideoCapture("KP.mp4")
#print cap.shape
while(cap.isOpened()):
	ret, frame = cap.read()
	if(ret):
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		cap.release()
		cv2.destroyAllWindows()
