import datetime
from domain.objects import Suspect

class FileRepo:
	def loadData(self):
		"""
		A function that returns all data from the data.txt file.
		Preconditions: -
		Post-conditions: a list with instances of the Suspect class.
		"""
		dataToReturn = []
		with open("C:\\sebifp\\jetBrains\\homework\\simulareFP\\files\\data.txt", "r") as file:
			line = file.readline().strip().split(",")
			while len(line) == 5:
				id = line[0]
				description = line[1]
				dateSplit = line[2].split("/")
				year = dateSplit[0]
				month = dateSplit[1]
				day = dateSplit[2]
				date = datetime.date(int(year), int(month), int(day))
				type = line[3]
				name = line[4]
				suspect = Suspect(id, description, date, type, name)
				dataToReturn.append(suspect)
				line = file.readline().strip().split(",")
		return dataToReturn
			