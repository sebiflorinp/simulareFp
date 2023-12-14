from domain.validators import SuspectValidator
from repository.memoryRepo import SuspectRepo
from service.SuspectService import SuspectService
from ui.console import Console
from repository.fileRepo import FileRepo
# Create DNA Service and its dependencies
repo = SuspectRepo()
validator = SuspectValidator()
service = SuspectService(repo, validator)
fileRepo = FileRepo()

# Create console
console = Console(service, fileRepo)

# Run the app
console.run()