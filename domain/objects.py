class Suspect:
	def __init__(self, id, description, date, type, name):
		"""
		The constructor of the Suspect class.
		Preconditions: id: a positive integer
									 description: a string
									 date: a datetime object
									 type: a string that has to be one of the following: DNA, photo, object, statement
									 name: a string 
		"""
		self.__id = id
		self.__description = description
		self.__date = date
		self.__type = type
		self.__name = name
	
	def __str__(self):
		"""
		A function that returns a certain value when the object is printed.
		"""
		return f"{self.__id},{self.__description},{self.__date.year}/{self.__date.month}/{self.__date.day},{self.__type},{self.__name}"
	
	def getId(self):
		"""
		A function that returns the id of the Suspect.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__id

	def getDescription(self):
		"""
		A function that returns the description of the Suspect.
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__description	

	def getDate(self):
		"""
		A function that returns the date of the Suspect.
		Preconditions: -
		Post-conditions: a datetime object
		"""
		return self.__date	

	def getType(self):
		"""
		A function that returns the type of the Suspect.
		Preconditions: -
		Post-conditions: a string that has to be one of the following: DNA, photo, object, statement
		"""
		return self.__type	

	def getName(self):
		"""
		A function that returns the name of the Suspect.
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__name	