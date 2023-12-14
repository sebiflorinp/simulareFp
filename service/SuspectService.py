class SuspectService:
	def __init__(self, repo, validator):
		self.__repo = repo
		self.__validator = validator
	
	def getAllSuspects(self, name):
		allData = self.__repo.getAllSuspects()
		filteredData = []
		for data in allData:
			if data.name == name:
				filteredData.append(data)
		filteredData.sort(key=lambda data: data.getDate())
		return filteredData
		