# file containing all needed classes


# node of our graphs
class Node_rpg:
	def __init__(self, informations):
		self._name    = informations[0]
		self._id      = informations[1]
		self._vampire = informations[2] == "Y"
		self._pc      = informations[3] == "Y"

class Edge_rpg:
	def __init__(self, informations):
		self._source  = informations[0]
		self._arrival = informations[1]
		self._links   = informations[2]

