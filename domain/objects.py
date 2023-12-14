class Suspect:
	def __init__(self, id, description, date, type, name):
		self.__id = id
		self.__description = description
		self.__date = date
		self.__type = type
		self.__name = name
	
	def getId(self):
		return self.__id

	def getDescription(self):
		return self.__description	

	def getDate(self):
		return self.__date	

	def getType(self):
		return self.__type	

	def getName(self):
		return self.__name	