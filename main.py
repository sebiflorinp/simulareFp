from domain.objects import DNA
from domain.validators import DNAValidator
from repository.memoryRepo import DNARepo
from service.DNAService import DNAService
from ui.console import Console

# Create DNA Service and its dependencies
repo = DNARepo()
validator = DNAValidator()
service = DNAService(repo, validator)

# Create console
console = Console(service)

# Run the app
console.run()