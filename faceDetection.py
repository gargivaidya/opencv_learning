import cv2 as cv

img = cv.imread('./photos/Profile.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haarFace.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 3)
print('Number of Faces', len(faces_rect))

for (x, y, w, h) in faces_rect:
	cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)

cv.imshow('Detected Images', img)
cv.waitKey(0)