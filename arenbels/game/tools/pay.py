

def pay(state,building):
	"""Pays the required money to build the building "building"
	
	In : class game.state.State, class game.building.Building
	Out : None
	"""
	state.treasure -= building().cost
