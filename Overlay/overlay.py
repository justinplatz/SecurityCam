import cv2


def transparentOverlay():
	# s_img = cv2.imread("face.png")
	l_img = cv2.imread("person.jpg")
	x_offset=160
	y_offset=35
	# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

	s_img = cv2.imread("face.png", -1)
	s_img = cv2.resize(s_img, (100,100))
	for c in range(0,3):
	    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] =  \
	    s_img[:,:,c] * (s_img[:,:,3]/255.0) +  l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] * (1.0 - s_img[:,:,3]/255.0)

	cv2.imshow('image',l_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
transparentOverlay()
