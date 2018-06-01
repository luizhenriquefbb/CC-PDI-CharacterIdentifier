'''
Util methods
'''

import cv2
import PIL

def resizeImage(image, x=80, y=80):
	'''
	Resizes an image

	Params:
		x and y are width and height respectively
	'''
	return cv2.resize(image, (x, y))

def convertCV2toPIL(cv2_im):
	'''
	Unfortunately we are using two libs to handle image. So the faster way to fix problems is using
	a convesor

	Params:
		cv2_im = image in openCv format
	'''
	return PIL.Image.fromarray(cv2_im)


def cleanImage(image):
	'''
	Consider only black pixels within a range
	'''

	for row in range(len(image)):
		for colunm in range(len(image[row])):
			if image[row][colunm][0] > 20 or image[row][colunm][1] > 20 or image[row][colunm][2] > 20:
				image[row][colunm] = [255,255,255]

	return image
