import cv2
import numpy as np

# Creating a video capture device 
cap = cv2.VideoCapture(0)

# Creating a video writer device
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
while(cap.isOpened()):
	ret,frame = cap.read()
	cv2.imshow('Test',frame)
#	if ret==True:
#		frame = cv2.flip(frame,0)

	# Write the flipped frame
#	out.write(frame)
	
#	cv2.imshow('frame',frame)
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
