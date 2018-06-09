'''
Font: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
'''
from PIL import Image
import sys
import util

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']


def __scale_image(image, new_width=100):
	"""
	Resizes an image preserving the aspect ratio.
	"""
	(original_width, original_height) = image.size
	aspect_ratio = original_height/float(original_width)
	new_height = int(aspect_ratio * new_width)

	new_image = image.resize((new_width, new_height))
	return new_image


def __convert_to_grayscale(image):
	# TODO: usar algoritmo feito para os projetos
	return image.convert('L')


def __map_pixels_to_ascii_chars(image, range_width=25):
	"""
	Maps each pixel to an ascii char based on the range
	in which it lies.

	0-255 is divided into 11 ranges of 25 pixels each.
	"""

	pixels_in_image = list(image.getdata())
	pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
					   pixels_in_image]

	return "".join(pixels_to_chars)


def __convert_image_to_ascii(image, new_width=100):
	image = __scale_image(image)
	image = __convert_to_grayscale(image)

	pixels_to_chars = __map_pixels_to_ascii_chars(image)
	len_pixels_to_chars = len(pixels_to_chars)

	image_ascii = [pixels_to_chars[index: index + new_width] for index in
				   xrange(0, len_pixels_to_chars, new_width)]

	return "\n".join(image_ascii)


def handle_image_conversion(image = None, image_filepath = None):
	'''
	Can receive an image already readed or image path
	params:
		image is an openCv image
	'''

	# read image
	if image is None:
		try:
			# try to read the image
			image = Image.open(image_filepath)
		except Exception, e:
			print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
			print e
			return
	else:
		image = util.convertCV2toPIL(image)

	image_ascii = __convert_image_to_ascii(image)
	# print image_ascii
	return image_ascii


if __name__ == '__main__':
	'''
	use this only for test
	'''
	# image_file_path = sys.argv[1]
	image_file_path = "/media/luiz/sata/Documentos/ciencia_da_computacao/PDI/CC-PDI-CharacterIdentifier/testeCases/unknown/deleteme-1.png"
	a = handle_image_conversion(image_filepath=image_file_path)
	import pdb; pdb.set_trace()
