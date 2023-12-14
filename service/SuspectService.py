import datetime


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

	def getSuspectsByEvidence(self):
		allData = self.__repo.getAllSuspects()
		dataToReturn = []
		names = []
		for data in allData:
			if data.getName() not in names:
				names.append(data.getName())
		for name in names:
			evidence = []
			for data in allData:
				if data.getName() == name:
					evidence.append(data)
			evidence.sort(key=lambda pieceOfEvidence: pieceOfEvidence.getDate(), reverse=True)
			status = ""
			if len(evidence) >= 3:
				status = "criminal"
			else:
				status = "inocent"
			time = evidence[0].getDate() - evidence[len(evidence) - 1].getDate()
			timeToDisplay = time.days
			dataToReturn.append(f"{name}: {len(evidence)}, {timeToDisplay},"
			                    f" {status}")
		return dataToReturn
		