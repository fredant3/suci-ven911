from helpers.RepositoryMixin import Repository
from tecnologia.models import Tecnologia


class TecnologiaRepository(Repository):
    def __init__(self):
        self.entity = Tecnologia
