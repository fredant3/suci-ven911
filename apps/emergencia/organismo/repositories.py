from helpers.RepositoryMixin import Repository
from emergencia.organismo.models import OrganismoCompetente


class OrganismoRepository(Repository):
    def __init__(self):
        self.entity = OrganismoCompetente
