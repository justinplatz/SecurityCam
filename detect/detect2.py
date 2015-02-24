import cv2
import sys



class Detector():
	def __init__(self, image):
		self.image = image
		self.path = "/home/pi/CV/opencv-2.4.10/data/haarcascades/"

	def detect(self, xml):
		cascade = cv2.CascadeClassifier(self.path + xml)
		img = cv2.imread(self.image)
		gray = cv2.cvtColor(, cv2.COLOR_BGR2GRAY)
		hits = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(10, 10),
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	def face(self):
		return self.detect('haarcascade_frontalface_alt.xml')

	def face2(self):
		return self.detect('haarcascade_frontalface_alt.xml')

det = new Detector("img_5.jpg")

print det.face()
