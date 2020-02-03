

def cost(money,building):
	""" Ensures the money is efficient to build the building "building"
	
	In : int, class game.building.Building
	Out : bool
	"""
	return money >= building().cost
