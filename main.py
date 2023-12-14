from domain.objects import Suspect
from domain.validators import SuspectValidator
from repository.memoryRepo import SuspectRepo
from service.SuspectService import SuspectService
from ui.console import Console

# Create DNA Service and its dependencies
repo = SuspectRepo()
validator = SuspectValidator()
service = SuspectService(repo, validator)

# Create console
console = Console(service)

# Run the app
console.run()