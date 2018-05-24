
import numpy as np

def levenshtein(source, target):
	'''
	Distance between 2 words. The larger the integer, the more different the strings are

	Font to more versions:
		# https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
	'''
	
	print("initializing levenshetein")


	if len(source) < len(target):
		return levenshtein(target, source)

	# So now we have len(source) >= len(target).
	if len(target) == 0:
		return len(source)

	# We call tuple() to force strings to be used as sequences
	# ('c', 'a', 't', 's') - numpy uses them as values by default.
	source = np.array(tuple(source))
	target = np.array(tuple(target))

	# We use a dynamic programming algorithm, but with the
	# added optimization that we only need the last two rows
	# of the matrix.
	previous_row = np.arange(target.size + 1)
	for s in source:
		# Insertion (target grows longer than source):
		current_row = previous_row + 1

		# Substitution or matching:
		# Target and source items are aligned, and either
		# are different (cost of 1), or are the same (cost of 0).
		current_row[1:] = np.minimum(
			current_row[1:],
			np.add(previous_row[:-1], target != s))

		# Deletion (target grows shorter than source):
		current_row[1:] = np.minimum(
			current_row[1:],
			current_row[0:-1] + 1)

		previous_row = current_row

	return previous_row[-1]

 
if __name__ == '__main__':
	'''
	Test methos only
	'''
	s1 = 'casa'
	s2 = 'csa'
	s3 = 'nada a ver'
	s4 = 'kasa'

	print(s1, s2, levenshtein(s1, s2))
	print(s1, s3, levenshtein(s1, s3))
	print(s1, s4, levenshtein(s1, s4))
