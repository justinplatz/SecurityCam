import cv2
import sys



class Detector():
	def __init__(self, image):
		self.image = image
		self.path = "/home/pi/CV/opencv-2.4.10/data/haarcascades/"

	def detect(self, xml):
		cascade = cv2.CascadeClassifier(self.path + xml)
		img = cv2.imread(self.image)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		hits = cascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(10, 10),
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		return hits

	def face(self):
		return self.detect('haarcascade_frontalface_default.xml')

	def face2(self):
		return self.detect('haarcascade_frontalface_alt.xml')

	def face3(self):
		return self.detect('haarcascade_frontalface_alt2.xml')

	def full_body(self):
		return self.detect('haarcascade_fullbody.xml')

	def upper_body(self):
		return self.detect('haarcascade_upperbody.xml')

	def pedestrian(self):
		return self.detect("../hogcascades/hogcascade_pedestrians.xml")

## Test
# det = Detector("img_5.jpg")
# print det.pedestrian()
