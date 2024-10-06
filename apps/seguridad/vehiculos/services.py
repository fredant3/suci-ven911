from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import VehiculoRepository


class VehiculoService(CrudService):
    def __init__(self):
        self.repository = VehiculoRepository()
