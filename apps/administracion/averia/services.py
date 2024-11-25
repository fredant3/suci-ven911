from administracion.averia.repositories import AveriaRepository
from django.db.models import Q
from helpers.CrudMixin import CrudService


class AveriaService(CrudService):
    def __init__(self):
        self.repository = AveriaRepository()
