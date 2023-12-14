class Suspect:
	def __init__(self, id, description, date, type, name):
		"""
		The constructor of the Suspect class.
		Preconditions: id: a positive integer
									 description: a string
									 date: a datetime object
									 
		"""
		self.__id = id
		self.__description = description
		self.__date = date
		self.__type = type
		self.__name = name
	
	def __str__(self):
		return f"{self.__id},{self.__description},{self.__date.year}/{self.__date.month}/{self.__date.day},{self.__type},{self.__name}"
	
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