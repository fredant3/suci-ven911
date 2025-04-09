from helpers.RepositoryMixin import Repository
from tecnologia.auditoria.models import Auditoria


class AuditoriaRepository(Repository):
    def __init__(self):
        self.entity = Auditoria
