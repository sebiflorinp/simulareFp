class SuspectService:
	def __init__(self, repo, validator):
		self.__repo = repo
		self.__validator = validator
		
	def addSuspect(self, suspect):
		self.__repo.addSuspect(suspect)
		
	def getSuspectByName(self, name):
		allData = self.__repo.getAllSuspects()
		filteredData = []
		for data in allData:
			if data.getName() == name:
				filteredData.append(data)
		if len(filteredData) > 0:
			filteredData.sort(key=lambda data: data.getDate(), reverse=True)
		else:
			filteredData.append("There's is no evidence of the input suspect")
		return filteredData
		