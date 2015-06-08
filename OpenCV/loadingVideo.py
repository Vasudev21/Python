# Program loads and displays a video.
import cv2
import numpy

# Load a video named KP.mp4
cap = cv2.VideoCapture("KP.mp4")

# Read every frame and display.
while(cap.isOpened()):
	ret, frame = cap.read()

	# If there is a frame then convert it to gray and display
	if(ret):
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		# Display the image in a new window named 'frame'
		cv2.imshow('frame',gray)
		# If 'q' key is pressed close the program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		cap.release()
		cv2.destroyAllWindows()
