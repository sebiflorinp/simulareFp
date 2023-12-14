from utils.errors import SuspectRepoError

class SuspectRepo:
	def __init__(self):
		self.__suspects = {}
	
	def addSuspect(self, suspect):
		if suspect.getId() in self.__suspects:
			raise SuspectRepoError
		self.__suspects[suspect.getId()] = suspect
		
	def getAllSuspects(self):
		data = []
		for suspect in self.__suspects:
			data.append(self.__suspects[suspect])
		return data