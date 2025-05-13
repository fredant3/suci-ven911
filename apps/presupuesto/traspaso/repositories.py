from presupuesto.traspaso.models import Traspaso
from helpers.RepositoryMixin import Repository


class TraspasoRepository(Repository):
    def __init__(self):
        self.entity = Traspaso
