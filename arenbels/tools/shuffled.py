from random import shuffle

def shuffled(L):
	"""Returns a shuffled version of a shallow copy of L
	
	In : list
	Out : list
	"""
	K = L.copy()
	shuffle(K)
	return K
	
