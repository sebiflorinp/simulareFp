from utils.errors import SuspectRepoError

class SuspectRepo:
	def __init__(self):
		"""
		The constructor of the SuspectRepo class.
		Preconditions: -
		"""
		self.__suspects = {}
	
	def addSuspect(self, suspect):
		"""
		A function that adds the received suspect in the suspect dictionary.
		Preconditions: suspect: an instance of the Suspect class
		Post-conditions: -
		"""
		if suspect.getId() in self.__suspects:
			raise SuspectRepoError
		self.__suspects[suspect.getId()] = suspect
		
	def getAllSuspects(self):
		"""
		A function that returns all suspects in the dictionary in a list.
		Preconditions: -
		Post-conditions: a list with all instances of the Suspect class in the repo.
		"""
		data = []
		for suspect in self.__suspects:
			data.append(self.__suspects[suspect])
		return data