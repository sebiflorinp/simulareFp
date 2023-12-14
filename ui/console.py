class Console:
	def __init__(self, DNAService):
		self.__DNAService = DNAService
		
	def run(self):
		print("Welcome!!!!!!")
		print("This app is used to manage criminal cases.")
		print("This app can be used through the following commands:\n  display evidence by suspect\n  find criminals\n  exit")
		while True:
			command = input("Enter a command.\n")
			if command == "display evidence by suspect":
				pass
			if command == "find criminals":
				pass
			if command == "exit":
				return 