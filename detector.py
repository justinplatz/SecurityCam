import cv2
import sys
import random


class Detector():
	def __init__(self, image):
		self.image_name = image
		self.image = []
		self.drawn = 0
		self.drawColors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
		# self.path  = "/home/pi/CV/opencv-2.4.10/data/haarcascades/"
		self.path = "xml/"
		self.rects = []
		self.overlays = ["face","obama","lebron","curry", "nick", 
						"bat", "captain", "hulk", "ironman", "spider","xmen"]

	def detect(self, xml):
		cascade = cv2.CascadeClassifier(self.path + xml)
		self.image = cv2.imread(self.image_name)
		gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
		hits = cascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(10, 10),
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		self.rects.append(hits)
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
		return self.detect("hogcascade_pedestrians.xml")

	def draw(self):
		for hits in self.rects:
			color = self.drawColors[self.drawn % len(self.drawColors)]
			self.drawn += 1
			for (x,y,w,h) in hits:
				cv2.rectangle(self.image, (x, y), (x+w, y+h), color, 1)
		cv2.imwrite(self.image_name, self.image)
		return hits

	def overlay(self):
		for (x,y,w,h) in self.rects[0]:
			img_offset = 30
			x_offset = x
			y_offset = y - img_offset/2
			img = random.choice(self.overlays)
			s_img = cv2.imread("Overlay/"+img+".png", -1)
			s_img = cv2.resize(s_img, (w,h+img_offset))
			for c in range(0,3):
			    self.image[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] =  \
			    s_img[:,:,c] * (s_img[:,:,3]/255.0) +  self.image[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] * (1.0 - s_img[:,:,3]/255.0)
			cv2.imwrite(self.image_name, self.image)
			# cv2.imshow('image',self.image)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

## Test
# det = Detector("img_5.jpg")
# print det.pedestrian()
