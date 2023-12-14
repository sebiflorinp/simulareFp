class Console:
	def __init__(self, SuspectService):
		self.__SuspectService = SuspectService
		
	def run(self):
		print("Welcome!!!!!!")
		print("This app is used to manage criminal cases.")
		print("This app can be used through the following commands:\n  display evidence by suspect\n  find criminals\n  exit")
		while True:
			command = input("Enter a command.\n")
			if command == "display evidence by suspect":
				name = input("Enter suspects name.\n")
				dataToDisplay = self.__SuspectService.getAllSuspects()
				for suspect in dataToDisplay:
					print(suspect)
			if command == "find criminals":
				pass
			if command == "exit":
				return 