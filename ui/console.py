class Console:
	def __init__(self, suspectService, fileRepo):
		"""
		The constructor of the Console class.
		Preconditions: suspectService: an instance of the SuspectService class.
									 fileRepo: an instance of the FileRepo class.
		"""
		self.__suspectService = suspectService
		self.__fileRepo = fileRepo
		
	def run(self):
		"""
		A function that is run when the app opens.
		Preconditions: -
		Post-conditions: -
		"""
		data = self.__fileRepo.loadData()
		for suspect in data:
			self.__suspectService.addSuspect(suspect)
		print("Welcome!!!!!!")
		print("This app is used to manage criminal cases.")
		print("This app can be used through the following commands:\n  display evidence by suspect\n  find criminals\n  exit")
		while True:
			command = input("Enter a command.\n")
			if command == "display evidence by suspect":
				name = input("Enter suspects name.\n")
				dataToDisplay = self.__suspectService.getSuspectByName(name)
				for suspect in dataToDisplay:
					print(suspect)
			if command == "find criminals":
				dataToDisplay = self.__suspectService.getSuspectsByEvidence()
				for data in dataToDisplay:
					print(data)
			if command == "exit":
				return 