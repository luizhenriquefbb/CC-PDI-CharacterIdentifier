'''
Util methods
'''

import cv2
import PIL

def resizeImage(image, x=67, y=67):
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
