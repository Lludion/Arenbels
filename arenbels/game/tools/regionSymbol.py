
def chreg(i):
	""" returns the char defining the ith region"""
	return chr(48 + i)

def regionSymbol(region,i):
	""" returns the string defining the region in a .arb file"""
	st = chreg(i) + region.name
	if region.sea:
		st += "#"
	return st + "\n"
