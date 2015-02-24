import cv2
import sys

if len(sys.argv) < 2:
	print "Improper Usage. Need photo File and Algorithm XML."
	sys.exit(0)


cascPath = "/home/pi/CV/opencv-2.4.10/data/hogcascades/hogcascade_pedestrians.xml"

print cascPath

faceCascade = cv2.CascadeClassifier(cascPath)

img = cv2.imread(sys.argv[1])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Faces Detected:", faces
