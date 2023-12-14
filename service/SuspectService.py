class SuspectService:
	def __init__(self, repo, validator):
		"""
		The constructor of the SuspectService class.
		Preconditions: repo: an instance of the SuspectRepo class
									 validator: an instance of the SuspectValidator class
		"""
		self.__repo = repo
		self.__validator = validator
		
	def addSuspect(self, suspect):
		"""
		A function that adds the received suspect in the suspect repo.
		Preconditions: suspect: an instance of the Suspect class.
		Post-conditions: -
		Raises: SuspectRepoError
		"""
		self.__repo.addSuspect(suspect)
		
	def getSuspectByName(self, name):
		"""
		A function that returns all evidence of the suspect who has the input name or a message if there's no evidence.
		Preconditions: name: a string
		Post-conditions: a list with Suspect objects.
		"""
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
		"""
		A function that returns a list of strings that shows if a certain suspect is innocent or guilty.
		Preconditions: -
		Post-conditions: a list of strings that have the following format: <suspect name>,<numberOfEvidence>,
		<time between first and last evidence found>,<inocent or criminal>
		"""
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
		