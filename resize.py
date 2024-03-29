import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


capture = cv.VideoCapture('./videos/1.mp4')

while True:
	isTrue, frame = capture.read()
	frame_resized = rescaleFrame(frame)
	cv.imshow('Video', frame_resized)

	if cv.waitKey(20) & 0xFF == ord('d'): # If d is pressed 
		break

cv.waitKey(0)