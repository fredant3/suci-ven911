from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import ProyectoRepository


class ProyectoService(CrudService):
    def __init__(self):
        self.repository = ProyectoRepository()
